import requests
import json

url = "http://pokeapi.co/api/v2/pokemon/"
url2 = "https://es.wikipedia.org/wiki/P%C3%A1gina_web#:~:text=Una%20p%C3%A1gina%20web%2C%20p%C3%A1gina%20electr%C3%B3nica,accedida%20mediante%20un%20navegador%20web."
numero = int(input("COLOCA EL NUMERO DE POKEMON A BUSCAR : "))

def buscarPokemon(num):
    peticion = requests.get(url + str(num))
    respuesta = json.loads(peticion.content)
    print(respuesta["id"])
    print(respuesta["name"])
    #print(peticion.text)
    #peticion2 = requests.get(url2)
    #print(peticion2.text)

buscarPokemon(numero)