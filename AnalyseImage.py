from PIL.ImageGrab import grabclipboard
from pytesseract import image_to_string, pytesseract
from pytesseract.pytesseract import tesseract_cmd
from time import sleep
from pyperclip import paste, copy



try:
	pytesseract.tesseract_cmd= r'D:/Programme/Tesseract-OCS/tesseract.exe'

	
	# img= Image.open(str(input("Image: ")))
	img = grabclipboard()
	PATH= "C:/Users/KYLIAN~1/AppData/Local/Temp/Paste6523.png"
	img.save(PATH, 'PNG')
	
	texte= image_to_string(PATH)
	copy(texte)
	paste()	
	print(f'__________\nOutput:\n{texte}\n__________')
	sleep(7)
	
except AttributeError:
	print("\nAttributeError: Need a picture")
	sleep(7)
	





