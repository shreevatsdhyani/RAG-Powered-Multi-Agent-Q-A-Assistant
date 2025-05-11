
# 🤖 RAG-Powered Multi-Agent Q&A Assistant

This project is a simple yet powerful **Retrieval-Augmented Generation (RAG)**-based Question Answering Assistant with **agentic workflow**, built using **Streamlit**, **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Groq LLM**.

---

## 🎯 Objective

- Retrieve relevant info from a small document collection (RAG)
- Generate answers using an LLM
- Use a basic **agent workflow** to route queries intelligently

---

## 📦 Features

✅ RAG pipeline (FAISS + HuggingFace embeddings)  
✅ LLM integration via **Groq** (using LLaMA3 8B)  
✅ Agent decision logic for:
- **"calculate"** ➜ Calculator
- **"define ..."** ➜ Dictionary stub
- Otherwise ➜ RAG-based Answer  
✅ Streamlit UI with:
- Agent decision log  
- Retrieved context  
- Final answer display

---

## 🗂️ Project Structure

```

📁 project-root/
├── data/               # Folder with 3–5 .txt documents
├── main.py             # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .env                # Contains GROQ\_API\_KEY
├── .gitignore
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv ragvenv
ragvenv\Scripts\activate      # On Windows
# source ragvenv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your GROQ API Key

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free key from: [https://console.groq.com/keys](https://console.groq.com/keys)

---

## 🚀 Run the App

```bash
streamlit run main.py
```

Then open the URL shown in your terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## 🧠 Agent Workflow Logic

The assistant routes queries as follows:

| Query Type           | Action Taken                |
| -------------------- | --------------------------- |
| `"calculate"`        | Uses Python `eval()` safely |
| `"define something"` | Returns mock dictionary def |
| Other queries        | Runs through RAG → Groq LLM |

All decisions are **logged and displayed** in the Streamlit app.

---

## 🧪 Example Use Cases

* “What are the features of our product?”
* “Calculate 12 \* 18”
* “Define artificial intelligence”
* “How does the warranty work?”

---

## 🛠 Built With

* [LangChain](https://www.langchain.com/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Groq LLM](https://console.groq.com/)
* [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
* [Streamlit](https://streamlit.io/)
