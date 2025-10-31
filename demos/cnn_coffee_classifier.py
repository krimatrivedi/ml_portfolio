import streamlit as st
from PIL import Image
import torch
from torchvision import models, transforms
import json
import requests

@st.cache_resource
def load_model():
    model = models.resnet50(weights="IMAGENET1K_V2")  # pretrained, proven model
    model.eval()
    return model

@st.cache_resource
def load_labels():
    url = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
    labels = requests.get(url).json()
    return labels

def run_demo():
    st.header("🕵️ Image Detective — Pretrained AI Classifier")
    st.write("""
    Upload an image and watch how a pretrained **ResNet50** model (trained on ImageNet)
    acts like a **detective**, examining clues (edges, colors, shapes) to identify what’s inside.
    """)

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Your uploaded image", use_container_width=True)

        # preprocess
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(image).unsqueeze(0)

        model = load_model()
        labels = load_labels()

        with torch.no_grad():
            outputs = model(input_tensor)
            probs = torch.nn.functional.softmax(outputs[0], dim=0)

        top_prob, top_catid = torch.topk(probs, 3)
        st.subheader("🔍 AI’s Best Guesses:")
        for i in range(3):
            st.write(f"{i+1}. {labels[top_catid[i]]} ({top_prob[i]*100:.1f}%)")

        st.caption("""
        **Analogy:**  
        Imagine the AI as a **detective** in a gallery full of objects.  
        - It first notices shapes (the outline of a suspect 🎩).  
        - Then colors and textures (is it furry or metallic?).  
        - Finally, it compares clues with its “case files” of 1,000 objects.  
        When the evidence matches, it declares its best guess — just like a seasoned detective!
        """)
