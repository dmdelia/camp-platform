import asyncio
import json
import socket

from random import randint as randint

from rich import print as printr
from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live


# Functions for simple conversion, due to it being a Key Element of the Communication

cls = lambda: print("\033c\033[3J", end='')

def dictionary_to_json(python_dict):
    __json_string = json.dumps(python_dict, indent=2)
    return(__json_string)

def json_to_dictionary(json_string):
    __python_dict = json.loads(json_string)
    return(__python_dict)

cli_layout = Layout()
cli_layout.split_row(Layout(name="no1"), Layout(name="no2"))



# Socket Server Setup INET (Telemetrie)

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind(('127.0.0.1', 6422))
socket_server.setblocking(False)

# Initializing 'global' Variables
global newest_INET
newest_INET = None
    
async def update_INET():
    while True:
        loop = asyncio.get_running_loop()
        INET_data = await loop.sock_recv(socket_server, 1024)
        global newest_INET
        newest_INET = INET_data.decode()
        await asyncio.sleep(0.1)

async def update_BLUETOOTH():
    while True:
        __temp = 1 # simple "logic" to avoid any issues with using the "..." or stuff
        if __temp == 2:
            break
        await asyncio.sleep(1)
    return __temp

def update_CLI():

    def get_percentage(x): 
        return 1.1 * x - 98
    
    global cli_layout

    # 0. Receiving (in demo)
    received_dict = json_to_dictionary(newest_INET) 


    # 1. Telemetry Panel 
    text_telemetry = f"Left Arm servo State: {received_dict['angle']}°"
    align_telemetry = Align.center(text_telemetry, vertical="middle")
    cli_layout["no1"].update(Panel(align_telemetry, title="[bold]Telemetrie[/]", border_style="#FF5F1F", height=3))

    # 2. Battery Panel
    random_percent = int(get_percentage(received_dict['angle'])) # just for visualisation purpose, no simulated battery yet
    text_battery = f"Endo Central Brain Battery: {random_percent} %"
    align_battery = Align.center(text_battery, vertical="middle")
    cli_layout["no2"].update(Panel(align_battery, title="[bold]Battery[/]", border_style="#1FFF75", height=3))


async def show_latest_telemetry():
    while True:
        if newest_INET:
            update_CLI()
            await asyncio.sleep(0.1)
        else:
            await asyncio.sleep(0.5)

async def main():

    with Live(cli_layout, refresh_per_second=10):

        async with asyncio.TaskGroup() as tg:
            tg.create_task(update_INET())
            tg.create_task(show_latest_telemetry())
            
            # tg.create_task(update_BLUETOOTH())
            # no calling of update_BLUETOOTH yet cuz not realized yet

if __name__ == "__main__":
    asyncio.run(main())


