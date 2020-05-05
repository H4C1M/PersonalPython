from gpiozero import Robot, DistanceSensor, DistanceSensorNoEcho, OutputDevice, InputDevice
import time

'''method1
# Set-up
ds = DistanceSensor(echo=18, trigger=16)

# Get Constant Data Values

while True:
        print('Distance: ' + ds.distance * 100)
        time.sleep(1)
'''

trigger = OutputDevice(16)
echo = InputDevice(18)

pulse_start = 0
pulse_end = 0

try:
    while True:
        trigger.on()
        time.sleep(0.00001)
        trigger.off()

        while not echo.is_active:
            pulse_start = time.time()

        while echo.is_active:
            pulse_end = time.time()

        distance = 34300 * ((pulse_end - pulse_start)/2)
        distance *= 100

        print('Distance: ' + str(distance))
except DistanceSensorNoEcho:
    print('Nothing Found, Wait')
    time.sleep(1)
except:
    print('Wacky Shit Going Down')
    time.sleep(1)
