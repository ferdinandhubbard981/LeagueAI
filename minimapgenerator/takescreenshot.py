import time
from PIL import ImageGrab
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

x = 0
time.sleep(10)
ImageGrab.grab().save("bluekaynexample.jpg", "JPEG")

while True:
    break
    x += 1
    ImageGrab.grab().save("minimap" + str(x) + ".jpg", "JPEG")
    print(x)
    time.sleep(5)
