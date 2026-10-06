import streamlit as st
from datetime import datetime

# ==============================
# CẤU HÌNH TRANG
# ==============================

st.set_page_config(
    page_title="Quản Lý NVD",
    page_icon="💇",
    layout="wide"
)

# ==============================
# TIÊU ĐỀ
# ==============================

st.title("💇 QUẢN LÝ NVD")
st.caption("Hệ thống quản lý dịch vụ và doanh thu")

st.divider()

# ==============================
# MENU
# ==============================

menu = st.sidebar.radio(
    "📋 MENU",
    [
        "🏠 Trang chủ",
        "✂️ Dịch vụ",
        "👥 Nhân viên",
        "📊 Báo cáo",
        "⚙️ Cài đặt"
    ]
)

# ==============================
# TRANG CHỦ
# ==============================

if menu == "🏠 Trang chủ":

    st.header("🏠 Quản lý hôm nay")

    # Thông tin tổng quan
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("✂️ Số lượt cắt", "0")

    with col2:
        st.metric("🧴 Hóa chất", "0")

    with col3:
        st.metric("💰 Doanh thu", "0 VNĐ")

    st.divider()

    # ==============================
    # GHI NHẬN DỊCH VỤ
    # ==============================

    st.subheader("📝 Ghi nhận dịch vụ")

    if st.button(
        "➕ GHI NHẬN DỊCH VỤ",
        use_container_width=True
    ):
        st.session_state["hien_form"] = True

    # ==============================
    # FORM GHI NHẬN
    # ==============================

    if st.session_state.get("hien_form", False):

        st.divider()

        st.subheader("📝 Thông tin dịch vụ")

        # ------------------------------
        # LOẠI DỊCH VỤ
        # ------------------------------

        loai_dich_vu = st.radio(
            "Loại dịch vụ",
            [
                "✂️ Cắt",
                "🧴 Hóa chất"
            ],
            horizontal=True
        )

        # ------------------------------
        # GIÁ DỊCH VỤ
        # ------------------------------

        gia = st.number_input(
            "💰 Giá dịch vụ (VNĐ)",
            min_value=0,
            step=10000,
            value=0
        )

        # ------------------------------
        # HÌNH THỨC THANH TOÁN
        # ------------------------------

        thanh_toan = st.radio(
            "💳 Hình thức thanh toán",
            [
                "💵 Tiền mặt",
                "🏦 Chuyển khoản"
            ],
            horizontal=True
        )

        # ------------------------------
        # THỜI GIAN
        # ------------------------------

        st.info(
            "🕐 Thời gian sẽ được hệ thống tự động "
            "ghi nhận khi bạn bấm XÁC NHẬN."
        )

        # ------------------------------
        # NÚT XÁC NHẬN / HỦY
        # ------------------------------

        col1, col2 = st.columns(2)

        with col1:
            xac_nhan = st.button(
                "✅ XÁC NHẬN",
                use_container_width=True
            )

        with col2:
            huy = st.button(
                "❌ HỦY",
                use_container_width=True
            )

        # ==============================
        # XÁC NHẬN DỊCH VỤ
        # ==============================

        if xac_nhan:

            thoi_gian = datetime.now().strftime("%H:%M:%S")

            st.success("✅ Đã ghi nhận dịch vụ!")

            st.write("### Thông tin vừa ghi nhận")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("🕐 **Giờ:**")
                st.write(thoi_gian)

            with col2:
                st.write("✂️ **Dịch vụ:**")
                st.write(loai_dich_vu)

            with col3:
                st.write("💰 **Giá:**")
                st.write(f"{gia:,.0f} VNĐ")

            with col4:
                st.write("💳 **Thanh toán:**")
                st.write(thanh_toan)

            # Đóng form
            st.session_state["hien_form"] = False

        # ==============================
        # HỦY
        # ==============================

        if huy:

            st.session_state["hien_form"] = False

            st.rerun()


# ==============================
# DỊCH VỤ
# ==============================

elif menu == "✂️ Dịch vụ":

    st.header("✂️ Dịch vụ")

    st.info(
        "Sau này đây sẽ là nơi xem và quản lý "
        "toàn bộ các dịch vụ đã ghi nhận."
    )


# ==============================
# NHÂN VIÊN
# ==============================

elif menu == "👥 Nhân viên":

    st.header("👥 Quản lý nhân viên")

    st.info(
        "Sau này bạn sẽ có thể thêm, sửa, "
        "khóa và quản lý ID của từng nhân viên."
    )


# ==============================
# BÁO CÁO
# ==============================

elif menu == "📊 Báo cáo":

    st.header("📊 Báo cáo")

    st.info(
        "Sau này sẽ có báo cáo theo ngày, "
        "tháng và theo từng nhân viên."
    )


# ==============================
# CÀI ĐẶT
# ==============================

elif menu == "⚙️ Cài đặt":

    st.header("⚙️ Cài đặt")

    st.subheader("⚙️ Các thiết lập")

    st.write("👥 Quản lý nhân viên")
    st.write("💰 Cài đặt hoa hồng")
    st.write("🧾 Quản lý các khoản chi")
    st.write("🔐 Quản lý tài khoản và ID")
