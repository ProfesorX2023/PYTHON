import bs4
import requests
import lxml

resultado = requests.get("https://www.gconta.com/")

sopa = bs4.BeautifulSoup(resultado.text,'lxml')



imagenes2 = sopa.select('img')

for i in imagenes2:
    print(i)

imagen=requests.get(imagenes2)

