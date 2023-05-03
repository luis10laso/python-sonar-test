import requests

respuesta = requests.get("https://fakestoreapi.com/users")

tuples = [(x["username"], x["email"]) for x in respuesta.json()]

print(tuples)