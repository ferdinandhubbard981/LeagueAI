from os import listdir
from PIL import Image
from random import randint
#load random minimap image
print("1")
#images = listdir("mixedpictures/")
#image = Image.open("mixedpictures/" + images[randint(0, len(images) - 1)])
#image.show()
#pick 10 random champ icons


#place champ icons randomly on minimap and make txt file with coordinates and classes

img = Image.open('championicons/Darius.jpg', 'r')
img_w, img_h = img.size
background = Image.new('RGBA', (1440, 900), (255, 255, 255, 255))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, offset)
background.save('out.png')
print("done")
