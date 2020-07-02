from PIL import Image
from os import listdir
def transparent(imgdir, imgpath):
        img = Image.open(imgdir + imgpath)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        imgpath = imgpath[:-4]
        print(imgpath)
        img.save("transparentchampionicons/" + imgpath + ".png")

images = listdir("championicons/")
for image in images:
    transparent("championicons/", image)
