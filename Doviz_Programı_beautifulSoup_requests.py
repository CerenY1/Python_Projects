import requests
from bs4 import BeautifulSoup


url = "https://kur.doviz.com/"
response = requests.get(url)

html_content = response.content   #sayfanın html içeriği gelir.

soup = BeautifulSoup(html_content,"html.parser")    #html sayfasını parçalar ve daha güzel görünmesini sağlar.

#print(soup.prettify()) 
#HTML ve XML gibi yapılandırılmış metin verileri, genellikle birçok iç içe geçmiş etiket ve düzensiz boşluklar içerebilir. soup.prettify() işlevi, bu veriyi girintileme kullanarak daha okunabilir ve düzenli hale getirir.

"""for i in soup.find_all("a"):
    print(i.text)"""

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