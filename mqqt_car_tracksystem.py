from paho.mqqt import client

if connect(localhost, port=1883, keepalive=60, bind_addres=localhost) == True:
	print 'I have connected Bitch!'
else:
	print 'NOOOOO IM DEAD MAN'