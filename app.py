import streamlit as st
from PIL import Image
from text import * 
from extractor import *
import json
from generateSummary import *

st.title("Image Processor")

tb1, tb2, tb4 = st.tabs(["Text Extractor", "Background remover", "Summarize Image"])


with tb1:
    st.header("Text Extractor")
    uploaded_file = st.file_uploader("Upload your image with text", type=["jpg", "png","jpeg"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_path = f"./{file_name}"
        with open(file_path, "wb") as fle:
            fle.write(uploaded_file.getbuffer())
        
        c1, c2 = st.columns(2)
        with c1:
            st.image(file_path, caption="Uploaded imawge")
        with c2:
            st.subheader("Extracted text")
            result = ocr_space_file(file_path)
            response = json.loads(result)
            if response:
                parsed_text = response['ParsedResults'][0]['ParsedText']
                lines = parsed_text.split("\r\n")
                complete_text = "\n".join(lines)
                if complete_text!="":
                    st.text_area("Extracted text", complete_text, height=400)
                else:
                    st.write("No text found in the image")
        st.subheader("Summarization of the extracted text")
        res = generate(complete_text)
        st.write(res)
            

with tb2:
    st.header("Remove Background from Image")
    img = st.file_uploader("Upload your image file here", type=["jpg", "png", "jpeg"])
    
    if img:
        image_name = img.name
        save_path = f"./{image_name}"
        with open(save_path, "wb") as f:
            f.write(img.getbuffer())
        col1, col2 = st.columns(2)
        with col1:
            st.image(save_path, caption="Uploaded Image")

        
        result = remove_bg(save_path)
        
        if "Error" not in result:
            with col2:
                    st.image(result, caption="Processed Image (No Background)")
            with open(result, "rb") as f:
                st.download_button("Downlod Processed Imaeg", data=f, file_name=f"{result}-processed.png")
                    
        else:
            with col2:
                st.error(result)

# with tb3:
#     st.header("AI Image generator through text")
#     prompt = st.text_input("Enter your prompt", placeholder="ai will gen this")
#     if prompt:
#         result = generate(prompt)
#         st.write(result) 

with tb4:
    st.header("Image summarization using Gemini")
    image = st.file_uploader("Upload your image file here", type=["jpg", "png"])
    if image:
        image_name = image.name
        save_path = f"./{image_name}"
        with open(save_path, "wb") as f:
            f.write(image.getbuffer())
        st.image(save_path, caption="Uploaded image")
        opened = Image.open(save_path)
        response = generate(opened)
        st.write(response)
    
        