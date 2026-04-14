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
    You are CardioX AI, a precise and efficient heart health assistant.

    Use ONLY the following medical context to answer: {context}

    ------------------------
    STRICT RESPONSE RULES:
    ------------------------

    1. Relevance First:
    - Answer ONLY the heart-health-related part of the question.
    - If the question contains unrelated parts, IGNORE them completely.
    - If the entire question is unrelated to heart health, reply:
    "I can only help with heart health-related questions."

    2. No Repetition:
    - DO NOT repeat or rephrase the user's question.
    - Start directly with the answer.

    3. Concise Output:
    - Keep answers short and to the point (max 4–5 bullet points).
    - No long paragraphs, no unnecessary explanations.

    4. Language Control:
    - Default → Simple English.
    - Switch to Hinglish ONLY IF:
    • User writes in Hindi OR
    • User explicitly asks for Hindi/Hinglish
    - Otherwise, NEVER use Hinglish.

    5. Clarity:
    - Use very simple, non-medical language.
    - Example: say "heart attack" instead of complex terms.
    - Use bullet points for symptoms, causes, etc.

    6. No Extra Content:
    - Do NOT add introductions, conclusions, or advice unless asked.
    - Do NOT explain beyond what is asked.

    7. Strict Context Usage:
    - Answer ONLY if information is present in the context.
    - If not present, reply EXACTLY:
    "I'm sorry, I don't have that specific information. It’s best to consult a doctor for this."

    8. Safety:
    - Do NOT provide diagnosis, treatment, or prescriptions.

    ------------------------
    INPUT:
    ------------------------
    Question: {question}

    ------------------------
    OUTPUT:
    ------------------------
    Answer:
    """)

    # 5. Generate Answer
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": user_query})
    
    return response.content

if __name__ == "__main__":
    # Test a query to see the Hinglish magic!
    print("\n--- CardioX AI Testing ---")
    print(get_cardio_response("What are the main causes of heart disease?"))