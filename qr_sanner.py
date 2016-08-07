import cv2.cv as cv
import zbar
class ScanQr:
	#initialazing variables
	def __init__(self, frame, set_zbar, set_width = 100.0/100, set_height = 90.0/100):
		self.set_width = set_width
		self.set_height = set_height
		self.coord_x = int(frame.width * (1 - self.set_width)/2)
		self.coord_y = int(frame.height * (1 - self.set_height)/2)
		self.width = int(frame.width * self.set_width)
		self.height = int(frame.height * self.set_height)
		self.frame = frame

	def scanner_procces(self):
		get_sub = cv.GetSubRect(self.frame, (self.coord_x+1, self.coord_y+1, self.width-1, self.height-1))
		cv.Rectangle(self.frame, (self.coord_x, self.coord_y), (self.coord_x + self.width, self.coord_y + self.height), (255,0,0))

	    cm_im = cv.CreateImage((get_sub.width, get_sub.height), cv.IPL_DEPTH_8U, 1)
		cv.ConvertImage(get_sub, cm_im)

		image = zbar.Image(cm_im.width, cm_im.height, 'Y800', cm_im.tostring())
		set_zbar.scan(image)

		for symbol in image:
			print '\033[1;32mResult : %s symbol "%s" \033[1;m' % (symbol.type,symbol.data)

		cv.ShowImage("webcame", frame)
		cv.WaitKey(10)


if __name__ == "__main__":
	#set up our stuff
	cv.NamedWindow("webcame", cv.CV_WINDOW_AUTOSIZE)
	capture = cv.CaptureFromCAM(-1)
	set_zbar = zbar.ImageScanner()

	while True:
		frame = cv.QueryFrame(capture)
		sQr = ScanQr(frame = frame, set_zbar = set_zbar)
		sQr.scanner_procces()
