import os
images = os.listdir("minimapgenerator/mixedpictures/")
print(images[0])
x = 0
for image in images:
    x += 1
    image = image.crop((1645, 805, 1920, 1080))
    image.save("croppedminimap/minimap" + str(x) + ".jpg")
