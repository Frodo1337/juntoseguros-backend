#encoding: utf-8

import logger
import pyrebase

class Database:
    def __init__(self, config):
        self.config = config;
        self.rodando = False
        self.firebase = None

    def inicia(self):
        logger.write("Inicializando firebase...")

        if not self.rodando:
            try:
                self.firebase = pyrebase.initialize_app(self.config).database()
                self.rodando = True

                logger.write("Firebase inicializada com sucesso!")
            except Exception as e:
                logger.write("Erro: " + str(e))
        else:
            logger.write("Firebase já inicializada")
