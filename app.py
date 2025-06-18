import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

# LLMの初期化
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# 専門家の選択肢
expert_types = {
    "栄養学の専門家": "あなたは栄養学の専門家です。科学的根拠に基づき、わかりやすく丁寧に回答してください。",
    "子供の発達の専門家": "あなたは子供の発達に関する専門家です。発達心理学や教育学の知見を活かし、保護者にも理解しやすいように回答してください。"
}

st.title("専門家LLMチャット")

# ラジオボタンで専門家タイプ選択
expert = st.radio("専門家の種類を選択してください", list(expert_types.keys()))

# 入力フォーム
user_input = st.text_input("質問を入力してください")

if st.button("送信") and user_input:
    # システムメッセージを選択値で切り替え
    system_message = SystemMessage(content=expert_types[expert])
    human_message = HumanMessage(content=user_input)
    response = llm([system_message, human_message])
    st.write("### 回答")
    st.write(response.content)

