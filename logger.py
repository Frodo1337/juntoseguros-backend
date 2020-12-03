#encoding: utf-8

import os
from datetime import datetime

#Função para criar logs do progresso
def write(str):
    #path = "/logs"
    path = "logs"
    #Cria o diretório de logs, caso ele ainda não exista
    if not os.path.exists(path):
        os.mkdir(path)

    #Data para escrever o erro no arquivo de log, a data segue o seguinte formato:
    #ano, mês, dia, hora, minutos e segundos
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #Nome para o arquivo de log, usa o ano, mês e dia como nome
    nomeArquivo = datetime.now().strftime("%Y-%m-%d")
    #Concatena ao arquivo de log o erro
    arquivo = open(path + "/" + nomeArquivo + ".log", "a")
    arquivo.write("[" + data + "]" + str + "\n")
    arquivo.close()
