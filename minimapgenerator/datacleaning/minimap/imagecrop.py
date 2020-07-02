from PIL import Image
import os
images = os.listdir("mixedpictures/")
print(images[0])
x = 0
for image in images:
    x += 1
    im = Image.open("mixedpictures/" + image)
    #im = im.crop((1645, 805, 1920, 1080))
    im = im.crop((1653, 813, 1909, 1069)) #multiple of 32
    im.save("croppedminimap/minimap" + str(x) + ".jpg")