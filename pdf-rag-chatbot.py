import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS  # Vector store
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import RetrievalQA

# Load environment variables from .env file
load_dotenv()

# Fetch API key from .env file
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")

if not HUGGINGFACEHUB_API_TOKEN:
    st.error("❌ Hugging Face API key is missing! Please check your .env file.")

# Ensure proper file upload handling
def process_pdf(uploaded_file):
    try:
        pdf_reader = PdfReader(uploaded_file)
        return [page.extract_text() or "" for page in pdf_reader.pages]
    except Exception as e:
        return []

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    return text_splitter.split_text("\n".join(text))

def get_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return FAISS.from_texts(docs, embeddings)

def get_retrieval_chain(vectorstore):
    repo_id = "tiiuae/falcon-7b"
    llm = HuggingFaceEndpoint(repo_id=repo_id, task='text-generation', temperature=0.2, max_length=1000)
    return RetrievalQA.from_chain_type(llm, chain_type='stuff', retriever=vectorstore.as_retriever())

def main():
    st.set_page_config(page_title="Chat with PDFs using RAG")
    st.header("Chat with your PDFs 📄")
    
    uploaded_files = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=True)
    if uploaded_files and st.button("Process"):
        with st.spinner("Processing PDFs..."):
            all_text = []
            for file in uploaded_files:
                extracted_text = process_pdf(file)
                if extracted_text:
                    all_text.extend(extracted_text)
                else:
                    st.warning(f"⚠️ Could not extract text from {file.name}")
            
            if not all_text:
                st.error("❌ No text extracted from uploaded PDFs.")
                return
            
            text_chunks = get_text_chunks(all_text)
            vectorstore = get_vectorstore(text_chunks)
            st.session_state.retrieval_chain = get_retrieval_chain(vectorstore)
            st.success("✅ PDF successfully processed! You can now ask questions.")
    
    if "retrieval_chain" in st.session_state:
        user_question = st.text_input("Ask a question about your document:")
        if user_question:
            response = st.session_state.retrieval_chain.invoke(user_question)
            st.write("### 🤖 AI Response:")
            st.write(response)

if __name__ == "__main__":
    main()
