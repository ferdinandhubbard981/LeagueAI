# to get the champion icons from website
# the images were in semi random directories so I had to brute force the a/ab part where a and b can be a digit or lowercase letter. 

import requests
list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
with open("lolchampscleancropped.txt", "r") as file:
    champ_names = [line.rstrip('\n').replace(" ", "_") for line in file]
print(champ_names[0])
requestcount = 0
for champ_name in champ_names:
    found = False
    for i in list:
        if found == True:
            break
        for j in list:
            url = "https://vignette.wikia.nocookie.net/leagueoflegends/images/" + i + "/" + i + j + "/" + champ_name + "_OriginalCircle.png"
            print(url)
            response = requests.get(url)
            requestcount += 1
            print(requestcount)
            if response.status_code == 404:
                continue

            with open("championicons/" + champ_name + ".jpg", "wb") as f:
                content = response.content
                f.write(content)
            found = True
            break
