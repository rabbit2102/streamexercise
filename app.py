# streamlit_square_app.py
import streamlit as st
import pandas as pd
import numpy as np

# 앱 제목
st.title("🔢 Streamlit 숫자 제곱 계산기")

# 사용자 입력
number = st.number_input("숫자를 입력하세요:", min_value=0, value=2, step=1)

# 계산 결과
square = number ** 2
st.write(f"👉 {number}의 제곱은 **{square}** 입니다!")

# 데이터프레임 만들기
data = pd.DataFrame({
    "x": np.arange(0, number + 1),
    "x²": np.arange(0, number + 1) ** 2
})

# 차트 표시
st.subheader("📈 제곱 함수 시각화")
st.line_chart(data.set_index("x"))

# 추가: 체크박스로 데이터 표시
if st.checkbox("데이터 보기"):
    st.dataframe(data)
