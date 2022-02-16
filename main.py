import vgamepad as vg
import time
import pygame
from inputs import get_gamepad
import math
import threading

gamepad = vg.VX360Gamepad()

autopilotas = 0
throttle = 0


class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def init(self):
        self.RightTrigger = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
        x = self.RightTrigger
        return [x]



    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1

read(self)

if autopilotas == 0:
    gamepad.right_trigger_float()
else:
    gamepad.right_trigger_float(throttle)