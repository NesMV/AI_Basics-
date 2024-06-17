import cv2
import pytesseract
from openvino.runtime import Core

class OCRProcessor:
    def __init__(self, tesseract_cmd_path):
        self.core = Core()
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path

    def recognize_text(self, image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        result = pytesseract.image_to_string(gray)
        return result
    
