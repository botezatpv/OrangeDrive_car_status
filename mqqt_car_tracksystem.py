import paho.mqtt.client as mqtt

class MqttClient:

	def __init__(self):
		self.HOSTNAME = "10.0.0.49"
		self.PORT = 1883
		self.KEEPALIVE = 60
		self.client = mqtt.Client()

	# The callback for when the client receives a CONNACK response from the server
	# Subscribe on topic when client receives a CONNACK response from the server
	def on_connect(self, client, userdata, flags, rc):
	    print("Connected with result code "+str(rc))
	    self.client.subscribe("#")

	# The callback for when a PUBLISH message is received from the server.
	def on_message(self, client, userdata, msg):
	    print(msg.topic+" "+str(msg.payload))

	def main(self):    
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		self.client.connect(self.HOSTNAME, self.PORT, self.KEEPALIVE)
		self.client.loop_forever()

if __name__ == "__main__":
	mqqt = MqttClient()
	mqqt.main()

