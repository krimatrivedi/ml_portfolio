def run_demo():
    import streamlit as st
    import torch
    import torch.nn as nn
    import torch.optim as optim
    import matplotlib.pyplot as plt
    import numpy as np

    # --------------------
    # PAGE CONFIG
    # --------------------
    st.header("🤖 Neural Network Learner")
    st.subheader("Barista improving coffee with feedback ☕")

    st.write("""
    In this analogy, our **neural network is a barista** learning how much milk 🥛 and sugar 🍬 to add 
    to make coffee that matches a customer's taste (perfect satisfaction = 1).  
    Each training round (epoch) is like the barista trying again, tasting, and adjusting.  
    """)

    # --------------------
    # USER INPUTS
    # --------------------
    st.sidebar.header("Your Coffee Preferences")
    milk = st.sidebar.slider("Preferred milk level (0–1)", 0.0, 1.0, 0.7)
    sugar = st.sidebar.slider("Preferred sugar level (0–1)", 0.0, 1.0, 0.4)
    epochs = st.sidebar.slider("Number of training rounds (epochs)", 10, 300, 100)

    # --------------------
    # DATA (Coffee taste examples)
    # --------------------
    X = torch.tensor([[0.2,0.1],[0.9,0.8],[0.5,0.6],[0.7,0.3]], dtype=torch.float32)
    y = torch.tensor([[0.3],[0.95],[0.7],[0.65]], dtype=torch.float32)

    # --------------------
    # MODEL
    # --------------------
    model = nn.Sequential(
        nn.Linear(2, 4),
        nn.ReLU(),
        nn.Linear(4, 1)
    )

    loss_fn = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.05)

    losses = []

    # --------------------
    # TRAINING (Barista improving)
    # --------------------
    for epoch in range(epochs):
        y_pred = model(X)
        loss = loss_fn(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        losses.append(loss.item())

    # --------------------
    # VISUALIZE LEARNING
    # --------------------
    fig, ax = plt.subplots(figsize=(6,3))
    ax.plot(losses)
    ax.set_xlabel("Training Round (Epoch)")
    ax.set_ylabel("Taste Error (Loss)")
    ax.set_title("Barista Learning Curve")
    st.pyplot(fig)

    # --------------------
    # PREDICTION
    # --------------------
    user_input = torch.tensor([[milk, sugar]], dtype=torch.float32)
    predicted_taste = model(user_input).item()

    st.success(f"Predicted Coffee Satisfaction ☕: **{predicted_taste:.2f} / 1.00**")

    # Interpretation
    if predicted_taste > 0.9:
        st.write("✅ The barista nailed it! Perfect coffee balance.")
    elif predicted_taste > 0.6:
        st.write("🙂 Pretty good! The barista is getting close.")
    else:
        st.write("😅 Needs more training — too bitter or too sweet.")

    st.markdown("---")
    st.caption("Concept: Each training round = barista tasting and adjusting recipe (backpropagation).")
