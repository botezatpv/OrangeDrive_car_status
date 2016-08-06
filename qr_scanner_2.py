import qrtools
from qrtools import QR
myCode = QR()
print myCode.decode_webcam()
print myCode.data
print myCode.data_type
print myCode.data_to_string()