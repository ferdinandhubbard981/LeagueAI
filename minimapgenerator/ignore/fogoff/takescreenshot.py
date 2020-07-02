import time
from PIL import ImageGrab
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

x = 23
while True:
    x += 1
    ImageGrab.grab().save("minimap" + str(x) + ".jpg", "JPEG")
    print(x)
    time.sleep(5)
