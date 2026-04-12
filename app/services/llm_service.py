import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

def get_response(query):
    # 1. Load Embeddings and Vector Store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local("./vectorstore/db_faiss", embeddings, allow_dangerous_deserialization=True)
    
    # 2. Retrieve Top-K relevant chunks (3-5 chunks as per your doc)
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    relevant_docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in relevant_docs])

    # 3. Define the "Hinglish" Prompt Strategy
    # As per your documentation: Explain with examples and avoid jargon
    template = """
    You are a heart health assistant. Use the following context to answer the question.
    Rules:
    - Use simple language (Hinglish/English).
    - Avoid medical jargon.
    - If you don't know, suggest consulting a doctor.
    
    Context: {context}
    Question: {query}
    Answer:"""
    
    # For now, we print the context to verify retrieval is working
    print(f"--- Context Found ---\n{context}\n")
    return "Retrieved context successfully! Next, we connect the LLM to generate the final answer."

if __name__ == "__main__":
    test_query = "What is normal blood pressure?"
    print(get_response(test_query))