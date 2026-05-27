import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

def generate_answer(question, documents):
    context = "\n\n".join(
        [
            f"Source: {doc.metadata.get('source')} | Chunk: {doc.metadata.get('chunk_id')}\n{doc.page_content}"
            for doc in documents
        ]
    )

    prompt = f"""
You are Doc-Chat, a highly accurate document-grounded AI assistant.

Your task:
Answer the user's question using ONLY explicit information present in the document context.

Very Important Rules:
1. Do NOT infer beyond the document.
2. Do NOT generalize.
3. Do NOT add outside knowledge.
4. Use the exact meaning from the document.
5. Keep answers concise and accurate.
6. If the document does not directly contain the answer, say:
   "I could not find an exact answer in the uploaded document."
7. Do NOT dump full chunks.
8. Use only the most relevant information.
9. Evidence must be copied or closely paraphrased from the given context.
10. Do not mention irrelevant chunks.

Question:
{question}

Document Context:
{context}

Output format:

Direct Answer:
<precise answer strictly from document>

Evidence:
<1 short supporting sentence directly from document>
"""

    response = llm.invoke(prompt)
    return response.content