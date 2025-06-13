import streamlit as st

st.set_page_config(page_title="어울리는 디즈니 공주 테스트", page_icon="👑")
st.title("✨ 나와 어울리는 디즈니 공주는? 👸")
st.write("아래 질문에 답해보세요. 당신과 닮은 디즈니 공주를 찾아드릴게요!")

# 질문지
q1 = st.radio("1. 당신은 모험을 좋아하나요?", 
              ("아주 좋아해요!", "가끔은요", "별로 안 좋아해요"))

q2 = st.radio("2. 당신의 성격은 어떤 편인가요?", 
              ("용감하고 당당해요", "차분하고 침착해요", "명랑하고 사교적이에요", "조용하고 내성적이에요"))

q3 = st.radio("3. 어려움이 닥쳤을 때 어떻게 대응하나요?", 
              ("직접 부딪혀 해결해요", "주변의 도움을 구해요", "잠시 피하고 다시 도전해요"))

q4 = st.radio("4. 선호하는 환경은?", 
              ("바다", "도시나 궁전", "숲속이나 시골", "산이나 눈 덮인 곳"))

q5 = st.radio("5. 가장 중요하게 생각하는 가치는?", 
              ("자유", "사랑", "용기", "지혜", "가족"))

# 각 공주 초기 점수 설정
scores = {
    "모아나": 0,
    "엘사": 0,
    "벨": 0,
    "라푼젤": 0,
    "애리얼": 0
}

# 답변에 따라 점수 가중치 부여
def calculate_scores():
    # Q1
    if q1 == "아주 좋아해요!":
        scores["모아나"] += 2
        scores["라푼젤"] += 1
        scores["애리얼"] += 1
    elif q1 == "가끔은요":
        scores["벨"] += 1
        scores["엘사"] += 1
    else:
        scores["엘사"] += 1
        scores["벨"] += 1

    # Q2
    if q2 == "용감하고 당당해요":
        scores["모아나"] += 2
        scores["라푼젤"] += 1
    elif q2 == "차분하고 침착해요":
        scores["엘사"] += 2
    elif q2 == "명랑하고 사교적이에요":
        scores["애리얼"] += 2
    elif q2 == "조용하고 내성적이에요":
        scores["벨"] += 2

    # Q3
    if q3 == "직접 부딪혀 해결해요":
        scores["모아나"] += 1
        scores["엘사"] += 1
    elif q3 == "주변의 도움을 구해요":
        scores["라푼젤"] += 1
        scores["애리얼"] += 1
    elif q3 == "잠시 피하고 다시 도전해요":
        scores["벨"] += 1

    # Q4
    if q4 == "바다":
        scores["모아나"] += 2
        scores["애리얼"] += 2
    elif q4 == "도시나 궁전":
        scores["벨"] += 1
        scores["엘사"] += 1
    elif q4 == "숲속이나 시골":
        scores["라푼젤"] += 2
    elif q4 == "산이나 눈 덮인 곳":
        scores["엘사"] += 2

    # Q5
    if q5 == "자유":
        scores["모아나"] += 1
        scores["애리얼"] += 1
        scores["라푼젤"] += 1
    elif q5 == "사랑":
        scores["애리얼"] += 1
        scores["라푼젤"] += 1
    elif q5 == "용기":
        scores["모아나"] += 1
        scores["엘사"] += 1
    elif q5 == "지혜":
        scores["벨"] += 2
    elif q5 == "가족":
        scores["엘사"] += 1

# 결과 계산 및 표시
if st.button("👑 결과 보기"):
    calculate_scores()
    top_princess = max(scores, key=scores.get)
    descriptions = {
        "모아나": "모험을 사랑하고 바다를 두려워하지 않는 당신은 모아나와 닮았어요!",
        "엘사": "냉철하면서도 따뜻한 마음을 지닌 당신은 엘사와 잘 어울려요.",
        "벨": "지혜롭고 호기심 많은 당신은 벨과 가장 닮았어요.",
        "라푼젤": "자유를 꿈꾸며 세상에 대한 호기심이 가득한 당신은 라푼젤이에요!",
        "애리얼": "새로운 세계에 대한 동경이 강한 당신은 애리얼과 잘 어울려요!"
    }

    st.subheader(f"🎉 당신과 어울리는 디즈니 공주는... **{top_princess}**!")
    st.success(descriptions[top_princess])

    # 공주 이미지 (원하는 이미지 URL로 바꾸기)
    image_urls = {
        "모아나": "https://i.imgur.com/Y1VZUGm.jpg",
        "엘사": "https://i.imgur.com/3nJgVxk.jpg",
        "벨": "https://i.imgur.com/xLPwdrz.jpg",
        "라푼젤": "https://i.imgur.com/sgxyVVW.jpg",
        "애리얼": "https://i.imgur.com/8WKiNPR.jpg"
    }
    st.image(image_urls[top_princess], use_column_width=True)
