# Write your code here :-)
import board
import digitalio
import time
# Requires adafruit-circuitpython-bundle-7.x-mpy-20230128\lib\adafruit_ahtx0.mpy in the lib dir in CIRCUITPY
import adafruit_ahtx0

led = digitalio.DigitalInOut(board.LED)

led.direction = digitalio.Direction.OUTPUT

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)


print("Hello, world")

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(0.5)
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
