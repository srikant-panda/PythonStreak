import requests

def scan ():
    res = requests.get('http://localhost:8000/')
    return res.status_code

