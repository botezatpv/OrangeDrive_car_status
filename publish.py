import sys
try:
    import paho.mqtt.publish as publish
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.publish"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.publish as publish

msgs = [{'topic':"devices/Edison/aaaa::212:4b00:939:3607/gpio/2/toggle", 'payload':"0"}, ("devices/Edison/aaaa::212:4b00:939:3607/gpio/2/toggle", "1", 0, False)]
publish.multiple(msgs, hostname="100.100.144.205")
