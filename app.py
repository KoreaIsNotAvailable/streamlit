import streamlit as st

변수 = st.session_state
if '체력' not in 변수:
    변수.체력=100
st.image("https://static1.personalitydatabase.net/2/pdb-images-prod/3b65a9a3/profile_images/e320d616f7c243e0aff65da751303967.png")
st.title(f"남은 체력: {변수.체력}")
if 변수.체력 < 0 :
    st.error("사망")

if st.button("2.3만드러줘"):
    변수.체력 = 변수.체력 - 20
    st.rerun()

if st.button("칭찬"):
    변수.체력 = 변수.체력 + 0.1
    st.rerun()
