import cv2
import numpy as np
import os
from pytesseract import pytesseract
import pypdfium2 as pdfium

def text_extract(path):
    ext = os.path.splitext(path)[1]
    # if pdf then convert to image
    if ext == '.pdf':
        pdf = pdfium.PdfDocument(path)
        page = pdf.get_page(0)
        img = page.render_to(pdfium.BitmapConv.pil_image)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    else:
        img = cv2.imread(path)
    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    # If os is windows
    if os.name == 'nt':
        pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe" 
    custom_config = r'--oem 3 --psm 4'
    text = pytesseract.image_to_string(img, config=custom_config,lang='eng')
    return text
