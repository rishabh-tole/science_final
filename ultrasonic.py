import utime
from hcsro4 import HCSR04
import machine

class Security:

    def __init__(self):
        self._state = "DISARMED"
        self._ref_distance = 0
        self.sensor = HCSR04(trigger_pin=5, echo_pin=4)
        self.buzzer = machine.Pin(14, machine.Pin.OUT)
        self.light = machine.Pin(12, machine.Pin.OUT)
        self.button = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
        self.start = utime.ticks_ms()
        self.password = "hell0"
        

    def calibrate(self):
        self._ref_distance = self.sensor.distance_cm()
        
    def buzz(self):
        for x in range(50):
            self.buzzer.on()
            utime.sleep_ms(100)

    def call_the_police(self):
        print("calling the police...")
    """ FOR NOW NOT IMPLEMENTED"""

    def arm(self):
        self._state = "ARMED"
        self.light.on()

    def disarm(self):
        ans = input("whats the pass:")
        if ans == self.password:
            self._state = "DISARMED"
            self.light.off()
        else:
            print("wrong pass")

    while True:

        if self.button.value() == 0:
            self.start = utime.ticks_ms()
            if ticks_diff(itime.ticks_us(), self.start) > 1000:
                if self._state == "ARMED":
                    self.disarm()
                else:
                    self.arm()

        if self._state == "ARMED" and ticks_diff(itime.ticks_us(), self.start) > 500:
            self.calibrate()
            actual_dist =  self.sensor.distance_cm()

            if self._ref_distance*0.7 > actual_dist:
                self.buzz()
                self.call_the_police()


                





        


