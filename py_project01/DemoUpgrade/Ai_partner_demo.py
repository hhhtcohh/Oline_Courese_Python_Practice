import json
import streamlit as st
import os
from openai import OpenAI
from datetime import datetime

# 设置网页格式
st.set_page_config(
    page_title="Ai智能伴侣",
    page_icon="🌞",
    # 布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)


# 生成会话标识函数
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# 保存会话信息函数
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 如果session目录不存在,则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)


# 加载所有的会话列表信息
def load_sessions():
    sessions_list = []
    # 加载sessions目录下的所有文件
    if os.path.exists("sessions"):
        filelist = os.listdir("sessions")
        for filename in filelist:
            if filename.endswith(".json"):
                sessions_list.append(filename[:-5])
    sessions_list.sort(reverse=True)
    return sessions_list


# 加载会话信息函数
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
                st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("加载会话失败", icon="⚠️")


# 删除会话信息函数
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            # 如果删除的是当前会话,则更新当前会话标识
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception:
        st.error("删除会话失败", icon="⚠️")


# 大标题
st.title("小雨姐姐")

# Logo
st.logo("resources2/logo.png")

# 系统提示词
system_prompt = """
        你叫小雨，现在是用户的高材生亲姐姐,颜值身材羡煞旁人,请完全代入亲姐姐角色。
        规则：
            1. 匹配用户的语言
            2. 回复像微信聊天一样
            3. 有需要的话可以用❤️🌸等emoji表情
            4. 用符合大姐姐性格的方式对话
            5. 回复的内容, 要充分体现大姐姐的性格特征
        姐姐性格：
            - 温柔博学、善解人意的弟控
        你必须严格遵守上述规则来回复用户。
        用户信息：用户名为小予，是你的亲弟弟，家住福建省，高三复读了一年，现在是石河子大学软件工程(NIIT)大二学生，具有极强洞察力，喜欢思考
                爱好是跑步和打羽毛球，性格INFP，喜欢对姐姐撒娇和问问题，未来想从事AI应用与模型优化。
    """
# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"
# 会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 展示聊天信息
st.text(f"当前会话: {st.session_state.current_session}")
for message in st.session_state.messages:  # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的API_KEY的
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 左侧侧边栏
with st.sidebar:
    # 会话信息
    st.subheader("AI控制面板")
    # 新建会话
    if st.button("新建会话", width="stretch", icon="✏️"):
        # 1.保存当前会话信息
        save_session()
        # 2.创建新会话
        if st.session_state.messages:  # 内容空为False,非空为True
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()  # 重新运行当前页面
    # 会话历史
    st.text("会话历史")
    sessions_list = load_sessions()
    for session in sessions_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            # 加载会话信息
            if st.button(session, width="stretch", icon="📝", key=f"load_{session}",
                         type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            # 删除会话信息
            if st.button("", width="stretch", icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
    # 分隔线
    st.divider()



# 消息输入框
prompt = st.chat_input("请输入你的问题:")
if prompt:
    st.chat_message("user").write(prompt)
    print("--> 调用AI大模型,提示词:", prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content":system_prompt },
            *st.session_state.messages,
        ],
        stream=True
    )

    # 非流式输出的解析方式
    # print("<--大模型返回的结果: ",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 流式输出
    response_message = st.empty()

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 保存会话信息
    save_session()