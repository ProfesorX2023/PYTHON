import bs4
import requests
import lxml

resultado = requests.get('https://academiafibonacci.com.gt/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

barra_navegacion = sopa.select('.menu-navegacion a')

for a in barra_navegacion:
    print(a.getText())