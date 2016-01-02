import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')

# start an iterator thread so
# serial buffer doesn't overflow
iter = pyfirmata.util.Iterator(board)
iter.start()

dirA = board.getpin('d:12:o')
dirB  = board.getpin('d:13:o')
pwmA =  board.getpin('d:3:p')
pwmB = board.getpin('d:11:p')
breakA = board.getpin('d:9:o')
breakB = board.getpin('d:8:o')

class Motor():
    def __init__(self):
        self.speedA = 100
        self.speedB = 100
    def moveA(self, direction, speed):
        self.speedA = speed
        if speed == 0:
            breakA.write(1)
        else:
            breakA.write(0)
        if speed > 0:
            pwmA.write(speed)


