#encoding: utf-8

import sys
import json
import logger
from flask_cors import CORS
from datetime import datetime
from flask import Flask, jsonify, request

class Api:
    def __init__(self, ip, db):
        app = Flask(__name__)

        #HOME PAGE
        @app.route("/")
        def home():
            if self.db.rodando:
                return "API is running and good to go :)"
            else:
                return "API is running, but database is down :("

        #CRIAÇÃO DE UMA NOVA TAREFA
        @app.route("/tarefas/nova/<idUsuario>&<tarefa>", methods=["POST"])
        def criaNovaTarefa(idUsuario, tarefa):
            try:
                dados = {"tarefa": tarefa, "concluida": "false"}
                self.db.firebase.child("tarefas").child(idUsuario).push(dados)

                return self.criaResponse("Ok", 200)
            except Exception as e:
                logger.write("Erro ao responder requisição '/tarefas/nova/': " + str(e))

                return self.criaResponse("Error: " + str(e), 500)

        #SELEÇÃO DE TODAS AS TAREFAS DE UM USUÁRIO
        @app.route("/tarefas/todas/<idUsuario>", methods=["GET"])
        def selecionaTodasTarefasUsuario(idUsuario):
            try:
                retorno = self.db.firebase.child("tarefas").child(str(idUsuario)).get()

                return self.criaResponse(retorno.val(), 200)
            except Exception as e:
                logger.write("Erro ao responder requisição '/tarefas/todas/': " + str(e))

                return self.criaResponse("Error: " + str(e), 500)

        #SELEÇÃO DE TODAS AS TAREFAS CONCLUÍDAS DE UM USUÁRIO
        @app.route("/tarefas/todasConcluidas/<idUsuario>", methods=["GET"])
        def selecionaTodasTarefasConcluidas(idUsuario):
            try:
                #Seleção de todas as tarefas de um usuário
                tarefas = self.db.firebase.child("tarefas").child(str(idUsuario)).get()
                #Conversão das tarefas para um dicionário
                dadosTarefas = dict(tarefas.val())
                #Seleção de apenas tarefas concluídas através de comprehension
                tarefasConcluidas = {i: dadosTarefas[i] for i in dadosTarefas if dadosTarefas[i]["concluida"] == "true"}

                return self.criaResponse(tarefasConcluidas, 200)
            except Exception as e:
                logger.write("Erro ao responder requisição '/tarefas/todasConcluidas/': " + str(e))

                return self.criaResponse("Error: " + str(e), 500)

        #REMOÇÃO DE UMA TAREFA
        @app.route("/tarefas/deleta/<idUsuario>&<idTarefa>", methods=["DELETE"])
        def deletaTarefa(idUsuario, idTarefa):
            try:
                self.db.firebase.child("tarefas").child(str(idUsuario)).child(str(idTarefa)).remove()

                return self.criaResponse("OK", 200)
            except Exception as e:
                logger.write("Erro ao responder requisição '/tarefas/deleta/': " + str(e))

                return self.criaResponse("Error: " + str(e), 500)

        #MARCANDO UMA TAREFA COMO CONCLUÍDA
        @app.route("/tarefas/conlcui/<idUsuario>&<idTarefa>", methods=["PUT"])
        def concluiTarefa(idUsuario, idTarefa):
            try:
                #Seleciona a tarefa a ser concluída
                tarefa = self.db.firebase.child("tarefas").child(str(idUsuario)).child(str(idTarefa)).get()
                #Converte o resultado da query para um dict
                dadosTarefa = dict(tarefa.val())
                #Atualiza a tarefa como concluída
                dadosTarefa["concluida"] = "true"

                self.db.firebase.child("tarefas").child(str(idUsuario)).child(str(idTarefa)).update(dadosTarefa)

                return self.criaResponse("OK", 200)
            except Exception as e:
                logger.write("Erro ao responder requisição '/tarefas/conlcui/': " + str(e))

                return self.criaResponse("Error: " + str(e), 500)

        self.ip = ip
        self.app = app
        self.running = False
        self.db = db

        CORS(self.app)

    #Retorna uma response para a api
    def criaResponse(self, response, status):
        response = self.app.response_class(response=json.dumps(response),
                                           status=status,
                                           mimetype="application/json")
        return response

    #Inicia a API
    def start(self):
        #Define que a API está rodando
        self.running = True
        #Inicia a API
        self.app.run(debug=True, host=self.ip)
