import time
from plyer import notification

while True:
    notification.notify(
        title="Drink Water",
        message='Drink water to keep yourself hydrated',
        app_icon=r'C:\Users\rv\VSCode\Projects\WaterNotify\glass.ico',
        timeout=2)
    time.sleep(60*60)
