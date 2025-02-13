

```markdown
# 📚 PDF-RAG Chatbot using Hugging Face & LangChain

A **Retrieval-Augmented Generation (RAG) Chatbot** that allows users to upload PDFs and ask questions based on their content. Built using **Hugging Face Transformers, LangChain, and FAISS**, this chatbot processes and stores document embeddings for efficient retrieval and AI-powered responses.

---

## **🚀 Features**
- 📄 **PDF Upload**: Users can upload multiple PDFs for analysis.
- 🔎 **Chunking & Vectorization**: Documents are split into smaller chunks and stored using **FAISS** for optimized search.
- 🤖 **LLM-powered Q&A**: Uses **Falcon-7B** (or any Hugging Face-hosted model) for answering questions.
- 🧠 **Context-aware Conversations**: Implements memory to maintain chat history.
- 🎨 **Web Interface**: Built with **Streamlit** for an interactive UI.

---

## **🛠️ Tech Stack**
- **Python**
- **Streamlit** (Frontend UI)
- **LangChain** (RAG Pipeline)
- **FAISS** (Vector Storage)
- **Hugging Face Models** (MiniLM, Falcon-7B)
- **PyPDF2** (PDF Processing)
- **dotenv** (Environment Variables)

---

## **⚡ Installation Guide**
1️⃣ **Clone the Repository**:
```bash
git clone https://github.com/AniketMunde/PDF-RAG-Chatbot-using-Hugging-Face-LangChain.git
cd PDF-RAG-Chatbot-using-Hugging-Face-LangChain
```

2️⃣ **Create Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate      # Windows
```

3️⃣ **Install Dependencies**:
```bash
pip install -r requirements.txt
```

---

## **🔑 API Key Setup**
This project requires **Hugging Face API Keys**.

1. Create a `.env` file in the root directory:
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```
2. Replace `your_huggingface_api_key` with your actual key.

---

## **🚀 How to Run**
To start the chatbot, run:
```bash
streamlit run pdf-rag-chatbot.py
```
It will launch the chatbot in your browser where you can **upload PDFs and ask questions**.

---

## **🛠️ Usage Instructions**
1. Upload one or multiple PDFs.
2. Click **"Process"** to extract text and create embeddings.
3. Ask questions based on the content.
4. The chatbot responds with **contextual answers** from the PDFs.

---

## **🤝 Contribution**
Feel free to:
- Open Issues & Bug Reports 🐛
- Suggest Enhancements 💡
- Submit Pull Requests ✨

Fork and contribute to make this **RAG-based chatbot even better**! 🚀

---

## **📝 License**
This project is **MIT Licensed**. You are free to modify and distribute it.

---

🚀 **Built with ❤️ by Aniket Munde**
```

---

