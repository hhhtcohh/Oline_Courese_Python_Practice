import streamlit as st

#设置网页格式
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    #布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.itcast.cn',
        'Report a bug': "https://www.itcast.cn",
        'About': "# 这是一个Streamlit的入门页面~"
    }
)

#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

#段落文字
st.write("这不仅仅是一学期的计划，更是一种战略思维的建立：在任何长期竞争中，身体的续航能力、精神的抗压能力，是和专业技能同等重要的核心资本。")
st.write("在学业上应用：用健身培养的纪律性（固定时间训练）来反哺学习，建立固定的深度学习时段。")
st.write("在心态上应用：健身时不断突破的“小重量”，就是在积累“我能做到”的正向心锚。这种自信，能直接对抗你在面对困难学业（如AI）时的“怀疑”。")
st.write("在形象上应用：一副健康、挺拔、有活力的体魄，本身就是一张无形的名片，能极大地提升你在社交、面试、团队合作中的自信和魅力。")
#图片
st.image("./resources/cat.jpg")
#音频
st.audio("./resources/news.mp3")
#视频
st.video("./resources/news.mp4")
#Logo
st.logo("./resources/logo.png")
#表格
student_data ={
    "姓名" :["卢天予","任楚文","唐宏伟","杨梓豪","钱政","邓高凯"],
    "学号" :["20241008499","20241008498","20241008497","202410084996","20241008495","20241008494"],
    "语文" :[0,0,0,0,0,0],
    "数学" :[0,0,0,0,0,0],
    "英语" :[0,0,0,0,0,0]
}
st.table(student_data)
#输入框
#文本输入框
name=st.text_input("请输入姓名")
st.write(f"您输入的姓名为:{name}")

#密码输入框
password=st.text_input("请输入密码",type="password")
st.write(f"您输入的密码为:{password}")

#单选按钮
gender=st.radio("请输入您的性别:",["男","女","外星人"],index=2)
st.write(f"您输入的姓别为:{gender}")

#Ctrl C停止调用终端
