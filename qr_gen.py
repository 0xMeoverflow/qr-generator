import qrcode

def qr_gen(from_text):

    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, border = 4, box_size = 10)
    qr.make(fit = True)
    qr.add_data(text)

    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('output.png')

text = input('Text to QR\n')
qr_gen(text)
