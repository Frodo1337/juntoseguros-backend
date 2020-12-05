#encoding: utf-8

import sys
import json
from api import Api
from database import Database

if __name__ == "__main__":
    #Carrega o arquivo de credenciais
    arquivoCredenciais = open("credentials.json", "r")
    credenciais = json.load(arquivoCredenciais)
    arquivoCredenciais.close()

    db = Database(credenciais)
    api = Api("0.0.0.0", 5000, db)

    db.inicia()
    api.start()
