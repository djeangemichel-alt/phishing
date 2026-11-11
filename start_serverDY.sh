#!/bin/bash

while true 
do 
    echo "[$(date)] Démarre le seveur flask ..."
    py serveur_static.py &  # la command python n'est pas reconnu depuis 
    PID=$!  # recupere le PID du processus qui vient detre lancé
    echo "serveur lancé avec le PID $PID "
    
    sleep 15

    echo "[$(date)] Arret du serveur ..."

    kill $PID

    #petit pause
    sleep 1
done  


































while True 
do
    echo "lancement du serveur ..."

    sleep (2)

    python3 envoyerICMP.py & 
    

    echo " le serveur s'est arrété "

    sleep (5)

done 



while True 
do
    echo "lancement du serveur ..."

    sleep (2)

    python3 envoyerICMP.py & 
    PID = $!

    echo " le serveur va s'arréter"
    sleep (5)
    kill $PID

    sleep (5)

done 