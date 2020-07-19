from PIL import Image 
import pytesseract



im=Image.open("test_tesseract/image2.jpg")
text=pytesseract.image_to_string(im,lang='eng')
print(text)