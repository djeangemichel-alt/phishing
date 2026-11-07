#!/bin/bash

while true 
do 
    echo "[$(date)] Démarre le seveur flask ..."
    py serveur_static.py &  # la command python n'est pas reconnu depuis 
    PID=$!  # recupere le PID du processus qui vient detre lancé
    echo "serveur lancé avec le PID $PID "
    
    sleep 5

    echo "[$(date)] Arret du serveur ..."

    kill $PID

    #petit pause
    sleep 1
done  
