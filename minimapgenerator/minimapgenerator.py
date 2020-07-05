from os import listdir
from PIL import Image
from random import randint
#load random minimap image
#pick 10 random champ icons


#place champ icons randomly on minimap and make txt file with coordinates and classes

def placeimage(background, foreground, pos):
    background.paste(foreground, pos, foreground)
    return background

def checkpos(pos, previouspos, touchingrandomizer):

    if touchingrandomizer == False:
        #this will return false if any icon is touching another
        for oldpos in previouspos:
            if ((oldpos[0] - pos[0]) ** 2 + (oldpos[1] - pos[1]) ** 2) ** 0.5 < 24:
                return False
        return True

    if touchingrandomizer == True:
        #this will return false if any icon is not touching at least one other icon
        for oldpos in previouspos:
            if ((oldpos[0] - pos[0]) ** 2 + (oldpos[1] - pos[1]) ** 2) ** 0.5 < 24:
                return True
        return False
def makerandomminimap(iconstouching, f, numofchamps):

    images = listdir(minimapdir)
    minimap = Image.open(minimapdir + images[randint(0, len(images) - 1)])
    #image.show()
    previouspos = []

    for i in range(numofchamps):
       foundpos = False
       pos = [randint(3,229), randint(3,229)] #pixels 0,0 are at the top right of images
       touchingrandomizer = iconstouching
       if iconstouching == True and randint(1, 2) == 2:
           touchingrandomizer = False
       while(foundpos == False and len(previouspos) > 0 and touchingrandomizer == False):
           pos = [randint(3,229), randint(3,229)]
           foundpos = checkpos(pos, previouspos, touchingrandomizer)

       while(foundpos == False and len(previouspos) > 0 and touchingrandomizer == True):
           pos = [randint(3,229), randint(3,229)]
           foundpos = checkpos(pos, previouspos, touchingrandomizer)
       previouspos.append(pos)
       object = randint(0, len(champs) - 1)
       champ = champs[object].strip("\n")
       #print(str(object) + " " + str((pos[0] + 12) / 256.0) + " " + str(((pos[1] + 12)) / 256.0) + " " + str(26 / 256.0) + " " + str(26 / 256.0) + "\n")
       f.write(str(object) + " " + str((pos[0] + 12) / 256.0) + " " + str(((pos[1] + 12)) / 256.0) + " " + str(26 / 256.0) + " " + str(26 / 256.0) + "\n")
       championicon = Image.open(championicondir + champ.replace(" ", "_") + ".png")
       #print(champ + " pos: " + str(pos))
       minimap = placeimage(minimap, championicon, pos)
    return minimap

#variables to change for new datasets
minimapdir = "newcroppedminimap/"
subfolder = "data/"
folder = "train/"
iconstouching = True
maxnumofchamps = 10
numofimages = 1000
championicondir = "resizedtransparentchampionicons/"
championlistdir = "lolchampsclean.txt"

f = open(championlistdir, "r")
champs = f.readlines()
f.close()

if __name__ == "__main__":
    offset = 1 #in case you interrupt, offset should be equal to the num of the last image (after "notouch" in its name)
    for i in range(numofimages):
        numofchamps = randint(1, maxnumofchamps)
        print(i + offset)
        f = open(subfolder + folder + "notouch" + str(i + offset) + ".txt", "w+")
        minimap = makerandomminimap(iconstouching, f, numofchamps)
        f.close()
        minimap.save(subfolder + folder + "notouch" + str(i + offset) + ".jpg")
        if i + offset >= numofimages * 0.9:
            folder = "test/"
        elif i + offset >= numofimages * 0.7:
            folder = "valid/"
