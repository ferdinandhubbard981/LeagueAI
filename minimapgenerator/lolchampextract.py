#https://lol.gamepedia.com/Portal:Champions/List

f = open("lolchampunclean.txt", "r")
oldlist = f.readlines()
newlist = []
for line in oldlist:
    if (line[0] == " "):
        newlist.append(line.strip())
f.close()
with open("lolchampsclean.txt", "w") as f:
    for line in newlist:
        f.write(line + "\n")
