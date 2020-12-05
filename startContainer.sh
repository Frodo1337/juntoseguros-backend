#!/bin/sh

docker build . -t frodo1337/juntoseguros-backend
docker run -d -p 5000:5000 frodo1337/juntoseguros-backend
