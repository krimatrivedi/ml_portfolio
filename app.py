import streamlit as st

# --------------------
# PAGE CONFIG
# --------------------
st.set_page_config(
    page_title="Krima Trivedi | ML & AI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# --------------------
# HEADER
# --------------------
st.title("👩‍💻 Krima Trivedi")
st.subheader("AI Engineer | GenAI Engineer | Python Backend Developer")
st.markdown(
    """
    I build scalable backend systems and AI-powered applications using Python, FastAPI, and Large Language Models. 
    Experienced in production-ready GenAI workflows, multi-agent systems, and intelligent automation.
    """
)

st.divider()

# --------------------
# ABOUT ME
# --------------------
st.header("🌱 About Me")
st.write(
    """
    I am an **AI Engineer and Python Backend Developer** with **2.9 years of experience** building scalable backend systems and AI-powered applications. 
    I specialize in developing production-ready GenAI workflows, multi-agent systems, and Retrieval-Augmented Generation (RAG) pipelines.

    - 🚀 Experienced in **FastAPI, Django, PostgreSQL, and Pinecone**.
    - 💡 Focus on **Prompt Engineering, LLM orchestration, and NLP workflows**.
    - 🛠️ Passionate about bridging the gap between AI prototypes and production-grade engineering.
    """
)

st.divider()

# --------------------
# TECHNICAL SKILLS
# --------------------
st.header("⚙️ Technical Skills")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("💻 Backend")
    st.write("- Python, FastAPI, Django")
    st.write("- REST APIs, Microservices")
    st.write("- HTML5, CSS3, AngularJS")

with col2:
    st.subheader("🤖 AI & GenAI")
    st.write("- RAG, LLMs, AI Agents")
    st.write("- Multi-Agent Systems")
    st.write("- Prompt Engineering, NLP")

with col3:
    st.subheader("🗄️ Databases")
    st.write("- PostgreSQL, SQL")
    st.write("- Pinecone, Vector DBs")
    st.write("- Semantic Search")

with col4:
    st.subheader("🛠️ Tools")
    st.write("- Docker, Git")
    st.write("- Streamlit, Hugging Face")
    st.write("- OpenAI APIs")

st.divider()

# --------------------
# PROFESSIONAL EXPERIENCE
# --------------------
st.header("💼 Professional Experience")

with st.expander("🚀 Software Engineer | Current Organization", expanded=True):
    st.write("**Feb 2026 – Present**")
    st.write(
        """
        - Developed AI-powered backend services using Python, FastAPI, PostgreSQL, and Vector Databases.
        - Built Retrieval-Augmented Generation (RAG) pipelines that improved contextual response relevance.
        - Designed modular microservice architectures that accelerated feature integration.
        - Optimized backend APIs, reducing response latency and improving application performance.
        """
    )

with st.expander("💻 Full Stack Python Developer | Intellial Solution Pvt Ltd"):
    st.write("**May 2023 – Jan 2026**")
    st.write(
        """
        - Developed and maintained enterprise-grade web applications using Python, Django, and PostgreSQL.
        - Built scalable backend APIs and automation workflows that reduced repetitive manual operations.
        - Optimized database queries and backend logic, improving application responsiveness.
        - Supported integration of AI-powered retrieval workflows and intelligent backend features.
        """
    )

st.divider()

# --------------------
# PROJECTS SECTION
# --------------------
st.header("📂 Selected AI Projects")

project_cols = st.columns(2)

with project_cols[0]:
    st.subheader("🤖 AI Support Multi-Agent System")
    st.write(
        """
        Intelligent support system that classifies, routes, and responds to queries using AI-driven orchestration.
        - **Key Features:** Multi-agent workflow, AI ticket classification, automated response generation, and FastAPI backend.
        """
    )
    st.markdown("[🔗 View on GitHub](https://github.com/krimatrivedi/ai-support-multi-agent)")

with project_cols[1]:
    st.subheader("⚕️ AI Medical Scribe Demo")
    st.write(
        """
        Extracts structured medical information from doctor-patient conversations using NLP and LLM workflows.
        - **Key Features:** Symptom & diagnosis extraction, automated clinical note generation, and Streamlit integration.
        """
    )
    st.markdown("[🔗 View on GitHub](https://github.com/krimatrivedi/medical_scribe_demo)")

project_cols2 = st.columns(2)

with project_cols2[0]:
    st.subheader("📈 AI Business Analytics Platform")
    st.write(
        """
        Generates business insights and automated analytical summaries using AI-driven processing.
        - **Key Features:** Backend analytics services, AI-powered summarization, and PostgreSQL integration.
        """
    )
    st.markdown("[🔗 View on GitHub](https://github.com/krimatrivedi/ai-business-analytics)")

with project_cols2[1]:
    st.subheader("🏠 Resume Screening System")
    st.write(
        """
        Extracts skills and experience from resumes and computes match scores against job descriptions.
        - **Key Features:** PDF parsing, skill extraction, and real-time match scoring using NLP.
        """
    )
    st.markdown("[🔗 View on GitHub](https://github.com/krimatrivedi/resume-screening-system)")

st.divider()

# --------------------
# CURRENTLY BUILDING
# --------------------
# st.header("🧩 Currently Building")
# st.write(
#     """
#     - 👓 **AI-Powered Smart Reading Glasses** – detects text in real-time and reads aloud using OCR & speech synthesis.  
#     - 🏠 **Price Prediction Model** – predicting house prices using supervised ML (scikit-learn, regression models).  
#     - 🧩 **Interactive ML Demos** – experimenting with regression, classification, clustering, and CNN concepts for hands-on learning.
#     """
# )

# st.divider()

# --------------------
# INTERACTIVE DEMOS SECTION
# --------------------
st.header("🧩 Interactive ML & AI Demos")
st.info("Try small interactive demos that showcase ML & AI concepts (more coming soon!)")

from demos import (
    coffee_price_predictor,
    coffee_classifier,
    sweetness_clustering,
    neural_network_learner,
    cnn_coffee_classifier,
    llm_playground,
    agentic_research_assistant,
    rag_chatbot,
    # multi_processing
)

demo_cols = st.columns(5)
demo_cols1 = st.columns(5)

with demo_cols[0]:
    # st.image("https://via.placeholder.com/300x180.png?text=Regression+Demo", use_container_width=True)
    if st.button("Launch Regression Demo", key="regression_demo"):
        st.session_state["active_demo"] = "regression"

with demo_cols[1]:
    # st.image("https://via.placeholder.com/300x180.png?text=Classification+Demo", use_container_width=True)
    if st.button("Launch Classification Demo", key="classification_demo"):
        st.session_state["active_demo"] = "classification"

with demo_cols[2]:
    # st.image("https://via.placeholder.com/300x180.png?text=Clustering+Demo", use_container_width=True)
    if st.button("Launch Clustering Demo", key="clustering_demo"):
        st.session_state["active_demo"] = "clustering"

with demo_cols[3]:
    # st.image("https://via.placeholder.com/300x180.png?text=Neural+Network+Demo", use_container_width=True)
    if st.button("Launch Neural Network Demo", key="nn_demo"):
        st.session_state["active_demo"] = "neural_net"

with demo_cols[4]:
    # st.image("https://via.placeholder.com/300x180.png?text=CNN+Demo", use_container_width=True)
    if st.button("Launch CNN Demo", key="cnn_demo"):
        st.session_state["active_demo"] = "cnn"


with demo_cols1[0]:
    # st.image("https://via.placeholder.com/300x180.png?text=CNN+Demo", use_container_width=True)
    if st.button("LLM Playground", key="llm_api"):
        st.session_state["active_demo"] = "llm_api"

with demo_cols1[1]:
    # st.image("https://via.placeholder.com/300x180.png?text=CNN+Demo", use_container_width=True)
    if st.button("Agentic Scheduler", key="agentic_ai"):
        st.session_state["active_demo"] = "agentic_ai"

with demo_cols1[2]:
    # st.image("https://via.placeholder.com/300x180.png?text=CNN+Demo", use_container_width=True)
    if st.button("Resume RAG Chatbot", key="rag_chatbot"):
        st.session_state["active_demo"] = "rag_chatbot"

# with demo_cols1[3]:
#     # st.image("https://via.placeholder.com/300x180.png?text=CNN+Demo", use_container_width=True)
#     if st.button("Multi processing", key="multi_processing"):
#         st.session_state["active_demo"] = "multi_processing"

# Load selected demo dynamically (lazy loading)
if "active_demo" in st.session_state:
    demo = st.session_state["active_demo"]
    if demo == "regression":
        coffee_price_predictor.run_demo()
    elif demo == "classification":
        coffee_classifier.run_demo()
    elif demo == "clustering":
        sweetness_clustering.run_demo()
    elif demo == "neural_net":
        neural_network_learner.run_demo()
    elif demo == "cnn":
        cnn_coffee_classifier.run_demo()
    elif demo == "llm_api":
        llm_playground.run_demo()
    elif demo == "agentic_ai":
        agentic_research_assistant.run_demo()
    elif demo == "rag_chatbot":
        rag_chatbot.run_demo()
    # elif demo == "multi_processing":
    #     multi_processing.run_demo()
    # Close button
    if st.button("❌ Close Demo"):
        del st.session_state["active_demo"]
        st.rerun()

st.divider()

# --------------------
# WHY ME
# --------------------
st.header("🚀 Why Choose Me")
st.write(
    """
    ✅ I combine **AI intuition + engineering execution** — I not only build models but also make them deployable and explainable.  
    ✅ I understand **both code and communication** — turning complex ML ideas into clear business outcomes.  
    ✅ I value **clean, reliable, and scalable code** — ensuring solutions stay useful beyond experiments.
    """
)

st.divider()

# --------------------
# CERTIFICATIONS
# --------------------
st.header("🎓 Certifications")
st.write(
    """
    - **Google IT Automation with Python Professional Certificate** – [Google/Coursera]  
    - **Machine Learning** – [DeepLearning.AI/Coursera]  
    """
)

# --------------------
# RESUME DOWNLOAD
# --------------------
st.header("📄 Resume")
st.write("Download my latest resume below:")
try:
    with open("Krima_Trivedi_Resume.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Resume",
            data=file,
            file_name="Krima_Trivedi_Resume.pdf",
            mime="application/pdf",
        )
except FileNotFoundError:
    st.caption("_Upload your resume PDF in the same folder to enable this button._")

st.divider()

# --------------------
# CONTACT
# --------------------
st.header("📬 Contact")
st.write("💬 Always open to opportunities in AI, ML, and data-driven engineering roles.")
st.write("Let's build something impactful together!")

st.markdown(
    """
    <p style='font-size:13px; color:gray;'>
    If clicking on the email link doesn’t open your mail app,<br>
    you can also send me a message directly using the form below. 👇
    </p>
    """,
    unsafe_allow_html=True
)

# Direct contact info
st.write("📧 **Email:** [krimatrivedi1@gmail.com](mailto:krimatrivedi1@gmail.com)")
st.write("💼 [LinkedIn](https://www.linkedin.com/in/krimatrivedi)")
st.write("🐙 [GitHub](https://github.com/krimatrivedi)")
st.write("✍️ [Medium](https://medium.com/@krimatrivedi1)")

# Contact form
form_html = """
<form action="https://formsubmit.co/krimatrivedi1@gmail.com" method="POST" target="_blank">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" placeholder="Your Name *" required>
  <input type="email" name="email" placeholder="Your Email *" required>
  <textarea name="message" placeholder="Your Message..." rows="5" required></textarea>
  <button type="submit">Send Message 🚀</button>
</form>
"""
st.markdown(form_html, unsafe_allow_html=True)

# Styling
st.markdown("""
<style>
form {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
}
input, textarea {
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #ddd;
    margin-bottom: 12px;
    font-size: 16px;
}
button {
    background-color: #4B9CD3;
    color: white;
    padding: 10px 18px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
}
button:hover {
    background-color: #3c8ac1;
}
</style>
""", unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 Krima Trivedi | Built with Streamlit")

# --------------------
# CUSTOM STYLE
# --------------------
st.markdown(
    """
    <style>
    h1, h2, h3 {color: #2E2E2E;}
    section[data-testid="stSidebar"] {background-color: #f7f9fb;}
    .stButton>button {border-radius: 8px; padding: 0.5rem 1rem;}
    </style>
    """,
    unsafe_allow_html=True
)
