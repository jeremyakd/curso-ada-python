import requests
import pprint
import json

url = "https://covid-193.p.rapidapi.com/countrie"

headers = {
	"X-RapidAPI-Key": "98681c991fmshf6843598095047fp1b8661jsn103fbe67bddd",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

respuesta_cruda = requests.request("GET", url, headers=headers)
print(respuesta_cruda)

respuesta_text = respuesta_cruda.text

json_response = json.loads(respuesta_text)

print(type(json_response['response']))

print(json_response['response'])
