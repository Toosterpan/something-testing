import qrcode

while True:
    a=input("Please enter the qr code ")
    img= qrcode.make(a)
    b=input("Save image as ")
    img.save(b,"PNG")
