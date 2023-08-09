import requests
from bs4 import BeautifulSoup

url = "https://720pizle.mov/imdb-top-250-film.asp"

response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

# a = float(input("Rating'i giriniz:"))

basliklar = soup.find_all("a", {"class": "block text-nowrap text-black py-3"})
rating = soup.find_all("span", {"class": "text-bold text-[#333] text-small"})

with open("imdb.txt","w",encoding="utf-8") as file:
    x=1
    file.write("FILM'S;\n"
               "----------------------------------------------\n***********************************************\n"
               "----------------------------------------------\n")
    for i,j in zip(basliklar,rating):
        i=i.text.lstrip()
        j=j.text
        file.write("{}) NAME:{}RATING: {}\n".format(x,i,j))
        file.write("------------------------------------------\n")
        x+=1



