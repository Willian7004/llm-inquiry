llm-inquiry

本项目用于展示我使用LLM查询一些难检索的问题的记录。一些问题由于位于一个关键词所包含的内容的细节、涉及多个搜索关键词的内容或需要查找的历史内容被新闻覆盖，使用LLM回答相比搜索引擎有优势。本项目主要展示我使用LLM解答的这类问题，总体偏向杂谈形式。内容筛选方面，排除了一些可能出现事实错误的回答。使用的LLM包括deepseek v2.5、deepseek v3和deepseek r1 lite preview。
本项目逻辑部分使用LLM辅助生成，对话记录位于streamlit_app.txt
本项目已在Streamlit Cloud部署，域名为https://william7004-llm-inquiry.streamlit.app

本地部署流程

建议使用Python=3.10环境

1.安装依赖
pip install -r requirements.txt

2.运行应用

streamlit run streamlit_app.py