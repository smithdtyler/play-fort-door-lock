# Write your code here :-)

import sparkfun_qwiickeypad
import time
import board
import sys
import digitalio
import i2c_button

# IO Pin for the lock
lockpin = board.IO15
elock  = digitalio.DigitalInOut(lockpin)
elock.direction = digitalio.Direction.OUTPUT

# Create bus object using the board's I2C port
i2c = board.I2C()

#print(dir(i2c_button))

exitbtn = i2c_button.I2C_Button(i2c)

#print(dir(sparkfun_qwiickeypad))

#keypad = sparkfun_qwiickeypad.I2CDevice(i2c, 0x4B)  # default address is 0x4B
# ^ This method gets a generic i2c device. 

dadcode = ['1','2','3','4','5']

keypad = sparkfun_qwiickeypad.Sparkfun_QwiicKeypad(i2c)
buf = []
timeout = 3.0
accruedtime = 0.0

while True:
    elock.value = True
    keypad.update_fifo()
    exitstatus = exitbtn.status
    if(exitstatus.is_pressed):
        print("Exit Button Pressed")
        buf.clear()
        elock.value = False
        time.sleep(5.0)
    button = keypad.button
    if(button != 0):
        accruedtime = 0
        charb = chr(button)
        print(charb)
        buf.append(charb)
        if(len(buf) >= 5):
            print(buf)
            if(buf == dadcode):
                print("correct!")
                elock.value = False
                time.sleep(5.0)
            else:
                print("wrong!")
            buf.clear()
    time.sleep(0.1)
    accruedtime += 0.1
    if (accruedtime >= timeout):
        accruedtime = 0
        buf.clear()
