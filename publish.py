import sys
import requests 
import json
import time
try:
    import paho.mqtt.publish as publish
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.publish"
    import os
    import inspect
    from delay import delayed
    import time
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.publish as publish

door_status = False
def close_door():
    msgs = [{'topic':"devices/Edison/aaaa::212:4b00:939:3607/gpio/2/set", 'payload':"0"}, ("devices/Edison/aaaa::212:4b00:939:3607/gpio/2/toggle", "0", 0, False)]
    msgs_1 = [{'topic':"devices/Edison/aaaa::212:4b00:939:3607/gpio/1/set", 'payload':"1"}, ("devices/Edison/aaaa::212:4b00:939:3607/gpio/3/set", "1", 0, False)]
    publish.multiple(msgs, hostname="100.100.144.205")
    publish.multiple(msgs_1, hostname="100.100.144.205")
    


def open_door():
    msgs = [{'topic':"devices/Edison/aaaa::212:4b00:939:3607/gpio/2/set", 'payload':"1"}, ("devices/Edison/aaaa::212:4b00:939:3607/gpio/3/set", "1", 0, False)]
    msgs_1 = [{'topic':"devices/Edison/aaaa::212:4b00:939:3607/gpio/1/set", 'payload':"0"}, ("devices/Edison/aaaa::212:4b00:939:3607/gpio/3/set", "0", 0, False)]
    publish.multiple(msgs, hostname="100.100.144.205")
    publish.multiple(msgs_1, hostname="100.100.144.205")
    
if __name__ == "__main__":
    x = "1"
    while True:
        response = requests.get('http://orangedrive.ru/gate?rq=car_getstate') 
        json_data = json.loads(response.text)
        print x
        time.sleep(0.5)
        if x != response.text[-4]:
            if response.text[-4] == "0":
                close_door()
                x = response.text[-4]
            elif response.text[-4] == "1":
                open_door()
                x = response.text[-4]
        else:
            print 'smth '
            