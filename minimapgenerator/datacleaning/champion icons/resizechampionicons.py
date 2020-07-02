import os
from PIL import Image
def resize(imgpath):
    size = 24, 24
    im = Image.open("transparentchampionicons/" + imgpath)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("resizedtransparentchampionicons/" + imgpath, "PNG")

images = os.listdir("transparentchampionicons/")
for image in images:
    resize(image)
