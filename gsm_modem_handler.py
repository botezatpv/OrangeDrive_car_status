#!/usr/bin/env python
from __future__ import print_function
import logging
import paho.mqtt.publish as publish
from gsmmodem.modem import GsmModem

class GsmModemHandler:
	#Initializing PORT, BAUDRATE, PIN, HOSTNAME
	def __init__(self):
		self.PORT = '/dev/ttyUSB2'
		self.BAUDRATE = 115200
		self.PIN = None # SIM card PIN (if any)
		self.HOSTNAME = "10.0.0.4"

	#Get and reply sms	
	def handleSms(self, sms):
	    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))
	    print('Replying to SMS...')
	    sms.reply(u'SMS received: "{0}{1}"'.format(sms.text[:20], '...' if len(sms.text) > 20 else ''))
	    print('SMS sent.\n')
	    publish.single("hello/","Hello", hostname=self.HOSTNAME)
	    return sms.text
	    
	#Connecting to gsm device    
	def main(self):
	    print('Initializing modem...')
	    # Uncomment the following line to see what the modem is doing:
	    #logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
	    modem = GsmModem(self.PORT, self.BAUDRATE, smsReceivedCallbackFunc=self.handleSms)
	    modem.smsTextMode = False 
	    modem.connect(self.PIN)
	    print('Waiting for SMS message...')    
	    try:    
	        modem.rxThread.join(2**31) # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
	    finally:
	        modem.close();

if __name__ == '__main__':
	gsm = GsmModemHandler()
	gsm.main()