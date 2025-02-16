import http.client
from src.config import settings

def get_http_connn(url:str):
    conn = http.client.HTTPSConnection("")
    conn = http.client.HTTPSConnection(url) 
    return conn