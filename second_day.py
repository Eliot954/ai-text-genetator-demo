import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from transformers import pipeline
print("开始加载模型...")
generator = pipeline('text-generation',model='distilgpt2')
prompt1 = "HELLO,I'm learning AI in Hong Kong, and I want to"
result1 = generator(prompt1, max_length=60, num_return_sequences=1)
print("\n英文生成结果:")
print(result1[0]['generated_text'])
prompt2 = "我未来想找一份工作"
result2 = generator(prompt2, max_length=60, num_return_sequences=1)
print("\n中文生成结果:")
print(result2[0]['generated_text'])
prompt3 = "Write a simple Python function to calculate factorial:"
result3 = generator(prompt3, max_length=100, num_return_sequences=1)
print("\n生成代码示例:")
print(result3[0]['generated_text'])