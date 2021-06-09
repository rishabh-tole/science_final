from hcsro4 import HCSR04
import machine
import utime
class Security:

    def __init__(self):
        self._state = "DISARMED"
        self._ref_distance = 0
        self.sensor = HCSR04(trigger_pin=5, echo_pin=4)
        self.buzzer = machine.Pin(14, machine.Pin.OUT)
        self.light = machine.Pin(12, machine.Pin.OUT)
        self.button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
        self.password = "hell0"
        print("imports are fine")
        

    def calibrate(self):
        self._ref_distance = self.sensor.distance_cm()
        
    def buzz(self):
        for x in range(50):
            self.buzzer.on()
            utime.sleep_ms(100)
            self.buzzer.off()

    def call_the_police(self):
        print("calling the police...")
    """ FOR NOW NOT IMPLEMENTED"""

    def arm(self):
        self._state = "ARMED"
        self.light.on()

    def disarm(self):
        ans = input("whats the pass:")
        #for now
        if ans == self.password:
            self._state = "DISARMED"
            self.light.off()
        else:
            print("wrong pass")

    def start(self):
        while True:


            if int(self.button.value()) == 0:
                if self._state == "ARMED":
                    self.disarm()
                else:
                    self.arm()
                utime.sleep_ms(500)

            if self._state == "ARMED":
                self.calibrate()
                actual_dist =  self.sensor.distance_cm()

                if self._ref_distance*0.7 > actual_dist:
                    self.buzz()
                    self.call_the_police()


                





        


