import time
from PIL import ImageGrab
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

x = 0
time.sleep(10)
ImageGrab.grab().save("newminimap/elderdragon.jpg", "JPEG")

while True:
    break
    x += 1
    ImageGrab.grab().save("newminimap/" + str(x) + ".jpg", "JPEG")
    print(x)
    time.sleep(5)
