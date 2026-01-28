import os
import sys
import json

__path__ = os.path.dirname(os.path.abspath(__file__))
__root__ = os.path.dirname(os.path.dirname(__path__))
sys.path.append(__root__)

from core.search import search
from core.binarization import binarization
from core.plot import plot_bit_sequence

class Provider:
    def __init__(self, user_config, plot_config=None):
        self.user_config = user_config
        self.plot_config = plot_config
        self.database = "data.json"
        self.ip_address = "9.9.9.9"
    
    # pesquisa na web e retorna resultados binarizados
    def search(self, query):
        s = search(query)
        raw_results = s.search()
        b = binarization()
        binary_results = b.binarize(raw_results)
        return binary_results
    
    #verifica se o usuario existe no banco de dados
    def is_true(self, json_user):
        try:
            if json_user and "id" in json_user and "password" in json_user:
                with open(self.database, 'r') as file:
                    data = json.load(file)
                    for user in data.get("users", []):
                        if user.get("id") == json_user["id"] and user.get("password") == json_user["password"]:
                            return True
            return False
        except:
            return False
    

    def upload(self, json_upload):
        pacote_recebido = json_upload
        
        # validar usuario 
        passe = self.is_true(pacote_recebido)
        if not passe:
            return None 
        
        # buscar na web
        search_term = pacote_recebido.get("term", "")
        if not search_term:
            return None
        search_results = self.search(search_term)
    
        return search_results


if __name__ == "__main__":
    user_config = {
        "id": 1,
        "password": "030202",
        "ip": "192.168.1.1",
        "term": "historia do brasil"
    }

    provider = Provider(user_config)
    result = provider.upload(user_config)
    print("Resultados de Busca Binarizados:", result)
    if result:
        plot_bit_sequence(result)
    else:
        print("Nenhum resultado para plotar.")
    
    binarizer = binarization()
    decoded_results = binarizer.debinarize(result)
    print("Resultados de Busca Decodificados:")
    print(decoded_results)
    
    
    