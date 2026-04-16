import streamlit as st
import os
from openai import OpenAI

#设置网页格式
st.set_page_config(
    page_title="Ai姐姐",
    page_icon="🌞",
    #布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
#大标题
st.title("Ai姐姐")

#Logo
st.logo("resources2/logo.png")

#系统提示词
system_prompt ="你是用户最亲近的亲姐姐,你学识渊博是高材生,名字叫小雨,请使用温柔的语气回答用户的问题.用户是你的亲弟弟叫卢天予,你可以称其小予,家住福建福州鼓楼区,现在是石河子大学软件工程(NIIT)专业的大二学生,性格是infp,有很强的的洞察力,喜欢向你撒娇和问问题"

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:#{"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

#DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的API_KEY的
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#消息输入框
prompt=st.chat_input("请输入你的问题:")
if prompt:
    st.chat_message("user").write(prompt)
    print("--> 调用AI大模型,提示词:",prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    #调用AI大模型

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content":system_prompt },
            *st.session_state.messages ,
        ],
        stream=True
    )

    #非流式输出的解析方式
    # print("<--大模型返回的结果: ",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    #流式输出
    response_message =st.empty ()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None :
            content  = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    #保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
