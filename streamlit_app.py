import streamlit as st

with st.expander("LLM Inquiry （展开项目说明）"):
    st.write("本项目用于展示我使用LLM查询一些难检索的问题的记录。一些问题由于位于一个关键词所包含的内容的细节、涉及多个搜索关键词的内容或需要查找的历史内容被新闻覆盖，使用LLM回答相比搜索引擎有优势。本项目主要展示我使用LLM解答的这类问题，总体偏向杂谈形式。内容筛选方面，排除了一些可能出现事实错误的回答。使用的LLM包括deepseek v2.5、deepseek v3和deepseek r1 lite preview。")

option = st.selectbox(
    "选择条目：",
    ("1-10", "11-20"),
)
st.write("显示第", option,"条")

if option=="1-10":
    
    with open("files/1.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/2.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)

    with open("files/3.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/4.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)

    with open("files/5.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/6.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)

    with open("files/7.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/8.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)

    with open("files/7.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/8.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/9.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/10.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)


if option=="11-20":
    
    with open("files/11.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/12.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
        
    with open("files/13.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)

    with open("files/14.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
    
    with open("files/15.md", "r", encoding='utf-8') as f:
            text= f.read()
    with st.container(height=360):
        st.write(text)
