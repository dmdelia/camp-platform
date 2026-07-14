# Components connected to the emulated Endo "ENDO-FRED":
#   - Arm Bowden Servo ("arm_left")
#   = Leg Bowden Servo ("leg_right")
#   - Ear Servo

''' IMPORTS '''
import asyncio
import json
import socket

def clamp(value=float or int, min_value=float or int, max_value=float or int):
    return max(min_value, min(value, max_value))

class arm_servo():
    def __init__(self):
        self.__servo_state_degrees = 120
        self.__servo_max_degree = 180
        self.__servo_min_degree = 90
        self.__tick_rate_state = 1

    def servo_state_degrees(self):
        return self.__servo_state_degrees

    def update_servo_tick(self):
        if self.__servo_state_degrees + 1 == self.__servo_max_degree or self.__servo_state_degrees - 1 == self.__servo_min_degree:
            self.__tick_rate_state *= -1

        self.__servo_state_degrees = self.__servo_state_degrees + (1 * self.__tick_rate_state)

        # clamp for safety 
        self.__servo_state_degrees = clamp(self.__servo_state_degrees, self.__servo_min_degree, self.__servo_max_degree)

async def rechne_loop(servo_obj):
    while True:
        await asyncio.sleep(0.1)
        servo_obj.update_servo_tick()

async def sende_loop(servo_obj):
    camp_hub = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    while True:
        __got_angle = servo_obj.servo_state_degrees()

        built_dict = {
            "source": "ENDO-FRED",
            "servo": "arm_left",
            "angle": __got_angle
                    }
        
        encoded_json = json.dumps(built_dict).encode()
        camp_hub.sendto(encoded_json, ("127.0.0.1", 6422))
        await asyncio.sleep(0.1)

async def main():
    main_linker_arm = arm_servo()
    
    async with asyncio.TaskGroup() as tg:
        tg.create_task(rechne_loop(main_linker_arm))
        tg.create_task(sende_loop(main_linker_arm))

asyncio.run(main())
