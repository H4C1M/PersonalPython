from gpiozero import Robot
import time
from evdev import InputDevice, categorize, ecodes

robot = Robot(left=(17,18), right=(27,22))
controller = InputDevice("/dev/input/event0")

# Mapping
up = 46
down = 32
left = 18
right = 33

xBtn = 35
yBtn = 23
aBtn = 34
bBtn = 36

start = 24
select = 49

lTrigger = 37
rTrigger = 50

# Speeds
move = 0.75
turn = 0.5

# Controller Code
print(controller)
print()

for event in controller.read_loop():
    if event.value == 0:
        robot.stop()
    elif event.value == 1:
        if event.code == start:
            break
        elif event.code == select:
            temp = up
            up = down
            down = temp

        elif event.code == lTrigger:
            if turn > 0.25:
                move -= 0.25
                turn -= 0.25
        elif event.code == rTrigger:
            if move < 1:
                move += 0.25
                turn += 0.25

    if event.value == 1 or event.value == 2:
        if event.code == up:
            robot.forward(move)
        elif event.code == down:
            robot.backward(move)
        elif event.code == left:
            robot.left(turn)
        elif event.code == right:
            robot.right(turn)

        elif event.code == xBtn:
            print('X')
            # nothing for now
        elif event.code == yBtn:
            print('Y')
            # nothing for now
        elif event.code == aBtn:
            print('A')
            # nothing for now
        elif event.code == bBtn:
            robot.stop()