import io
import qrcode
import streamlit as st
import zxingcpp
from PIL import Image


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PragyanAI - QR Code Generator & Decoder",
    page_icon="🔳",
    layout="centered"
)


# ============================================================
# HEADER
# ============================================================

st.title("PragyanAI- QR Code Generator & Decoder")

st.write(
    "Generate a QR Code from a URL or information, "
    "display it, download it, and decode it."
)

st.info(
    "Built with Python + Streamlit + Pillow + QRCode + ZXing-C++. "
    "OpenCV is not used."
)


# ============================================================
# SESSION STATE
# ============================================================

if "qr_bytes" not in st.session_state:
    st.session_state.qr_bytes = None

if "generated_data" not in st.session_state:
    st.session_state.generated_data = ""


# ============================================================
# SECTION 1 — GENERATE QR CODE
# ============================================================

st.header("1️. Generate QR Code")

data = st.text_area(
    "Enter URL / Information",
    placeholder=(
        "Example:\n"
        "https://www.pragyanai.com\n\n"
        "or any text/information"
    ),
    height=120
)
