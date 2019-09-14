#API:  MetaWeather
#Busca cidades que contenham o mesmo nome ou parte da string digitada e retorna a lista com os nomes, latitude e longitude
import requests
import json
import urllib.request


def buscar_cidade(nome):
    a = requests.get('https://www.metaweather.com/api/location/search/?query='+ nome)
    b =json.loads(a.text)
    return b

def main():
    while True == True:
        name = input("digite o nome da cidade")
        cidades = buscar_cidade(name)
        for cidade in cidades:
            print(cidade['title'] + ' / ' + cidade['latt_long'])

if __name__ == "__main__":
    main()

