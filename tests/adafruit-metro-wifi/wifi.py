# Write your code here :-)
import board
import digitalio
import time
import wifi
import time
import ipaddress
import socketpool
import ssl
# Requires adafruit-circuitpython-bundle-7.x-mpy-20230128\lib\adafruit_requests.mpy in the lib dir in CIRCUITPY
import adafruit_requests

# Example from https://gist.github.com/todbot/7534740779cd64a2ce636d14ecb6e5af

led = digitalio.DigitalInOut(board.LED)

led.direction = digitalio.Direction.OUTPUT

print("Hello, world")

for network in wifi.radio.start_scanning_networks():
    print(network, network.ssid, network.channel)
wifi.radio.stop_scanning_networks()

print("joining network...")
print(wifi.radio.connect(ssid="XXXXXXXXX",password="ZZZZZZZZZ"))

print("my IP addr:", wifi.radio.ipv4_address)

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(0.5)
