# Removing existing image files
import glob
import os
removing_files = glob.glob('*.png')
for i in removing_files:
    os.remove(i)
if os.path.exists(".png"):
  os.remove(".png")

# Package imports
import qrcode
from qrcode.constants import ERROR_CORRECT_L
import js2py

qr = qrcode.QRCode(
  version=3,
  error_correction=ERROR_CORRECT_L,
  box_size=3,
  border=3
)

# Console prints
print('''
HELPFUL TIP: To paste text into the console from your clipboard, press:
   • Ctrl + Shift + V
      or
   • Command ⌘  + Shift + V

''')

link = str(input("Enter the link/text you want the QR code to refer to: "))

# QR code generation
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
file_name= input("Enter the desired name for the file: ") + ".png"

# Check if file name is too long
if len(file_name) > 154:
  print("")
  print("ERROR: The file name you entered exceeds the limit of 150 characters. Please run the code again.")
  quit()
  
# Saving the image
img.save(file_name)

# Console prints
print("")
print("Your QR code is saved in PNG image format and is named as",file_name)
print("You can view it by clicking 'show files', then clicking on " + file_name)
print('''
To download the image, view the image, then right click the image, then click the 'download' or 'save as' option, depending on your browser.


To generate another QR code, run this repl again!
''')