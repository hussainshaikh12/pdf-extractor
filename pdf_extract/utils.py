import cv2
import numpy as np
import os
from pytesseract import pytesseract
import pypdfium2 as pdfium

def crop_image(filename, pixel_value=255):
    gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    crop_rows = gray[~np.all(gray == pixel_value, axis=1), :]
    cropped_image = crop_rows[:, ~np.all(crop_rows == pixel_value, axis=0)]
    return cropped_image

def text_extract(path):
    ext = os.path.splitext(path)[1]
    # if pdf then convert to image
    if ext == '.pdf':
        pdf = pdfium.PdfDocument(path)
        page = pdf.get_page(0)
        pil_image = page.render_to(pdfium.BitmapConv.pil_image)
    else:
        pil_image = crop_image(path)
    if os.name == 'nt':
        pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe" 
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(pil_image, config=custom_config,lang='eng')

    return text