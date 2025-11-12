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
st.subheader("Machine Learning & AI Developer | Full-Stack Engineer")
st.markdown(
    """
    I build intelligent, data-driven systems that solve real-world problems.  
    My mission: blending ML models with practical engineering for measurable impact.
    """
)

st.divider()

# --------------------
# ABOUT ME
# --------------------
st.header("🌱 About Me")
st.write(
    """
    I'm a certified Machine Learning and AI with a strong foundation in Python, 
    full-stack web development.  
    I focus on **creating ML solutions that are easy to use, interpret** — 
    bridging the gap between data and decision-making.

    - 💡 Currently learning advanced Deep Learning & ML deployment.
    - 🚀 Experienced in Python, Streamlit, TensorFlow, scikit-learn, and AngularJS.
    """
)

st.divider()

# --------------------
# TECHNICAL SKILLS
# --------------------
st.header("⚙️ Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Programming")
    st.write("- Python")
    st.write("- JavaScript (AngularJS)")
    st.write("- SQL, POSTgreSQl, DJango")

    st.subheader("Libraries & Tools")
    st.write("- Pandas, NumPy")
    st.write("- scikit-learn, TensorFlow, PyTorch")
    st.write("- Streamlit, Git, Matplotlib")

with col2:
    st.subheader("Concepts")
    st.write("- Supervised & Unsupervised Learning")
    st.write("- Neural Networks & Deep Learning")
    st.write("- Clustering & Feature Engineering")
    st.write("- Model Evaluation Metrics")

st.divider()

# --------------------
# PROJECTS SECTION
# --------------------
st.header("📂 Projects")

project_cols = st.columns(2)

with project_cols[0]:
    st.subheader("🏠 Resume Screening System")
    st.write(
        "A Streamlit-powered application that extracts skills, education, and experience from resumes, compares them with job descriptions, and computes a match score. Perfect for recruiters and hiring teams to quickly screen candidates."
    )
    st.markdown("[🔗 View on GitHub](https://github.com/krimatrivedi/resume-screening-system)")

with project_cols[1]:
    st.subheader("🧠 AI Meeting Summarizer")
    st.write(
        "A Streamlit-powered web app that automatically summarizes meeting transcripts and extracts actionable tasks using AI and NLP."
    )
    st.markdown("[🔗 View on GitHub](https://github.com/krimatrivedi/meeting-summarizer.git)")

project_cols2 = st.columns(2)

with project_cols2[0]:
    st.subheader("📊 Customer Churn Prediction – End-to-End ML Project")
    st.write(
        "Telecom companies lose millions every year due to customer churn (customers leaving the service). "
        "This project predicts whether a customer will churn based on demographic, account, and service details. "
        "By identifying who is at risk, businesses can take action (loyalty programs, discounts, better service) to reduce churn and save revenue."
    )
    st.markdown("[🔗 View on GitHub](https://github.com/krimatrivedi/customer-churn-prediction.git)")

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
    agentic_research_assistant
    # rag_chatbot
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
    if st.button("LLM API", key="llm_api"):
        st.session_state["active_demo"] = "llm_api"

with demo_cols1[1]:
    # st.image("https://via.placeholder.com/300x180.png?text=CNN+Demo", use_container_width=True)
    if st.button("Agentic AI", key="agentic_ai"):
        st.session_state["active_demo"] = "agentic_ai"

# with demo_cols1[1]:
#     # st.image("https://via.placeholder.com/300x180.png?text=CNN+Demo", use_container_width=True)
#     if st.button("RAG", key="rag_chatbot"):
#         st.session_state["active_demo"] = "rag_chatbot"

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
    # elif demo == "rag_chatbot":
    #     rag_chatbot.run_demo()
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
st.caption("© 2025 Krima Trivedi | Built with Streamlit")

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
