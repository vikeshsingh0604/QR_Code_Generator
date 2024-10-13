import qrcode
from PIL import Image
import qrcode.constants   
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4)

qr.add_data("https://www.linkedin.com/feed/")
qr.make(fit=True)
img= qr.make_image(fill_color="red",back_color="blue")
img.save("linkdin_profile")