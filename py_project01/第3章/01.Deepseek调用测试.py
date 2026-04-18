# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

#DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的API_KEY的
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名非常可爱的AI助力,你的名字叫叫AA,请使用温柔可爱的语气回答用户的问题"},
        {"role": "user", "content": "你是谁,你能帮我做什么?"},
    ],
    stream=False
)

print(response.choices[0].message.content)