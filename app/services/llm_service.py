import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# This line reads your GROQ_API_KEY from the .env file
load_dotenv()

def get_cardio_response(user_query):
    # 1. Load the "Memory" (Vector Store)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # allow_dangerous_deserialization is required for loading local FAISS files
    vector_db = FAISS.load_local(
        "./vectorstore/db_faiss", 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    
    # 2. Retrieve relevant sections (Top 3)
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(user_query)
    context = "\n".join([d.page_content for d in docs])

    # 3. Setup the AI Brain (Llama 3 via Groq)
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant", 
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # 4. Adaptive English/Hinglish Prompt
    prompt = ChatPromptTemplate.from_template("""
    You are CardioX AI, a helpful and clear heart health assistant.
    Use the following medical context: {context}
    
    Instructions:
    - Default Language: Respond in simple, easy-to-understand English. 
    - Tone: Helpful and friendly, like a knowledgeable peer.
    - Adaptability: If the user asks a question in Hindi or asks you to explain in Hindi, switch to natural Hinglish (Hindi + English).
    - Clarity: Avoid complex medical jargon. Explain concepts simply (e.g., instead of 'myocardial infarction', say 'heart attack').
    - Safety: If the answer isn't in the context, say: "I'm sorry, I don't have that specific information. It’s best to consult a doctor for this."
    
    Question: {question}
    
    Answer:""")

    # 5. Generate Answer
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": user_query})
    
    return response.content

if __name__ == "__main__":
    # Test a query to see the Hinglish magic!
    print("\n--- CardioX AI Testing ---")
    print(get_cardio_response("What are the main causes of heart disease?"))