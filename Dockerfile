#Distribuição linux foi alpine porque ela é mais leve
FROM alpine:latest

COPY . /home

WORKDIR /home

RUN apk update && \
    #Instala o python3, o pip para o python3 e as dependências para buildar algumas libs do python
    apk add python3 py3-pip python3-dev g++ libffi-dev openssl-dev && \
    #Instala as dependências da api e para instalar elas
    python3 -m pip install -U pip wheel setuptools && \
    python3 -m pip install -r requirements.txt

#Exclusão de repositórios desnecessários
CMD rm -r __pycache__ logs

#Abre a porta 5000 para api no protocolo tcp
EXPOSE 5000/tcp

#Dá para o container a execução da api como motivo de viver
ENTRYPOINT ["./start.sh"]
