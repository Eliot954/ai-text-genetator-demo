import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
import streamlit as st
from transformers import pipeline
st.title("AI文本生成小工具")
st.write("输入一段开头文字，我来帮你续写！")
st.cache_resource
def load_model():
    return pipeline('text-generation',model='distilgpt2')
generator = load_model()
prompt = st.text_input("输入你的开头文字: ",
                       value="Hello,I'm a sofware engineering student looking for summer internship in zhengzhou,")
max_length = st.slider("生成最大长度",30,150,60)
num_results = st.slider("生成几个版本",1,5,1)
if st.button("生成文本"):
    with st.spinner("AI 正在思考..."):
        results = generator(prompt,max_length=max_length,num_return_sequences=num_results)
        for i, res in enumerate(results):
            st.subheader(f"生成版本 {i+1}")
            st.write(res['generated_text'])
