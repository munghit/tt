import streamlit as st
import pandas as pd


# ==============================
# 페이지 설정
# ==============================

st.set_page_config(
    page_title="소음 데이터 분석",
    page_icon="🔊",
    layout="wide"
)


# ==============================
# CSS
# ==============================

st.markdown("""
<style>

/* 전체 배경 */
.stApp{
    background:#0f172a;
    color:white;
}


/* 제목 */
h1{
    color:white;
    text-align:center;
}

h2,h3{
    color:#e2e8f0;
}


/* 설명 */
.stCaption{
    color:#94a3b8;
}


/* 카드 공통 */
.card{

    border-radius:20px;
    padding:25px;
    height:280px;
    color:white;

    box-shadow:
    0px 8px 20px rgba(0,0,0,0.35);

}


/* 단계별 색상 */

.blue{
background:linear-gradient(135deg,#2563eb,#1d4ed8);
}

.green{
background:linear-gradient(135deg,#16a34a,#15803d);
}

.orange{
background:linear-gradient(135deg,#ea580c,#c2410c);
}

.purple{
background:linear-gradient(135deg,#9333ea,#6b21a8);
}



.number{

font-size:35px;
font-weight:900;

}


.card-title{

font-size:24px;
font-weight:bold;

}


.card-text{

font-size:18px;
line-height:1.8;

}



/* 공식 박스 */

.box{

background:#1e293b;
padding:25px;
border-radius:20px;

}



/* 결과 카드 */

.analysis{

padding:25px;
border-radius:20px;
font-size:18px;

}


.good{

background:#064e3b;
border-left:8px solid #22c55e;

}


.warn{

background:#78350f;
border-left:8px solid #facc15;

}


/* dataframe */

[data-testid="stDataFrame"]{

background:white;
border-radius:15px;

}


/* info */

.stAlert{

border-radius:15px;

}



</style>

""",unsafe_allow_html=True)



# ==============================
# 제목
# ==============================


st.title("🔊 소음 데이터 평균 분석 시스템")

st.markdown(
"""
<div style="
text-align:center;
font-size:20px;
color:#94a3b8;
">
장소와 시간대별 소음 데이터를 분석하여 평균 dB를 산출하는 과정
</div>
""",
unsafe_allow_html=True
)


st.divider()



# ==============================
# 분석 과정
# ==============================


st.subheader("📌 데이터 처리 과정")


c1,c2,c3,c4 = st.columns(4)



cards=[

(
"①",
"데이터 수집",
"""
🔊 교실

🔊 다목적실

🔊 탑티어실

<br>

측정값 : dB
""",
"blue"
),


(
"②",
"데이터 분류",
"""
📂 장소별 분류

⏰ 시간대별 분류

<br>

쉬는시간<br>
점심시간<br>
야자시간
""",
"green"
),


(
"③",
"평균 계산",
"""
평균(dB)

<br>

Σ 소음값

÷

측정횟수

""",
"orange"
),


(
"④",
"결과 분석",
"""
📊 평균 비교

<br>

장소별 차이

시간별 변화
""",
"purple"
)

]


for col,data in zip(
    [c1,c2,c3,c4],
    cards
):

    with col:

        st.markdown(f"""

        <div class="card {data[3]}">

        <div class="number">
        {data[0]}
        </div>

        <div class="card-title">
        {data[1]}
        </div>

        <br>

        <div class="card-text">
        {data[2]}
        </div>

        </div>

        """,
        unsafe_allow_html=True)



st.markdown(
"""
<h1 style='text-align:center;color:#38bdf8'>
⬇️
</h1>
""",
unsafe_allow_html=True
)


# ==============================
# 공식 + 계산
# ==============================


left,right=st.columns(2)



with left:

    st.subheader("📐 평균 계산 공식")


    st.markdown("""
    <div class="box">

    """,
    unsafe_allow_html=True)


    st.latex(
    r"""
    평균(dB)=\frac{\sum dB}{측정횟수}
    """
    )


    st.markdown(
    """
    <br>

    ① 장소 선택

    <br>

    ② 시간대 선택

    <br>

    ③ 소음값 합산

    <br>

    ④ 측정 횟수로 나누기

    <br>

    ⑤ 평균 dB 출력

    """,
    unsafe_allow_html=True
    )

    st.markdown("</div>",
    unsafe_allow_html=True)




with right:


    st.subheader("🧮 실제 계산 예시")


    st.code(
"""
교실 - 점심시간


51.2
50.8
52.0
51.1


(51.2+50.8+52.0+51.1)

÷

4


= 51.27 dB
"""
)



st.divider()



# ==============================
# 결과표
# ==============================


st.subheader("📊 평균 소음 결과")


df=pd.DataFrame({

"시간대":
[
"쉬는시간",
"점심시간",
"야자시간"
],

"교실":
[
"47.34 dB",
"51.27 dB",
"-"
],

"다목적실":
[
"48.75 dB",
"45.68 dB",
"34.39 dB"
],

"탑티어실":
[
"29.79 dB",
"32.52 dB",
"40.66 dB"
]


})


st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)



st.divider()



# ==============================
# 분석 결과
# ==============================


st.subheader("🔍 데이터 분석 결과")


a,b=st.columns(2)


with a:

    st.markdown(
"""
<div class="analysis good">

<h3>🟢 주요 발견</h3>

✅ 교실은 점심시간 평균 소음이 가장 높음

<br>

✅ 탑티어실은 대부분 시간대에서 낮은 소음 유지

</div>

""",
unsafe_allow_html=True
)



with b:

    st.markdown(
"""
<div class="analysis warn">

<h3>🟡 패턴 분석</h3>

✅ 다목적실은 시간 변화에 따라 소음 감소

<br>

✅ 장소별 이용 특성에 따라 소음 차이 발생

</div>

""",
unsafe_allow_html=True
)



st.divider()



# ==============================
# 전체 흐름
# ==============================


st.subheader("🚀 전체 데이터 흐름")


st.markdown(
"""
<div class="box">

🔊 소음 측정

<br>
⬇️

📂 장소별 데이터 분류

<br>
⬇️

⏰ 시간대별 분류

<br>
⬇️

📊 평균 계산

<br>
⬇️

📋 결과 비교 및 분석

</div>
""",
unsafe_allow_html=True
)
