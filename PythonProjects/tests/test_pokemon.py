import requests
import pytest

host= 'https://api.pokemonbattle.me:9104'

def test_check_response():
    response = requests.get(f'{host}/trainers',params= {'trainer_id':3492})
    response = response.json()
    assert response["trainer_name"] == "Mei"
    
 
def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200