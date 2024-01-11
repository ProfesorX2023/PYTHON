import bs4
import requests
import lxml

resultado = requests.get("https://academiafibonacci.com.gt/")

#print(type(resultado))

#print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('title')) Aparece como lista

#print(sopa.select('p')) Aparecen todos los parrafos de la página

#print(len(sopa.select('p'))) aparece la cantidad de párrafos de la página

#print(sopa.select('title')[0]) muestra el titulo sin los corchetes

#print(sopa.select('title')[0].getText()) muestra el contenido del titulo

#parrafo_especial = sopa.select('p')

#print(parrafo_especial[3].getText())