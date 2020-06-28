import os
images = os.listdir("D://coding/minimapgenerator/mixedpictures/")
print(images[0])
for image in images:
    image = image.crop((1645, 805, 1920, 1080))
    image.save("")
