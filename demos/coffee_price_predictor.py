# inside demos/coffee_price_predictor.py
def run_demo():
    import streamlit as st
    import numpy as np
    from sklearn.linear_model import LinearRegression

    st.subheader("☕ Coffee Price Predictor — Regression Demo")
    st.write("Predict coffee prices using milk and sugar quantities ☕")

    milk = st.slider("Milk (ml)", 0, 500, 200)
    sugar = st.slider("Sugar (tsp)", 0, 10, 3)

    X = np.array([[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]])
    y = np.array([50, 100, 150, 200, 250])  # prices

    model = LinearRegression()
    model.fit(X, y)
    predicted_price = model.predict([[milk, sugar]])[0]

    st.success(f"Estimated Coffee Price: ₹{predicted_price:.2f}")
    st.caption("Just like adjusting milk & sugar changes flavor, ML features change predictions ☕")
