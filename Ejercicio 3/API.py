from urllib.request import urlopen
import json

class Dolar:
    __resultado = None
    
    def __init__(self):
        self.__resultado = None
        
    def Run(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
        
    def getResultado(self):
        return (self.__resultado)