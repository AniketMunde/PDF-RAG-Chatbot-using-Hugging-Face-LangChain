
---

### **📚 PDF-RAG Chatbot using Hugging Face & LangChain**

This project is a **Retrieval-Augmented Generation (RAG) Chatbot** that allows users to upload PDFs and interact with them using AI-powered Q&A. It leverages **Hugging Face Transformers, LangChain, and FAISS** for document retrieval and large language model (LLM) inference.

---

## **Features**
- **PDF Upload**: Users can upload and process multiple PDFs.
- **Text Chunking & Embeddings**: Splits documents into smaller chunks and converts them into embeddings using **MiniLM**.
- **Vector Search with FAISS**: Efficient document retrieval using FAISS vector storage.
- **LLM-powered Q&A**: Uses **Falcon-7B** hosted on Hugging Face for answering questions.
- **Conversational Memory**: Remembers context to provide relevant responses.
- **Supports Streamlit and Chainlit**: Run the chatbot with a web interface using either **Streamlit** or **Chainlit**.

---

## **Tech Stack**
- **Python**
- **Streamlit / Chainlit** (Frontend UI)
- **LangChain** (RAG Implementation)
- **FAISS** (Vector Database)
- **Hugging Face Models** (MiniLM for embeddings, Falcon-7B for LLM)
- **PyPDF2** (PDF Processing)
- **dotenv** (Environment Variables)

---

## **Installation**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/AniketMunde/PDF-RAG-Chatbot-using-Hugging-Face-LangChain.git
   cd PDF-RAG-Chatbot-using-Hugging-Face-LangChain
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## **API Key Setup**
The project requires a **Hugging Face API Key** for accessing embeddings and LLM.

1. Create a `.env` file in the root directory:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
   ```
2. Replace `your_huggingface_api_key` with your actual key.

---

## **Running the Chatbot**
### **Using Streamlit**
Run the chatbot with **Streamlit** UI:
```bash
streamlit run pdf-rag-chatbot.py
```
This will open a browser where you can **upload PDFs and start asking questions**.

### **Using Chainlit**
Run the chatbot with **Chainlit** UI:
```bash
chainlit run chatpdf.py
```
This will launch a **Chatbot UI** where you can interact with the model.

---

## **How It Works**
1. Upload one or more PDFs.
2. The system **extracts text** and **splits it into chunks**.
3. Each chunk is **converted into vector embeddings** using **MiniLM**.
4. The embeddings are **stored in FAISS** for retrieval.
5. The chatbot uses **Falcon-7B** LLM to generate **context-aware answers** based on retrieved document sections.
6. Users can ask multiple questions, and the chatbot maintains **conversation memory**.

---

## **Troubleshooting**
- If you face **repository push protection issues**, ensure that API keys are removed from the commit history.
- If getting **ImportError: Dependencies for InstructorEmbedding not found**, install the missing dependencies:
  ```bash
  pip install langchain_huggingface
  ```
- If **Hugging Face model isn't loading**, verify your API key and model access permissions.

---

## **Contributing**
- Feel free to submit issues and pull requests.
- If you improve this project, consider sharing it back with the community.

---

## **License**
This project is licensed under the **MIT License**.

---

## **Acknowledgments**
Special thanks to **LangChain**, **Hugging Face**, and **Streamlit** for enabling easy AI-powered applications.

---
