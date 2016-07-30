from paho.mqqt import client

if connect(host, port=1883, keepalive=60, bind_addres="") == True:
	print 'I have connected Bitch!'
else:
	print 'NOOOOO IM DEAD MAN'