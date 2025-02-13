import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma  # Vector store
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
import chainlit as cl

# Load environment variables from .env file
load_dotenv()

# Fetch API key from .env file
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")

if not HUGGINGFACEHUB_API_TOKEN:
    st.error("❌ Hugging Face API key is missing! Please check your .env file.")

# Ensure proper file upload handling
pages = []

def process_pdf(uploaded_file):
    try:
        pdf_reader = PdfReader(uploaded_file)
        return [page.extract_text() or "" for page in pdf_reader.pages]
    except Exception as e:
        return []

@cl.on_chat_start
async def main():  # Ensure this is async
    global pages
    uploaded_files = await cl.AskFileMessage(content="📄 Please upload a PDF file.", accept=["pdf"]).send()  # Await the message
    
    if not uploaded_files or len(uploaded_files) == 0:
        await cl.Message(content="⚠️ No PDF uploaded. Please upload a PDF file.").send()
        return

    pages = process_pdf(uploaded_files[0].path)
    if not pages:
        await cl.Message(content="⚠️ Unable to process the PDF. Ensure it's not empty or corrupted.").send()
        cl.user_session.set("retrieval_chain", None)
        return

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    docs = splitter.split_text("\n".join(pages))

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    doc_search = Chroma.from_texts(docs, embeddings)

    repo_id = "tiiuae/falcon-7b"
    llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={'temperature': 0.2, 'max_length': 1000})

    retrieval_chain = RetrievalQA.from_chain_type(llm, chain_type='stuff', retriever=doc_search.as_retriever())
    cl.user_session.set("retrieval_chain", retrieval_chain)
    await cl.Message(content="✅ PDF successfully processed! You can now ask questions.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    retrieval_chain = cl.user_session.get("retrieval_chain")
    if not retrieval_chain:
        await cl.Message(content="⚠️ Please upload and process a PDF before asking questions.").send()
        return

    textprompt = message.content
    res = await retrieval_chain.acall(textprompt, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res["result"]).send()

if __name__ == "__main__":
    cl.run()
