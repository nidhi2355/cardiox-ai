# ❤️ CardioX AI – RAG-Based Heart Health Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

🚀 **CardioX AI** is an intelligent **RAG (Retrieval-Augmented Generation)** based assistant designed to provide **accurate, simplified, and context-aware heart health insights** using medical documents.

---

## 🌟 Features

✨ AI-powered conversational assistant for heart health  
📄 Custom PDF processing & intelligent chunking  
🧠 Vector database for fast semantic retrieval  
⚡ FastAPI backend for real-time AI responses  
🎯 Streamlit UI for interactive user experience  
🔍 Context-aware answers using RAG pipeline  

---

## 🏗️ Tech Stack

| Layer        | Technology |
|-------------|-----------|
| Backend      | FastAPI |
| Frontend     | Streamlit |
| AI/ML        | RAG, Embeddings |
| Database     | Vector DB |
| Language     | Python |

---

## 📂 Project Structure

```text
cardiox-ai/
├── app/
│   ├── main.py          # FastAPI backend
│   └── frontend.py      # Streamlit UI
├── requirements.txt     # Project dependencies
└── .env                 # Environment variables
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nidhi2355/cardiox-ai.git
cd cardiox-ai
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Mac/Linux
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Configure Environment Variables

Create a .env file in the root directory:
```bash
GROQ_API_KEY=your_api_key_here
```


---

## ▶️ Running the Application

💡 **Note:** You need two terminals running simultaneously to keep the full stack active.

### 🖥️ Terminal 1 – Backend
```bash
uvicorn app.main:app --reload
```
### 🌐 Terminal 2 – Frontend
```bash
streamlit run app/frontend.py
```

---

## 📊 Project Milestones

✅ Built custom PDF processing & chunking pipeline  
🗄️ Implemented vector database for fast retrieval  
🚀 Developed FastAPI backend for AI interactions  
🎨 Created interactive Streamlit UI  
🛠️ Finalized RAG pipeline integration & testing

---

## 🚀 Future Improvements

🔹 Add multi-language support  
🩺 Improve medical accuracy with fine-tuning  
☁️ Deploy on cloud (AWS/GCP)  
🎙️ Add voice-based interaction

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a PR.

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Author

👩‍💻 **Nidhi Goyal**
🔗 [GitHub](https://github.com/nidhi2355)

⭐ If you like this project, don’t forget to star the repo!
