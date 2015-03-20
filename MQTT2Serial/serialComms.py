import time, serial
import mosquitto

ser = serial.Serial("/dev/tty.usbmodem14211", 9600, timeout=2)


def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload)
    if msg.payload == "ON":
        ser.write("1")
    elif msg.payload == "OFF":
        ser.write("0")



client = mosquitto.Mosquitto("Chris")
client.connect("141.163.83.78")
client.subscribe("lights")
client.on_message = messageReceived
while True: 
    client.loop()

        
#    while True:
#    inputKey = raw_input("on/off")
#
#    if inputKey == "1":
#        ser.write("1")
#    elif inputKey == "0":
#        ser.write("0")
#    elif inputKey == "q":
#        ser.write("0")
#        break