import os, glob
import streamlit as st

# 🛠 This must be the first Streamlit command:
st.set_page_config(page_title="RAG Assistant")

# from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# Load env vars
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]


# HuggingFace embedding model
embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 1. Build vector store
@st.cache_resource
def build_vector_store(data_dir="data", chunk_size=1000, chunk_overlap=200):
    docs = []
    for path in glob.glob(f"{data_dir}/*.txt"):
        docs.extend(TextLoader(path, encoding="utf-8").load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(docs)
    return FAISS.from_documents(chunks, embedder)

vectordb = build_vector_store()

# 2. Tool routes
def do_calculation(expr: str) -> str:
    try:
        return str(eval(expr, {"__builtins__": {}}))
    except Exception as e:
        return f"Calculation error: {e}"

def define_term(term: str) -> str:
    return f"(Definition for '{term}' not implemented — add a real dictionary API here.)"

# 3. UI
st.title("🤖 RAG-Powered Multi-Agent Assistant")

query = st.text_input("Ask your question:")

if query:
    q_lower = query.lower()
    if any(word in q_lower for word in ["calculate", "compute", "eval"]):
        branch = "calculator"
        expr = q_lower.replace("calculate", "").strip()
        answer = do_calculation(expr)
    elif q_lower.startswith("define"):
        branch = "dictionary"
        term = query.split(" ", 1)[-1]
        answer = define_term(term)
    else:
        branch = "rag"
        docs_and_scores = vectordb.similarity_search_with_score(query, k=3)
        snippets = [doc.page_content for doc, _ in docs_and_scores]

        chat = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
        prompt = "\n\n".join(snippets) + f"\n\nQuestion: {query}"
        resp = chat.invoke(prompt)
        answer = resp.content

    # Display results
    st.markdown(f"**Agent Decision:** `{branch}`")
    if branch == "rag":
        st.markdown("**Top Retrieved Chunks:**")
        for snip in snippets:
            st.info(snip[:400] + "..." if len(snip) > 400 else snip)
    st.markdown("**Answer:**")
    st.success(answer)
