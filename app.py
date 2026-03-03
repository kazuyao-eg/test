import streamlit as st

st.title("はじめての Streamlit アプリ")

st.write("こんにちは！これは Streamlit で動くシンプルなアプリです。")

name = st.text_input("名前を入力してください")
age = st.number_input("年齢を入力してください", min_value=0, max_value=120, value=20)

if st.button("挨拶する"):
    if name:
        st.success(f"こんにちは、{name}さん！あなたは {age} 歳ですね。")
    else:
        st.warning("先に名前を入力してください。")
