import qrcode
from qrcode.image.pil import PilImage
# Prompt the user ----------------------------------------------------------
url = input("Enter the url: ").strip()
if not url:
    raise ValueError("URL cannot be empty.")
file_path = r"C:\Users\MUI_Byron\OneDrive\Desktop\qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print("HERE'S YOUR QR CODE! :)")
print(f"Saved to: {file_path}")

