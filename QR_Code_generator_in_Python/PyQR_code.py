import pyqrcode

# String to represent the QR code
str_ = "http://idoston.com/python-development"

# Generate QR Code
url = pyqrcode.create(str_)

# Create and save the svg file with name idostoncom
url.svg("idostoncom.svg", scale=8)
