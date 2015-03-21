#import modules
import time, serial
import mosquitto

#declare serial connection
ser = serial.Serial("/dev/tty.usbmodem14211", 9600, timeout=2)

#function to run when message received
def messageReceived(broker, obj, msg):
    global client
    print("Message " + msg.topic + " containing: " + msg.payload)
    #if message received is "ON" then send "1" over serial port, otherwise if it is "OFF" then send a 0 to the arduino instead
    if msg.payload == "ON":
        ser.write("1")
    elif msg.payload == "OFF":
        ser.write("0")

#connect to client and subscribe to listen for messages
client = mosquitto.Mosquitto("Chris")
client.connect("141.163.83.78")
client.subscribe("lights")
client.on_message = messageReceived

#listen for messages
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