import streamlit as st


st.set_page_config(
    page_title="AI 협업 개발 실습",
    page_icon="🤝",
    layout="centered",
)


def make_prompt(goal: str, role: str, constraints: str) -> str:
    """실습에서 바로 복사해 쓸 수 있는 AI 협업 프롬프트를 만든다."""
    prompt = f"""[role]
너는 {role}

[task]
{goal}

[constraints]
{constraints}

[output]
1. 구현 계획
2. 필요한 파일 변경
3. 실행 및 검증 방법
"""
    return prompt.strip()


st.title("AI 협업 개발 실습")
st.caption("첫 번째 Streamlit 앱으로 요구사항을 정리하고 AI에게 전달할 프롬프트를 만들어 봅니다.")

st.subheader("1. 만들고 싶은 기능")
goal = st.text_area(
    "요구사항",
    value="사용자가 입력한 문장을 분석해서 핵심 키워드와 다음 행동을 보여주는 웹앱을 만든다.",
    height=110,
)

st.subheader("2. AI에게 맡길 역할")
role = st.text_input(
    "역할",
    value="Python Streamlit 기반 웹앱을 빠르게 생성하는 AI 개발자",
)

st.subheader("3. 제약 조건")
constraints = st.text_area(
    "조건",
    value="- app.py 파일 하나만 사용한다.\n- 초보자도 이해할 수 있게 단순하게 만든다.\n- 실행 방법을 함께 안내한다.",
    height=100,
)

st.divider()

prompt = make_prompt(goal, role, constraints)

st.subheader("생성된 협업 프롬프트")
st.code(prompt, language="markdown")

col1, col2 = st.columns(2)
with col1:
    st.metric("요구사항 길이", f"{len(goal)}자")
with col2:
    st.metric("체크 항목", "3개")

st.subheader("실습 체크리스트")
checks = [
    "요구사항을 구체적으로 썼다.",
    "AI의 역할을 명확히 정했다.",
    "파일, 기술, 난이도 같은 제약 조건을 적었다.",
]

for item in checks:
    st.checkbox(item)

st.info("실행 명령어: streamlit run app.py")
