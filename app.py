import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Futurio",
    page_icon="🚀",
    layout="wide"
)

# ================= HEADER =================

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🚀 Futurio</h1>
    <h4 style='text-align: center;'>See Your Future. Shape Your Path.</h4>
""", unsafe_allow_html=True)

st.divider()

# ================= SIDEBAR =================

st.sidebar.header("📘 Nhập thông tin của bạn")

name = st.sidebar.text_input("Tên của bạn")

math = st.sidebar.slider("Điểm Toán", 0.0, 10.0, 5.0)
literature = st.sidebar.slider("Điểm Ngữ Văn", 0.0, 10.0, 5.0)
english = st.sidebar.slider("Điểm Tiếng Anh", 0.0, 10.0, 5.0)
it = st.sidebar.slider("Điểm Tin học", 0.0, 10.0, 5.0)

favorite = st.sidebar.selectbox(
    "Lĩnh vực yêu thích",
    ["Công nghệ", "Kinh doanh", "Sáng tạo nội dung", "Khoa học", "Ngôn ngữ"]
)

goal = st.sidebar.text_area("Bạn muốn trở thành ai?")

analyze = st.sidebar.button("🔮 Phân tích tương lai")

# ================= MAIN =================

if analyze:

    avg = (math + literature + english + it) / 4

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"📊 Hồ sơ của {name}")
        st.metric("Điểm trung bình", f"{avg:.2f}")

        if math >= 8 or it >= 8:
            strength = "Tư duy logic & công nghệ"
        elif literature >= 8:
            strength = "Ngôn ngữ & sáng tạo"
        elif english >= 8:
            strength = "Ngoại ngữ"
        else:
            strength = "Tiềm năng đa lĩnh vực"

        st.info(f"Điểm mạnh nổi bật: {strength}")

    # ================= RADAR CHART =================

    with col2:
        st.subheader("🧠 Bản đồ năng lực")

        labels = ['Toán', 'Văn', 'Anh', 'Tin']
        values = [math, literature, english, it]

        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        values += values[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.25)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)

        ax.set_ylim(0, 10)

        st.pyplot(fig)

    st.divider()

    # ================= FUTURE SCENARIOS =================

    st.subheader("🔮 3 Kịch Bản Tương Lai")

    colA, colB, colC = st.columns(3)

    with colA:
        st.success("Giữ nguyên hiện tại")
        st.write("Ổn định nhưng khó bứt phá nếu không nâng cao kỹ năng.")

    with colB:
        st.warning("Phát triển lĩnh vực yêu thích")
        st.write(f"Nếu đầu tư mạnh vào {favorite}, cơ hội thành công sẽ tăng cao.")

    with colC:
        st.error("Thay đổi chiến lược")
        st.write("Cải thiện điểm yếu và tham gia thêm hoạt động ngoại khóa.")

    st.divider()

    st.markdown(f"""
    ### 🎯 Mục tiêu của bạn:
    > {goal}
    """)

    st.success("✨ Futurio khuyên bạn nên bắt đầu nâng cấp bản thân ngay hôm nay!")