import streamlit as st


st.set_page_config(page_title="First Streamlit App")

st.title("AI 협업 개발 실습")
st.write("첫 번째 Streamlit 앱입니다.")

# 사용자 이름을 입력받는 창입니다.
name = st.text_input("이름을 입력하세요")

# 화면을 구분하기 위한 선입니다.
st.divider()

# 실습 진행 방법을 알려주는 안내 문구입니다.
st.info("이름을 입력한 뒤 실습 시작 버튼을 눌러보세요.")

# 버튼을 누르면 환영 메시지를 보여줍니다.
if st.button("실습 시작"):
    if name:
        st.success(f"{name}님, 환영합니다! AI 협업 개발 실습을 시작합니다.")
    else:
        st.warning("이름을 먼저 입력해주세요.")
