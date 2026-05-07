import streamlit as st

from utils.ocr import extract_text
from utils.parser import parse_text
from utils.solar import calculate_solar
from utils.excel_writer import save_to_excel

# Streamlit page title
st.title("⚡ Solar Bill Analyzer")

# Upload bill image
uploaded_file = st.file_uploader(
    "Upload Electricity Bill",
    type=["jpg", "png", "jpeg"]
)

# When file uploaded
if uploaded_file:

    st.success("File uploaded successfully!")

    # STEP 1: OCR Text Extraction
    text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Text")
    st.text(text)

    # STEP 2: Parse important data
    data = parse_text(text)

    st.subheader("📊 Extracted Data")
    st.write(data)

    # STEP 3: Solar calculation
    solar_data = calculate_solar(
        data["units"],
        data["days"]
    )

    st.subheader("☀️ Solar Recommendation")
    st.write(solar_data)

    # STEP 4: Save Excel
    file_path = save_to_excel(data, solar_data)

    st.success("Excel report generated!")

    # Download button
    with open(file_path, "rb") as f:

        st.download_button(
            label="📥 Download Excel Report",
            data=f,
            file_name="solar_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )