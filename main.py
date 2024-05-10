from requests import get
import json

def get_json_data(postal_code):
    api_url = ("https://viacep.com.br/ws/" + postal_code + "/json")
    request = get(api_url)
    return request

given_postal_code = str(input("Postal code: "))

response = json.loads(get_json_data(given_postal_code).text)

print(f'CEP: {response["cep"]}')
print(f'Logradouro: {response["logradouro"]}')
print(f'Complemento: {response["complemento"]}')
print(f'Bairro: {response["bairro"]}')
print(f'UF: {response["uf"]}')
print(f'DDD: {response["ddd"]}')