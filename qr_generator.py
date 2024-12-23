import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
from datetime import datetime

# Title
st.title("Serial Number and QR Code Generator")

# Default values for year, month, and batch number
current_year = datetime.now().year
current_month = f"{datetime.now().month:02d}"  # Format as 2-digit month
default_batch_number = "M01"

# Inputs with default values
alpha_numeric = st.text_input("Enter Alphanumeric Number:")
year = st.text_input("Enter Year (YYYY):", value=str(current_year))
month = st.text_input("Enter Month (MM):", value=current_month)
batch_number = st.text_input("Enter Batch Number:", value=default_batch_number)
model = st.text_input("Enter Model:")

# Button to generate serial number and QR code
if st.button("Generate"):
    if alpha_numeric and year and month and batch_number and model:
        # Concatenate the serial number without hyphens and convert to uppercase
        serial_number = f"{alpha_numeric}{year}{month}{batch_number}{model}".upper()
        st.success(f"Generated Serial Number: {serial_number}")

        # Generate QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(serial_number)
        qr.make(fit=True)
        qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

        # Resize to 7cm x 7cm (300 DPI)
        qr_img = qr_img.resize((177, 177))  # 1.5cm = 177 pixels at 300 DPI


        # Display QR Code
        st.image(qr_img, caption="Generated QR Code (2cm x 2cm)", use_container_width=False)

        # Option to download QR Code
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.error("Please fill in all fields.")
    