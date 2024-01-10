# Note ---- The image you wish to create a QRcode for must be in the same directory/folder that this program is in.

import qrcode

data = 'QR Code using make() function'
img = qrcode.make(data)
img.save('MyQRCode1.png')
