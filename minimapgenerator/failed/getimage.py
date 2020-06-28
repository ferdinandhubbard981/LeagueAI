import requests

url = "https://leagueoflegends.fandom.com/wiki/File:Akali_OriginalCircle.png"

with open("./champion_icons/test.png","wb") as f:
    content = requests.get(url).content
    f.write(content)
