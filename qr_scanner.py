from qrtools import QR
class ScanFromCamera:
	def scan(self):
		myCode = QR()
		print myCode.decode_webcam()
if __name__=="__main__":
	sc = ScanFromCamera
	sc.scan()