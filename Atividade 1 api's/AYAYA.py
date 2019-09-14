#API: DOG API
#Faz Downloads de Imagens aleatorios de cachorro para onde o arquivo do python está
import requests
import json
import urllib.request


def baixar(nome):
    a = requests.get('https://dog.ceo/api/breeds/image/random')
    b =json.loads(a.text)
    file_name = nome+ '.jpg'
    urllib.request.urlretrieve(b['message'], file_name)

def main():
    while True == True:
        name = input("digite o nome da imagem")
        baixar(name)

if __name__ == "__main__":
    main()

