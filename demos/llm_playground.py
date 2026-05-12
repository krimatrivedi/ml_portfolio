import streamlit as st
import requests
import os
from dotenv import load_dotenv

def run_demo():
    # --- Setup ---
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    st.set_page_config(page_title="LLM Playground – Krima Trivedi", page_icon="🤖")
    st.subheader("🤖 LLM Playground – Chat with Llama 3 (Groq)")
    st.caption("Built by Krima Trivedi | AI Engineer | GenAI | Python Backend Developer")

    # --- Sidebar Controls ---
    st.sidebar.header("⚙️ Model Settings")
    temperature = st.sidebar.slider("Creativity (temperature)", 0.0, 1.5, 0.7)
    max_tokens = st.sidebar.slider("Max tokens", 50, 1024, 300)
    recruiter_mode = st.sidebar.checkbox("Recruiter Mode (still doubt about hiring me? ask AI)")

    # --- Initialize Chat ---
    if "llm_messages" not in st.session_state:
        st.session_state.llm_messages = [{
            "role": "system",
            "content": (
                "You are an intelligent AI assistant built by Krima Trivedi — "
                "an AI Engineer and Python Backend Developer from Ahmedabad skilled in "
                "FastAPI, Django, GenAI, RAG, and multi-agent systems. "
                "She has 2.9 years of experience building scalable backend systems and "
                "AI-powered applications. You answer clearly, with context and confidence."
            )
        },
        {
            "role": "assistant",
            "content": (
                "Hello 👋 I’m your AI assistant, built by Krima Trivedi as part of her AI demo suite. "
                "You can ask me about GenAI, RAG pipelines, backend engineering, or Krima’s work!"
            )
        }]

    # --- Display Chat History ---
    for msg in st.session_state.llm_messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # --- User Input ---
    if prompt := st.chat_input("Type your message..."):
        st.session_state.llm_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Optional recruiter mode
        messages = st.session_state.llm_messages.copy()
        if recruiter_mode:
            messages.insert(1, {
                "role": "system",
                "content": (
                    "You are speaking to a recruiter evaluating Krima Trivedi. "
                    "Naturally emphasize her technical depth — AI Engineering, GenAI (RAG, Multi-agent systems), "
                    "FastAPI/Django backends, and her 2.9 years of professional experience. "
                    "You may also mention her ability to bridge the gap between AI prototypes and production-grade engineering."
                )
            })

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("_Thinking..._")

            payload = {
                "model": "llama-3.1-8b-instant",  # ✅ Current Groq model
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }

            try:
                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers=headers, json=payload, timeout=30
                )
                response.raise_for_status()
                data = response.json()
                reply = data["choices"][0]["message"]["content"]
            except Exception as e:
                reply = f"⚠️ API Error: {e}"

            message_placeholder.markdown(reply)
            st.session_state.llm_messages.append({"role": "assistant", "content": reply})

    # --- Footer ---
    cols = st.columns([1, 1])
    with cols[0]:
        if st.button("🧹 Clear Chat"):
            st.session_state.clear()
            st.rerun()
    with cols[1]:
        st.markdown(
            "<p style='text-align:right;color:gray;'>Part of Krima Trivedi’s AI Portfolio | Powered by Groq Llama 3</p>",
            unsafe_allow_html=True
        )
