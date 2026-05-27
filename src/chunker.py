from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def create_chunks(text, filename):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    documents = []

    for index, chunk in enumerate(chunks):
        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "source": filename,
                    "chunk_id": index
                }
            )
        )

    return documents