#!/usr/bin/env bash

#http://github.com/gyukebox/ELSA-server
#http://github.com/gyukebox/ELSA-client
#http://github.com/gyukebox/ELSA-situation-recognition

#ELSA-server
echo "ELSA-SERVER:"
source ELSA-environment/bin/activate
python ELSA-server/manage.py runserver
#http://127.0.0.1:8000
echo "ELSA-SERVER::DONE"

#ELSA-client
echo "ELSA-CLIENT:"
cd ELSA-client
npm run build
cd ..
echo "ELSA-CLIENT::DONE"

#ELSA-situation-recognition
echo "ELSA-SITUATION_RECOGNITION:"
python ELSA-situation-recognition/main.py
echo "ELSA-SITUATION_RECOGNITION::DONE"

#Open Browser
python -mwebbrowser http://127.0.0.1:8000
