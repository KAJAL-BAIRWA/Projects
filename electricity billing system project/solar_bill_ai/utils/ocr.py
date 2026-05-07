import pytesseract
from PIL import Image

# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(file):

    """
    Extract text from uploaded image
    """

    try:

        # Open image
        image = Image.open(file)

        # OCR text extraction
        text = pytesseract.image_to_string(image)

        return text

    except Exception as e:

        return f"OCR Error: {str(e)}"