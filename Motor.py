import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')

# start an iterator thread so
# serial buffer doesn't overflow
iter = pyfirmata.util.Iterator(board)
iter.start()


direction = [board.getpin('d:12:o'),board.getpin('d:13:o')]
pwm = [board.getpin('d:3:p'), board.getpin('d:11:p')]
breaks = [board.getpin('d:9:o'), board.getpin('d:8:o')]

MOTOR_L = 0
MOTOR_R = 1
MOTOR_UP = 2

class Motor():
    def __init__(self, dirPin, pwmPin, breakPin):
        self.speed = 0
        self.direction = 1
        self.dirPin = dirPin
        self.pwmPin = pwmPin
        self.breakPin = breakPin
    def move(self, speed):
        if speed == 0:
            self.breakPin.write(1)
        else:
            self.breakPin.write(0)
        if speed > 0:
            self.dirPin.write(0)
            self.pwmPin(speed)
        elif speed < 0:
            self.dirPin.write(1)
            self.pwmPin(abs(speed))


class Propulsion():
    def __init__(self):
        self.motorA = Motor(direction[MOTOR_L], pwm[MOTOR_L], breaks[MOTOR_L])
        self.motorB = Motor(direction[MOTOR_R], pwm[MOTOR_R], breaks[MOTOR_R])
        #self.motorC = Motor(direction[0], pwm[0], breaks[0])
    def foward(self, speed = 100):
        self.motorA.move(speed)
        self.motorB.move(speed)
    def backward(self, speed = 100):
        self.motorA.move(-speed)
        self.motorB.move(-speed)
    def stop(self):
        self.motorA.move(0)
        self.motorB.move(0)
    def up(self):
        raise RuntimeWarning("not implemented yet")
    def down(self):
        raise RuntimeWarning("not implemented yet")
    def freeze(self):
        self.motorA.move(0)
        self.motorB.move(0)
        raise RuntimeWarning("not implemented yet for up/down motor")

prop = Propulsion()
prop.foward()






