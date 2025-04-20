# import streamlit as st

# st.set_page_config(
#     page_title="My great ChatGPT",
#     page_icon="🤗"
# )
# st.header("My Great ChatGPT 🤗")

# if user_input := st.chat_input("何か入力してね！"):
#     st.write(user_input)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    temperature=0.9,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

messages = [
    (
        "system",
        "あなたは日本語を関西弁に変換する助手です。ユーザーの文章を関西弁に変換してください。"
    ),
    (
        "human",
        "多様性（たようせい、英: diversity）とは、ある集団の中に異なる特徴・特性を持つ人がともに存在することである。英語の多様性diversityの語源は、ラテン語のdiverstiasに由来し、この言葉は、最初は「一致可能なものに反すること、矛盾、対立、不一致」といった消極的な意味を有したが、第二義的に「相違、多様、様々な形になる」という意味も併せ持っていた。17世紀になって、消極的な意味が失われ、現在のニュアンスになったとされている。また、diversityとは、相異なる要素を有する、もしくはそれから構成される状態であり、そこから更に、異なるタイプの人々をあるグループや組織に包摂すること、とされている"
    )
]

ai_msg = llm.invoke(messages)
print(ai_msg)
