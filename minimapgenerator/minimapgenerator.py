from os import listdir
from PIL import Image
from random import randint
#load random minimap image
#pick 10 random champ icons


#place champ icons randomly on minimap and make txt file with coordinates and classes

def placeimage(background, foreground, pos):
    background.paste(foreground, pos, foreground)
    return background

def checkpos(pos, previouspos, touching):
    if touching == False:
        for oldpos in previouspos:
            if ((oldpos[0] - pos[0]) ** 2 + (oldpos[1] - pos[1]) ** 2) ** 0.5 < 24:
                return False
        return True
    if touching == True:
        for oldpos in previouspos:
            if ((oldpos[0] - pos[0]) ** 2 + (oldpos[1] - pos[1]) ** 2) ** 0.5 > 24:
                return False
        return True
def makerandomminimap(touching, f, numofchamps):

    images = listdir("croppedminimap/")
    minimap = Image.open("croppedminimap/" + images[randint(0, len(images) - 1)])
    #image.show()
    previouspos = []

    for i in range(numofchamps):
       foundpos = False
       pos = [randint(3,229), randint(3,229)] #pixels 0,0 are at the top right of images
       while(foundpos == False and len(previouspos) > 0 and touching == False):
           pos = [randint(3,229), randint(3,229)]
           foundpos = checkpos(pos, previouspos, touching)

       while(foundpos == False and len(previouspos) > 0 and touching == True):
           pos = [randint(3,229), randint(3,229)]
           foundpos = checkpos(pos, previouspos, touching)
       previouspos.append(pos)
       object = randint(0, len(champs) - 1)
       champ = champs[object].strip("\n")
       #print(str(object) + " " + str((pos[0] + 12) / 256.0) + " " + str(((pos[1] + 12)) / 256.0) + " " + str(26 / 256.0) + " " + str(26 / 256.0) + "\n")
       f.write(str(object) + " " + str((pos[0] + 12) / 256.0) + " " + str(((pos[1] + 12)) / 256.0) + " " + str(26 / 256.0) + " " + str(26 / 256.0) + "\n")
       championicon = Image.open("resizedtransparentchampionicons/" + champ + ".PNG")
       #print(champ + " pos: " + str(pos))
       minimap = placeimage(minimap, championicon, pos)
    return minimap

f = open("lolchampsclean.txt", "r")
champs = f.readlines()
f.close()
subfolder = "data/"
folder = "train/"
maxnumofchamps = 10 #change
numofimages = 100000 #change
if __name__ == "__main__":
    offset = 1 #in case you interrupt, offset should be equal to the num of the last image (after "notouch" in its name)
    for i in range(numofimages):
        numofchamps = randint(1, maxnumofchamps)
        print(i + offset)
        f = open(subfolder + folder + "notouch" + str(i + offset) + ".txt", "w+")
        minimap = makerandomminimap(False, f, numofchamps)
        f.close()
        minimap.save(subfolder + folder + "notouch" + str(i + offset) + ".jpg")
        if i + offset >= numofimages * 0.9:
            folder = "test/"
        elif i + offset >= numofimages * 0.7:
            folder = "valid/"
