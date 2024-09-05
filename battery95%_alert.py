import psutil
from plyer import notification
import time

def check_battery():
    battery=psutil.sensors_battery()
    if battery.percent>=92 and battery.power_plugged:
        notification.notify(
            title="Battery full",
            message="Your  battery is charged its Health part (95%). Please unplug the charger to stay safe!",
            timeout=()
        )

while True:
    check_battery()
    time.sleep(60) # check every 60 seconds