#!/usr/bin/env python

import serial
import time
from pysine import sine

class Servo:
    def __init__(self):
        self.connection = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)

    def _send_servo_command(self, command):
        checksum = 0
        for b in command:
            checksum = checksum + b
        checksum = 0xFF - (checksum % 0xFF)
        
        to_write = [0x55, 0x55, *command, checksum]
        self.connection.flushInput()
        self.connection.flushOutput()
        self.connection.write(to_write)

    def set_servo_position(self, position):
        servo_id = 1
        command_id = 1
        command_length = 7

        self._send_servo_command([servo_id, command_length, command_id, position&0xFF, position>>8, 0, 0])

class Booper:
    DOWN_POSITION = 490
    UP_POSITION = 500
    RESET_POSITION= 1000

    def __init__(self):
        self.servo = Servo()
        self.last_time = time.time()

    def _delay(self, delay_time, play_tone = False):
        next_time = self.last_time + delay_time
        sleep_time = next_time - time.time()
        #print(f'last_time={self.last_time} delay_time={delay_time} time.clock={time.clock()} next_time={next_time} sleep_time={sleep_time}')

        self.last_time = next_time

        if(sleep_time > 0):
            if(play_tone):
                sine(duration = sleep_time + 0.03)
            else:
                time.sleep(sleep_time)

    def boop(self, wait_time = 0, down_time = 0.1):
        #time.sleep(wait_time)
        self._delay(wait_time)
        self.servo.set_servo_position(self.DOWN_POSITION)
        #time.sleep(down_time)
        self._delay(down_time, play_tone = True)
        self.servo.set_servo_position(self.UP_POSITION)

    def ready(self):
        self.servo.set_servo_position(self.UP_POSITION+20)
        time.sleep(1)

    def reset(self):
        self.servo.set_servo_position(self.RESET_POSITION)

b = Booper()
#b.ready()

b.boop()        # Restart
b.boop(.8)
b.boop(.8)
b.boop(.8)
b.boop(.8, 2.8) # Steps, triangles
b.boop(.5)      # Platform
b.boop(.8)
b.boop(.8)
b.boop(.8)
b.boop(.8, 1.8)   # Steps
b.boop(.9)
b.boop(.7)
b.boop(1.2)
b.boop(.8, .4)
b.boop(.6)
b.boop(.7, .6)
b.boop(.9)
b.boop(1.1, .8)   # Lowering spikes
b.boop(.7)
b.boop(.4)
b.boop(.5)
b.boop(.5)
b.boop(.8)
b.boop(.4)
b.boop(.6)
b.boop(.4)
b.boop(.8, .3)  # Flappy-bird
b.boop(.8, .6)
b.boop(1.3, .6)
b.boop(.7, .4)
b.boop(.8, .9)
b.boop(.9, .4)
b.boop(1.3, .6)
b.boop(1.1, .3)
b.boop(1.1, .3)
b.boop(1.1, .3) # End of flappy-bird


#b.reset()
