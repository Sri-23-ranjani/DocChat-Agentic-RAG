# Doc-Chat

## Multi-Agent RAG System for Long Document Understanding

Doc-Chat is an advanced document-grounded AI assistant that allows users to upload long documents and ask questions based on the uploaded content.

The system uses Retrieval-Augmented Generation (RAG) with vector embeddings, document parsing, and LLM-based answer generation to provide accurate and source-grounded answers.

---

## Features

- Upload PDF, DOCX, TXT, and PPTX documents
- Parse documents using Docling
- Chunk large documents intelligently
- Store embeddings using ChromaDB
- Retrieve relevant document sections
- Generate concise AI-powered answers
- Display supporting evidence and source chunks
- Reduce hallucinations using document-grounded prompting

---

## Tech Stack

- Python
- Gradio
- LangChain
- ChromaDB
- Docling
- Groq LLM
- Sentence Transformers

---

## Project Workflow

```text
Upload Document
        ↓
Document Parsing (Docling)
        ↓
Chunk Creation
        ↓
Embedding Generation
        ↓
Store in ChromaDB
        ↓
Question Retrieval
        ↓
LLM Answer Generation
        ↓
Source-Grounded Response
```

---

## Folder Structure

```text
doc-chat/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── parser.py
│   ├── chunker.py
│   ├── retriever.py
│   ├── agents.py
│   └── __init__.py
│
├── uploads/
├── chroma_db/
└── venv/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Sri-23-ranjani/DocChat-Agentic-RAG.git
```

### Navigate to Project

```bash
cd DocChat-Agentic-RAG
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run the Application

```bash
python app.py
```

---

## Example Questions

- What is this document about?
- Summarize the uploaded document
- What are the key points?
- Explain the main objective
- Give important findings from the document

---

## Future Improvements

- Hybrid Retrieval (BM25 + Vector Search)
- Verification Agent
- Hallucination Detection
- Self-Correction Loop
- Multi-document Querying
- Page-level Citations

---

## Author

Sri Ranjani V