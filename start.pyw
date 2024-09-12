import ctypes, time
from schedule import every, repeat, run_pending


@repeat(every(3).minutes)
def job():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/omalay.jpg" , 0)

while True:
    run_pending()
    time.sleep(1)


