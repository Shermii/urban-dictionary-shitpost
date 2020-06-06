from random import randint
from bs4 import BeautifulSoup
from requests import get

# this whole thing was made at 2am because I thought it was funny

def help():
    print('type "yes for more"')
    print('type "no" to quit')


def shitpost():
    url = f"https://www.urbandictionary.com/random.php?page={randint(1,1000)}"
    print(url[43:], "\n")
    text = get(url).content
    html = BeautifulSoup(text, features="lxml")

    print("Word: \n    " + html.find("a", class_="word").text + "\n")
    print("Meaning: \n    " + html.find("div", class_="meaning").text, "\n")
    print("Example: \n    " + html.find("div", class_="example").text, "\n")

print("type help or H E L P for help")
shitpost()


while 1:
    xx = input("more? ")
    
    xx = ''.join(xx.split(" ")).lower()


    if (xx == "help"):
        help()

    if (xx[:4] == "more" or xx[:3] == "yes"):
        shitpost()

    elif (xx[:2] == "no" or xx[:4] == "stop" or xx[:4] == "nope" or xx[:6] == "yamete"):
        quit()
