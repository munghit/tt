import streamlit as st
import pandas as pd

# ------------------------------
# 페이지 설정
# ------------------------------
st.set_page_config(
    page_title="평균 계산 과정",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# CSS
# ------------------------------
st.markdown("""
<style>

.main{
    padding-top:20px;
}

.step{
    background:#f8f9fa;
    border-radius:15px;
    padding:20px;
    text-align:center;
    box-shadow:0px 4px 10px rgba(0,0,0,0.15);
    height:260px;
}

.big{
    font-size:24px;
    font-weight:bold;
    color:#0d6efd;
}

.small{
    font-size:18px;
}

.result{
    background:#eef7ff;
    border-radius:15px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# 제목
# ------------------------------

st.title("📊 소음 데이터 평균 계산 과정")

st.caption("측정된 소음 데이터를 장소와 시간대별로 분류하여 평균을 계산하는 과정")

st.divider()

# ------------------------------
# 과정
# ------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""
<div class="step">

<div class="big">① 데이터 수집</div>

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

with c2:

    st.markdown("""
<div class="step">

<div class="big">② 데이터 분류</div>

<br>

📂 장소별

<br><br>

⏰ 시간대별

<br>

• 쉬는시간

<br>

• 점심시간

<br>

• 야자시간

</div>
""",unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="step">

<div class="big">③ 평균 계산</div>

<br>

평균(dB)

<br><br>

= Σ(소음값)

<br>

────────

<br>

측정횟수

</div>
""",unsafe_allow_html=True)

with c4:

    st.markdown("""
<div class="step">

<div class="big">④ 결과 출력</div>

<br>

📋 평균 dB

<br><br>

📊 장소별 비교

<br><br>

⏰ 시간대별 비교

</div>
""",unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>⬇️</h1>",unsafe_allow_html=True)

st.divider()

# ------------------------------
# 공식
# ------------------------------

left,right = st.columns([1,1])

with left:

    st.subheader("📐 평균 계산 공식")

    st.latex(r'''
    평균(dB)=\frac{\sum dB}{측정횟수}
    ''')

    st.info("""
① 같은 장소의 데이터를 선택

② 같은 시간대의 데이터를 선택

③ 소음값을 모두 더함

④ 측정횟수로 나눔

⑤ 평균 dB 산출
""")

with right:

    st.subheader("📝 계산 예시")

    st.code("""
교실 (점심시간)

51.2
50.8
52.0
51.1

↓

(51.2 + 50.8 + 52.0 + 51.1)

÷

4

=

51.27 dB
""")

st.divider()

# ------------------------------
# 결과표
# ------------------------------

st.subheader("📋 평균 계산 결과")

df = pd.DataFrame({

    "구분":["쉬는시간","점심시간","야자시간"],

    "교실":["47.34 dB","51.27 dB","-"],

    "다목적실":["48.75 dB","45.68 dB","34.39 dB"],

    "탑티어실":["29.79 dB","32.52 dB","40.66 dB"]

})

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ------------------------------
# 결과 해석
# ------------------------------

st.subheader("🔍 결과 분석")

a,b = st.columns(2)

with a:

    st.success("""
✅ 교실은 점심시간 평균이 가장 높아 가장 시끄럽습니다.

✅ 탑티어실은 쉬는시간과 점심시간에 가장 조용합니다.
""")

with b:

    st.warning("""
✅ 다목적실은 시간이 지날수록 소음이 감소하는 경향을 보였습니다.

✅ 장소마다 시간대에 따른 평균 소음이 다르게 나타났습니다.
""")

st.divider()



```python
st.divider()

st.subheader("📌 전체 흐름")

st.info("""
🔊 소음 측정
      ↓
📂 장소별 분류
      ↓
⏰ 시간대별 분류
      ↓
📊 평균 계산
      ↓
📋 결과 비교 및 분석
""")
