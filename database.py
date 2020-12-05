#encoding: utf-8

import logger
import pyrebase

class Database:
    def __init__(self, config):
        self.config = config;
        self.rodando = False
        self.database = None
        self.auth = None

    def inicia(self):
        logger.write("Inicializando firebase...")

        if not self.rodando:
            try:
                firebase = pyrebase.initialize_app(self.config)
                self.database = pyrebase.initialize_app(self.config).database()
                self.auth = pyrebase.initialize_app(self.config).auth()
                self.rodando = True

                logger.write("Firebase inicializada com sucesso!")
            except Exception as e:
                logger.write("Erro: " + str(e))
        else:
            logger.write("Firebase já inicializada")
