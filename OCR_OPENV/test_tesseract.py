import pytesseract
from PIL import Image

# Especificar la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Asegúrate de tener una imagen de prueba en el directorio actual
image_path = 'C:/Users/nesim/Documents/10mo Semestre/IA/LAST CHANCE/OCR_OPENV/test_image.png'

# Abre la imagen usando PIL
image = Image.open(image_path)

# Realiza el OCR en la imagen
text = pytesseract.image_to_string(image)

# Imprime el texto reconocido
print(text)
