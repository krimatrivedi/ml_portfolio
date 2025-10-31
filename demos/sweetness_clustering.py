def run_demo():
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans
    import plotly.express as px

    # --------------------
    # PAGE CONFIG
    # --------------------
    st.set_page_config(
        page_title="🍫 Sweetness Clustering | Krima Trivedi",
        page_icon="🍫",
        layout="centered"
    )

    # --------------------
    # HEADER
    # --------------------
    st.title("🍫 Sweetness Clustering")
    st.subheader("Unsupervised Learning Analogy – Grouping Chocolates by Sweetness & Cocoa")

    st.markdown(
        """
        Imagine you're a chocolatier 🍫 trying to understand your chocolate collection.  
        You record how **sweet** (sugar %) and **bitter** (cocoa %) each chocolate is.  
        But you don't label them manually.  
        Instead, you ask the machine to **discover natural groups**.  
        That's what clustering does — it finds patterns without supervision!
        """
    )

    st.divider()

    # --------------------
    # USER INPUTS
    # --------------------
    st.sidebar.header("⚙️ Experiment Settings")

    n_samples = st.sidebar.slider("Number of Chocolates", 10, 300, 100)
    n_clusters = st.sidebar.slider("Number of Flavor Groups (Clusters)", 2, 6, 3, step=1)
    random_state = st.sidebar.slider("Randomness (Seed)", 0, 50, 42)

    st.sidebar.markdown("👉 Adjust sliders and watch chocolates group themselves!")

    # --------------------
    # DATA GENERATION
    # --------------------
    np.random.seed(random_state)

    # Simulated chocolate data
    sugar = np.random.uniform(10, 90, n_samples)      # sweetness %
    cocoa = np.random.uniform(10, 90, n_samples)      # bitterness %

    data = pd.DataFrame({
        "Sugar (%)": sugar,
        "Cocoa (%)": cocoa
    })

    # --------------------
    # CLUSTERING
    # --------------------
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init="auto")
    data["Cluster"] = model.fit_predict(data[["Sugar (%)", "Cocoa (%)"]])

    # --------------------
    # VISUALIZATION
    # --------------------
    fig = px.scatter(
        data,
        x="Sugar (%)",
        y="Cocoa (%)",
        color=data["Cluster"].astype(str),
        color_discrete_sequence=px.colors.qualitative.Vivid,
        title="🍬 Chocolate Clusters based on Sweetness vs Cocoa Levels",
        labels={"color": "Cluster"},
        width=800,
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    # --------------------
    # CLUSTER INSIGHTS
    # --------------------
    st.markdown("### 🔍 What You Learned")
    st.write(
        f"""
        - The machine grouped {n_samples} chocolates into **{n_clusters} flavor families**  
        - Each cluster represents a unique **balance of sweetness and bitterness**  
        - No human told the algorithm what “milk” or “dark” chocolate is —  
        it **discovered** these patterns on its own 🧠  
        """
    )

    st.info("Try changing the number of clusters or chocolates to see how the groupings change!")

    # --------------------
    # FOOTER
    # --------------------
    st.markdown("---")
    st.caption("© 2025 Krima Trivedi | Unsupervised Learning Demo | Built with Streamlit")
