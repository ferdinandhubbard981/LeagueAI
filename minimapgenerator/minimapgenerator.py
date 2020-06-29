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

def placeimage(background, foreground):
    background.paste(foreground, (200, 200), foreground)
    background.show()

background = Image.open("croppedminimap/" + "minimap1.jpg")
foreground = Image.open("resizedtransparentchampionicons/" + "zyra.png")
placeimage(background, foreground)
