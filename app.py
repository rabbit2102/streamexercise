import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="오늘 뭐 먹지?", layout="wide")
st.title("🍴 오늘 뭐 먹지? 메뉴 추천기")

# CSV 파일 불러오기
df = pd.read_csv("menu.csv")

# 사용자 입력
food_type = st.selectbox("음식 종류를 선택하세요:", df['종류'].unique())
soup = st.radio("국물이 있는 걸 원하시나요?", ['있음', '없음'])
spicy = st.radio("매운 음식을 원하시나요?", ['매움', '안매움'])
temperature = st.radio("음식 온도는?", ['뜨거움', '차가움'])

# 필터링
recommendations = df[
    (df['종류'] == food_type) &
    (df['국물'] == soup) &
    (df['매움'] == spicy) &
    (df['온도'] == temperature)
]


# 결과 보여주기
if len(recommendations) > 0:
    st.subheader("추천 메뉴:")
    max_cols = 3  # 한 줄에 최대 3개
    for i in range(0, len(recommendations), max_cols):
        row_items = recommendations.iloc[i:i+max_cols]
        cols = st.columns(len(row_items))
        for col, menu in zip(cols, row_items.itertuples()):
            with col:
                st.markdown(f"**{menu.메뉴}**")
                st.image(menu.이미지, width=400)
else:
    st.write("조건에 맞는 메뉴가 없어요 😢")
