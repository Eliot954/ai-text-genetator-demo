import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
prompt = "Hello, I'm a language model in Shanghai, and I want to"
result = generator(prompt, max_length=50, num_return_sequences=1)
print("生成的文本：")
print(result[0]['generated_text'])