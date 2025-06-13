import streamlit as st

st.set_page_config(page_title="어울리는 디즈니 공주 찾기", page_icon="👑")

st.title("✨ 어울리는 디즈니 공주를 찾아보세요! 👸")
st.write("5가지 질문에 답하면 당신과 어울리는 디즈니 공주를 추천해드려요!")

# 질문 1
q1 = st.radio("1. 당신은 모험을 좋아하나요?", 
              ("아주 좋아해요!", "가끔은요", "별로 안 좋아해요"))

# 질문 2
q2 = st.radio("2. 당신의 성격은 어떤 편인가요?", 
              ("용감하고 당당해요", "차분하고 침착해요", "명랑하고 사교적이에요", "조용하고 내성적이에요"))

# 질문 3
q3 = st.radio("3. 어려움이 닥쳤을 때 어떻게 대응하나요?", 
              ("직접 부딪혀 해결해요", "주변의 도움을 구해요", "잠시 피하고 다시 도전해요"))

# 질문 4
q4 = st.radio("4. 선호하는 환경은?", 
              ("바다나 자연", "도시나 궁전", "숲속이나 시골", "산이나 눈 덮인 곳"))

# 질문 5
q5 = st.radio("5. 가장 중요하게 생각하는 가치는?", 
              ("자유", "사랑", "용기", "지혜", "가족"))

# 결과 추천 로직
def recommend_princess(q1, q2, q3, q4, q5):
    if q1 == "아주 좋아해요" and q2 == "용감하고 당당해요":
        return "모아나", "바다를 사랑하고 모험심이 강한 당신은 모아나와 닮았어요!"
    elif q2 == "차분하고 침착해요" and q4 == "산이나 눈 덮인 곳":
        return "엘사", "차분하면서도 강한 힘을 지닌 당신은 엘사와 비슷하군요!"
    elif q2 == "명랑하고 사교적이에요" and q5 == "사랑":
        return "애리얼", "사랑을 찾아 바다 너머로 떠난 애리얼처럼, 당신은 사랑을 중시하는 사람이에요."
    elif q3 == "주변의 도움을 구해요" and q5 == "가족":
        return "라푼젤", "새로운 세계를 향해 나아가는 용기를 지닌 라푼젤처럼, 당신도 밝은 에너지를 지녔어요."
    else:
        return "벨", "지혜롭고 독서를 좋아하는 당신은 벨과 잘 어울려요!"

# 결과 출력
if st.button("👑 나와 어울리는 공주 찾기!"):
    princess, description = recommend_princess(q1, q2, q3, q4, q5)
    st.subheader(f"당신과 어울리는 디즈니 공주는... {princess}!")
    st.success(description)
    st.image(f"https://example.com/images/{princess}.jpg", caption=princess, use_column_width=True)
