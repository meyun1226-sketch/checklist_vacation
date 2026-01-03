
import streamlit as st
st.set_page_config(layout="centered")

focus_df["date"] = pd.to_datetime(
    focus_df["date"],
    errors="coerce"
).dt.normalize()


st.set_page_config(
    page_title="Study App",
    page_icon="📘",
    layout="wide"
)

st.title("📘 방학용 학습 관리 앱")

st.markdown("""
왼쪽 사이드바에서 원하는 페이지를 선택하세요.

- 🛌 컨디션 & 기상 루틴  
- 📊 공부 기록 대시보드  
- 🗓️ 주간 시간표  
- ✅ 오늘 체크리스트  
- ⏱️ 집중력 테스트  
""")
