import os
import shutil
import gradio as gr

from src.parser import parse_document
from src.chunker import create_chunks
from src.retriever import index_documents, retrieve_documents
from src.agents import generate_answer

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def upload_file(file):
    if file is None:
        return "Please upload a file."

    file_path = os.path.join(UPLOAD_DIR, os.path.basename(file.name))
    shutil.copy(file.name, file_path)

    extracted_text = parse_document(file_path)

    documents = create_chunks(
        text=extracted_text,
        filename=os.path.basename(file.name)
    )

    total_chunks = index_documents(documents)

    return f"""
File uploaded, parsed, chunked, and indexed successfully.

Filename: {os.path.basename(file.name)}
Total chunks stored in ChromaDB: {total_chunks}
"""

def ask_question(question):
    if not question.strip():
        return "Please enter a question."

    docs = retrieve_documents(question)

    if not docs:
        return "I could not find enough information in the uploaded document."

    answer = generate_answer(question, docs)

    sources = "\n".join(
        sorted(
            set(
                [
                    f"{doc.metadata.get('source')} | chunk {doc.metadata.get('chunk_id')}"
                    for doc in docs
                ]
            )
        )
    )

    return f"""
{answer}

Sources:
{sources}
"""

with gr.Blocks(title="Doc-Chat") as demo:
    gr.Markdown("# Doc-Chat\nDocument-grounded AI assistant.")

    file_input = gr.File(label="Upload PDF / DOCX / TXT / PPTX")
    upload_button = gr.Button("Upload and Index")
    upload_output = gr.Textbox(label="Upload Status", lines=8)

    upload_button.click(
        upload_file,
        inputs=file_input,
        outputs=upload_output
    )

    gr.Markdown("## Ask from uploaded document")

    question_input = gr.Textbox(
        label="Enter your question",
        placeholder="Example: What is the main objective of this document?"
    )

    ask_button = gr.Button("Ask Doc-Chat")
    answer_output = gr.Textbox(label="Answer", lines=18)

    ask_button.click(
        ask_question,
        inputs=question_input,
        outputs=answer_output
    )

demo.launch()