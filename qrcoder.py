import qrcode

data = input("Enter information: ")
print("1")

def from_data_to_qrcode(data):
    qrname = data.split("/")[2]
    print(qrname)
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_name = f'QR/{qrname}.png'
    print(file_name)
    img.save(file_name)

from_data_to_qrcode(data)