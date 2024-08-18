import requests
import json

print('Program do sprawdzania aktualnej pogody w miastach.')
query = input('W jakim miecie chcesz sprawdzić pogodę?: ')

api_key = 'b5ac8b7f5dd1e0df9b1a5ec9861fec33'


response = requests.get(f'http://api.weatherstack.com/current?access_key={api_key}&query={query}')
formated = response.json()

if response.status_code == 200:
    if 'current' in formated:
        current_weather = formated['current']
        temperature = current_weather['temperature']
        feelslike = current_weather['feelslike']
        
        
        print(f'Temperatura w {query} wynosi: {temperature} stopni Celsjusza.')
        print(f'Odczuwalna temperatura w {query} wynosi: {feelslike} stopni Celsjusza.')
        
    else:
        print('Błąd, nie można odczytać temperatury. Sprawdź czy poprawnie wpisałes nazwę miasta.')

input()
        
        
    
