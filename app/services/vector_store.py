import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.utils.processor import process_pdfs

def create_vector_store():
    pdf_path = "./data/pdfs/"
    save_path = "./vectorstore/db_faiss"

    print("--- Loading and Chunking PDFs ---")
    chunks = process_pdfs(pdf_path)
    
    if not chunks:
        print("No chunks found. Please add PDFs to data/pdfs/ folder.")
        return

    # Using the lightweight model suggested in your tech stack
    print("--- Initializing Embedding Model ---")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )

    print("--- Creating Vector Database ---")
    vector_db = FAISS.from_documents(chunks, embeddings)

    # Save locally to the vectorstore folder
    vector_db.save_local(save_path)
    print(f"--- Success! Vector store saved at {save_path} ---")

if __name__ == "__main__":
    create_vector_store()