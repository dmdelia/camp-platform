from rich import print as printr
from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live

import random
import time

cls = lambda: print("\033c\033[3J", end='')
cls()
cli_layout = Layout()
cli_layout.split_row(Layout(name="no1"), Layout(name="no2"))

def get_percentage(x): 
    return 1.1 * x - 98

with Live(cli_layout, refresh_per_second=10):

    while True:
        # right now receiving: (in demo)
        received_dict = {
            'source': 'ENDO-FRED',
            'servo': 'arm_left',
            'angle': ''
        }
        
        randomnr = random.randint(90, 180)
        received_dict['angle'] = randomnr

        # 1. Telemetry Panel 
        text_telemetry = f"Left Arm servo State: {received_dict['angle']}°"
        align_telemetry = Align.center(text_telemetry, vertical="middle")
        cli_layout["no1"].update(Panel(align_telemetry, title="[bold]Telemetrie[/]", border_style="#FF5F1F", height=3))

        # 2. Battery Panel
        random_percent = int(get_percentage(randomnr)) # just for visualisation purpose, no simulated battery yet
        text_battery = f"Endo Central Brain Battery: {random_percent} %"
        align_battery = Align.center(text_battery, vertical="middle")
        cli_layout["no2"].update(Panel(align_battery, title="[bold]Battery[/]", border_style="#1FFF75", height=3))

        time.sleep(0.1)
