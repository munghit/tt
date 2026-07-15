import streamlit as st

# -------------------------------
# 페이지 설정
# -------------------------------
st.set_page_config(
    page_title="평균 계산 과정",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# CSS
# -------------------------------
st.markdown("""
<style>

.main{
    padding-top:20px;
}

.block{
    background-color:#F8F9FA;
    border-radius:15px;
    padding:25px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    height:260px;
}

.step{
    font-size:22px;
    font-weight:bold;
    color:#0E7490;
}

.title{
    font-size:40px;
    font-weight:bold;
}

.sub{
    font-size:18px;
    color:gray;
}

.arrow{
    text-align:center;
    font-size:45px;
    color:#4CAF50;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# 제목
# -------------------------------
st.markdown("<p class='title'>📊 소음 데이터 평균 계산 과정</p>", unsafe_allow_html=True)

st.markdown(
"<p class='sub'>측정된 소음 데이터를 장소와 시간대별로 분류하여 평균을 계산한 과정입니다.</p>",
unsafe_allow_html=True
)

st.divider()

# -------------------------------
# STEP
# -------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:

    st.markdown("""
    <div class="block">

    <div class="step">① 데이터 수집</div>

    <br>

    🔊 교실

    <br><br>

    🔊 다목적실

    <br><br>

    🔊 탑티어실

    <br><br>

    소음(dB) 측정

    </div>
    """,unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="block">

    <div class="step">② 데이터 분류</div>

    <br>

    📂 장소별 분류

    <br><br>

    ⏰ 시간대별 분류

    <br><br>

    • 쉬는 시간

    <br>

    • 점심시간

    <br>

    • 야자시간

    </div>
    """,unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="block">

    <div class="step">③ 평균 계산</div>

    <br><br>

    평균(dB)

    <br><br>

    =

    <br><br>

    소음값의 합

    <br>

    ─────────

    <br>

    측정 횟수

    </div>
    """,unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class="block">

    <div class="step">④ 결과 출력</div>

    <br>

    📊 평균 dB 계산

    <br><br>

    📈 장소별 비교

    <br><br>

    ⏰ 시간대별 비교

    <br><br>

    💡 특징 분석

    </div>
    """,unsafe_allow_html=True)

st.markdown("<div class='arrow'>⬇️</div>",unsafe_allow_html=True)

st.divider()

# -------------------------------
# 계산식
# -------------------------------

st.subheader("📐 평균 계산 공식")

st.latex(r'''
평균(dB)=\frac{\sum_{i=1}^{n}dB_i}{n}
''')

st.info("""
**계산 방법**

① 같은 장소와 같은 시간대의 소음 데이터를 모은다.

② 모든 소음값을 더한다.

③ 측정 횟수로 나눈다.

④ 평균 소음(dB)을 계산한다.
""")

st.divider()

# -------------------------------
# 결과 이미지
# -------------------------------

st.subheader("📋 평균 계산 결과")

st.image(
    "images/average_result.png",
    use_container_width=True
)

st.divider()

# -------------------------------
# 해석
# -------------------------------

st.subheader("🔍 결과 해석")

c1,c2 = st.columns(2)

with c1:

    st.success("""
✔ 점심시간에는 탑티어실이 가장 조용합니다.

✔ 교실은 점심시간 평균이 가장 높아 가장 시끄럽습니다.

✔ 다목적실은 시간이 지날수록 소음이 감소하는 경향을 보입니다.
""")

with c2:

    st.warning("""
✔ 탑티어실은 쉬는 시간과 점심시간에는 매우 조용합니다.

✔ 야자시간에는 소음이 증가하는 경향이 나타났습니다.

✔ 장소마다 시간대에 따른 소음 특성이 다르게 나타났습니다.
""")

st.divider()

st.caption("ⓒ Noise Analysis Dashboard")
