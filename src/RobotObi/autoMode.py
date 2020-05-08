from gpiozero import Robot, DistanceSensor
import time

robot = Robot(left=(17,18), right=(27,22))
ds = DistanceSensor(echo=24, trigger=23)

while True:
    dist = ds.distance * 100
    dist = round(dist, 3)
    print(dist)

    if dist > 10:
        robot.forward(0.25)
        time.sleep(0.5)
    else:
        robot.right()
        time.sleep(0.5)

        robot.forward(0.5)
        time.sleep(0.5)

        robot.right()
        time.sleep(0.5)

    time.sleep(0.1)

''' longer version that shows what simpler stuff below is actually doing (or could be doing)
trigger = OutputDevice(23)
echo = InputDevice(24)

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
    print('Wacky Going Down')
    time.sleep(1)
'''