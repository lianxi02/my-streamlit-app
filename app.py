import streamlit as st
# =========================
# 頁面設定
# =========================
st.set_page_config(
    page_title="課程回饋表單",
    page_icon="📝",
    layout="centered"
)
# =========================
# 自訂 CSS
# =========================
st.markdown("""
<style>
    /* 整體背景 */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eef7 100%);
    }
    /* 主要內容區域 */
    .main .block-container {
        max-width: 750px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    /* 標題區 */
    .title-box {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(79, 70, 229, 0.25);
    }
    .title-box h1 {
        margin: 0;
        font-size: 32px;
        font-weight: 700;
    }
    .title-box p {
        margin-top: 10px;
        margin-bottom: 0;
        font-size: 16px;
        opacity: 0.9;
    }
    /* 表單卡片 */
    .form-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
    }
    /* Streamlit Label */
    label {
        font-weight: 600 !important;
        color: #374151 !important;
    }
    /* 輸入框 */
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px !important;
    }
    /* Slider */
    .stSlider {
        padding-top: 5px;
        padding-bottom: 10px;
    }
    /* 送出按鈕 */
    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        font-size: 17px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.3);
    }
    /* 成功訊息 */
    .success-box {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        border-left: 5px solid #22c55e;
        padding: 18px 20px;
        border-radius: 12px;
        color: #166534;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        margin-top: 20px;
    }
    /* 頁尾 */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        margin-top: 25px;
    }
</style>
""", unsafe_allow_html=True)
# =========================
# 標題
# =========================
st.markdown("""
<div class="title-box">
    <h1>📝 課程回饋表單</h1>
    <p>您的意見是我們持續改進課程的重要參考</p>
</div>
""", unsafe_allow_html=True)
# =========================
# 表單
# =========================
with st.form("feedback_form"):
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    # 姓名
    st.markdown("### 👤 基本資料")
    name = st.text_input(
        "姓名",
        placeholder="請輸入您的姓名"
    )
    # 科系
    department = st.selectbox(
        "科系",
        ["資訊工程系", "電子工程系", "其他"]
    )
    st.markdown("---")
    # 滿意度
    st.markdown("### ⭐ 課程評價")
    satisfaction = st.slider(
        "課程滿意度",
        min_value=1,
        max_value=5,
        value=3,
        step=1
    )
    # 根據分數顯示文字
    satisfaction_text = {
        1: "😞 非常不滿意",
        2: "😕 不滿意",
        3: "😐 普通",
        4: "🙂 滿意",
        5: "🤩 非常滿意"
    }
    st.markdown(
        f"<p style='text-align:center; font-size:20px; "
        f"font-weight:600; color:#4f46e5;'>"
        f"{satisfaction} 分　{satisfaction_text[satisfaction]}"
        f"</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")
    # 意見回饋
    st.markdown("### 💬 意見回饋")
    feedback = st.text_area(
        "請留下您對課程的想法",
        placeholder="例如：課程內容很實用，希望未來可以增加更多實作練習……",
        height=150
    )
    st.write("")
    # 送出
    submitted = st.form_submit_button("📨 送出回饋")
    st.markdown("</div>", unsafe_allow_html=True)
# =========================
# 送出後處理
# =========================
if submitted:
    if name.strip() == "":
        st.warning("⚠️ 請先輸入您的姓名。")
    else:
        st.markdown("""
        <div class="success-box">
            ✅ 感謝您的回饋！<br>
            您的意見已成功送出。
        </div>
        """, unsafe_allow_html=True)
# =========================
# 頁尾
# =========================
st.markdown("""
<div class="footer">
    課程回饋系統 · Thank you for your feedback ❤️
</div>
""", unsafe_allow_html=True)