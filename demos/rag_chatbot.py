import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.prompts import PromptTemplate
import os
import time
from dotenv import load_dotenv

def run_demo():

    st.set_page_config(page_title="Ask My Resume", page_icon="📄")
    st.title("📄 Ask My Resume – RAG Chatbot")

    # ------------------------------
    # RATE LIMIT CONFIGURATION
    # ------------------------------
    MAX_REQUESTS = 2
    WINDOW_SECONDS = 60

    if "request_times" not in st.session_state:
        st.session_state.request_times = []

    # ------------------------------
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        with open("resume.pdf", "wb") as f:
            f.write(uploaded_file.read())

        loader = PyPDFLoader("resume.pdf")
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=80)
        docs = splitter.split_documents(pages)

        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        db = FAISS.from_documents(docs, embeddings)
        retriever = db.as_retriever(search_kwargs={"k": 3})

        load_dotenv()
        groq_api_key = os.getenv("GROQ_API_KEY")
        llm = ChatGroq(api_key=groq_api_key, model="llama-3.1-8b-instant")

        prompt = PromptTemplate(
            input_variables=["context", "input"],
            template="""
        You are a helpful assistant. Use ONLY the following documents to answer the question.
        If the answer is not in the documents, say: 'This information is not present in the resume.' 

        Documents:
        {context}

        Question: {input}
        """
        )

        combine_docs_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

        st.success("RAG is ready! Ask anything about your resume ⤵️")

        # ------------------------------
        # USER QUERY INPUT
        # ------------------------------
        query = st.text_input("Your question:")

        if query:

            # ------------------------------
            # CLEAN OLD TIMESTAMPS
            # ------------------------------
            current_time = time.time()
            st.session_state.request_times = [
                t for t in st.session_state.request_times
                if current_time - t < WINDOW_SECONDS
            ]

            # ------------------------------
            # CHECK RATE LIMIT
            # ------------------------------
            if len(st.session_state.request_times) >= MAX_REQUESTS:

                # Calculate cooldown remaining
                oldest_request = min(st.session_state.request_times)
                seconds_left = int(WINDOW_SECONDS - (current_time - oldest_request))

                st.error(f"⛔ Too many requests! Try again in {seconds_left} seconds.")
                return

            # ------------------------------
            # PROCESS USER QUERY
            # ------------------------------
            st.session_state.request_times.append(current_time)

            with st.spinner("Thinking..."):
                result = rag_chain.invoke({"input": query})

                st.chat_message("user").write(query)
                st.chat_message("assistant").write(result["answer"])
