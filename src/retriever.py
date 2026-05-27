from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

CHROMA_PATH = "chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_vector_db():
    return Chroma(
        collection_name="doc_chat",
        embedding_function=embedding_model,
        persist_directory=CHROMA_PATH
    )

def index_documents(documents):
    vector_db = get_vector_db()
    vector_db.add_documents(documents)
    return len(documents)

def retrieve_documents(question, k=4):
    vector_db = get_vector_db()
    results = vector_db.similarity_search(question, k=k)
    return results