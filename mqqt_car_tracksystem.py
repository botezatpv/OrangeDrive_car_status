from paho.mqtt import client


def on_connect(client, userdata, rc):  
    print("Connected with result code: %s" % rc)
    client.subscribe("devices/#")

def on_message(client, userdata, msg):  
    print("%s: %s" % (msg.topic, msg.payload))
    recived_vals = {{"ability": "N"}, {"last_seen":"3"}, {"last_sequience": "0"}, {"parent": "fe80::212:4b00:939:2d5d"}}
    print recived_vals
    #tokens = msg.split('/')

def main():  
    subscriber = client.Client()
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message

    subscriber.connect("100.100.144.205")
    subscriber.loop_forever()

if __name__ == "__main__":  
    main()