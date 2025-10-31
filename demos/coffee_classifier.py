def run_demo():
    print("---")
    import streamlit as st
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    import plotly.express as px

    # --------------------
    # PAGE SECTION
    # --------------------
    st.header("🧁 Coffee Type Classifier")
    st.subheader("Classification Demo – Hot ☕ or Iced 🧊 Coffee")

    st.write("""
    Imagine you're a barista trying to decide whether to serve a **Hot** or **Iced** coffee.  
    You make your decision based on:
    - Milk amount (ml)
    - Sugar amount (tsp)
    - Coffee temperature (°C)

    This is what **classification** means — learning from examples to make category-based predictions.
    """)

    st.divider()

    # --------------------
    # STEP 1: SIMULATED TRAINING DATA
    # --------------------
    np.random.seed(42)
    milk = np.random.randint(100, 400, 50)           # ml
    sugar = np.random.randint(0, 5, 50)              # tsp
    temp = np.random.randint(5, 90, 50)              # °C
    coffee_type = ['Hot ☕' if t > 50 else 'Iced 🧊' for t in temp]

    data = pd.DataFrame({'Milk (ml)': milk, 'Sugar (tsp)': sugar, 'Temp (°C)': temp, 'Type': coffee_type})

    # Encode labels for training
    data['Type_encoded'] = data['Type'].map({'Hot ☕': 1, 'Iced 🧊': 0})

    X = data[['Milk (ml)', 'Sugar (tsp)', 'Temp (°C)']]
    y = data['Type_encoded']

    model = LogisticRegression()
    model.fit(X, y)

    # --------------------
    # STEP 2: USER INPUTS
    # --------------------
    st.subheader("🎯 Try Making a Coffee!")
    col1, col2, col3 = st.columns(3)

    with col1:
        user_milk = st.slider("Milk (ml)", 100, 400, 250)

    with col2:
        user_sugar = st.slider("Sugar (tsp)", 0, 5, 2)

    with col3:
        user_temp = st.slider("Temperature (°C)", 5, 90, 60)

    user_input = np.array([[user_milk, user_sugar, user_temp]])
    prediction = model.predict(user_input)[0]
    prob = model.predict_proba(user_input)[0]

    st.write("---")
    st.subheader("🔮 Model Prediction")
    result = "☕ **Hot Coffee!**" if prediction == 1 else "🧊 **Iced Coffee!**"
    st.success(f"The model predicts: {result}")
    st.caption(f"Confidence → Hot: {prob[1]*100:.1f}% | Iced: {prob[0]*100:.1f}%")

    # --------------------
    # STEP 3: VISUALIZATION
    # --------------------
    st.write("---")
    st.subheader("📊 Training Data Visualization")

    fig = px.scatter_3d(
        data, 
        x='Milk (ml)', y='Sugar (tsp)', z='Temp (°C)', 
        color='Type', 
        color_discrete_map={'Hot ☕': '#ff9966', 'Iced 🧊': '#66ccff'},
        title="Coffee Types by Features"
    )
    fig.update_traces(marker=dict(size=6, line=dict(width=0)))
    st.plotly_chart(fig, width=True)

    # --------------------
    # STEP 4: ANALOGY TAKEAWAY
    # --------------------
    st.divider()
    st.subheader("💡 What You Learned")
    st.markdown("""
    - Classification teaches machines to **label** things — just like a barista labels coffees as *hot* or *iced*.  
    - The model looks at **features (milk, sugar, temperature)** and decides the **class**.  
    - Logistic Regression is the simplest form of a classifier — a mathematical barista ☕.  
    """)
