#API: PlaceGoat
#Faz download de imagens de bodes baseados em uma largura e altura inserida pelo usuário
import requests
import json
import urllib.request


def baixar(nome,largura,altura):
    a = 'http://placegoat.com/' + largura + '/' + altura
    file_name = nome+ '.jpg'
    urllib.request.urlretrieve(a, file_name)

def main():

    while True == True:
        largura = input("digite a largura da imagem")
        altura = input("digite a altura da imagem")
        name = input("digite o nome da imagem")
        baixar(name,largura,altura)

if __name__ == "__main__":
    main()
