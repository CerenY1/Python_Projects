import requests
from bs4 import BeautifulSoup


url = "https://kur.doviz.com/"
response = requests.get(url)

html_content = response.content   

soup = BeautifulSoup(html_content,"html.parser")   

name = soup.find_all("span",{"class":"name"})
value = soup.find_all("span",{"class": "value"})

for i,j in zip(name,value):
    print(i.text + "-->" + j.text)

miktar = float(input("Miktar:"))
type = input("Döviz tipi:")

for i,j in zip(name,value):
    if i.text == type:
        result = float(j.text.replace(",", ".")) * miktar
        print("Tutar: {}TL".format(result))
