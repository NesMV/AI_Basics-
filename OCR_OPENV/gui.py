import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from ocr_processor import OCRProcessor

class OCRApp:
    def __init__(self, root, ocr_processor):
        self.root = root
        self.ocr_processor = ocr_processor
        self.root.title("OCR con OpenVINO")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.load_button = tk.Button(self.frame, text="Cargar Imagen", command=self.load_image)
        self.load_button.pack(side=tk.LEFT, padx=10)

        self.text_area = ScrolledText(self.root, wrap=tk.WORD, width=50, height=15)
        self.text_area.pack(pady=20)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            text = self.ocr_processor.recognize_text(file_path)
            self.text_area.insert(tk.END, text)

# Punto de entrada
if __name__ == "__main__":
    tesseract_cmd_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Actualiza esta ruta según tu sistema
    ocr_processor = OCRProcessor(tesseract_cmd_path)
    
    root = tk.Tk()
    app = OCRApp(root, ocr_processor)
    root.mainloop()
