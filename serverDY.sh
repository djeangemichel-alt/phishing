#!/bin/bash

while true 
do 
    echo "[$(date)] Démarre le seveur flask ..."
    py serveur.py &   
    PID=$!  # recupere le PID du processus qui vient detre lancé
    echo "serveur lancé avec le PID $PID "
    
    sleep 35

    echo "[$(date)] Arret du serveur ..."

    kill $PID

    #petit pause
    sleep 1
done  
