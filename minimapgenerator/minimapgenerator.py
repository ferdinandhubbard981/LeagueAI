from os import listdir
from PIL import Image
from random import randint
#load random minimap image
#pick 10 random champ icons


#place champ icons randomly on minimap and make txt file with coordinates and classes

def placeimage(background, foreground, pos):
    background.paste(foreground, pos, foreground)
    return background


#background = Image.open("croppedminimap/" + "minimap1.jpg")
#foreground = Image.open("resizedtransparentchampionicons/" + "Red_kayn.png")
#placeimage(background, foreground)
def checkpos(pos, previouspos, touching):
    if touching == False:
        for oldpos in previouspos:
            if ((oldpos[0] - pos[0]) ** 2 + (oldpos[1] - pos[1]) ** 2) ** 0.5 < 24:
                print("failed!")
                return False
        return True
    if touching == True:
        for oldpos in previouspos:
            if ((oldpos[0] - pos[0]) ** 2 + (oldpos[1] - pos[1]) ** 2) ** 0.5 > 24:
                print("failed!")
                return False
        return True
def makerandomminimap(touching):

    images = listdir("croppedminimap/")
    minimap = Image.open("croppedminimap/" + images[randint(0, len(images) - 1)])
    #image.show()
    previouspos = []

    for i in range(30):
       foundpos = False
       pos = [randint(3,229), randint(3,229)] #pixels 0,0 are at the top right of images
       print(len(previouspos))
       while(foundpos == False and len(previouspos) > 0 and touching == False):
           pos = [randint(3,229), randint(3,229)]
           foundpos = checkpos(pos, previouspos, touching)

       while(foundpos == False and len(previouspos) > 0 and touching == True):
           pos = [randint(3,229), randint(3,229)]
           foundpos = checkpos(pos, previouspos, touching)
       previouspos.append(pos)
       images = listdir("resizedtransparentchampionicons/")
       champpath = images[randint(0, len(images) - 1)]
       championicon = Image.open("resizedtransparentchampionicons/" + champpath)
       print(champpath[:-4] + " pos: " + str(pos))
       minimap = placeimage(minimap, championicon, pos)
    return minimap
if __name__ == "__main__":
    minimap = makerandomminimap(False)
    minimap.show()
    minimap.save("minimaptests/minimap.jpg")
