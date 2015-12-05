#!/bin/bash

# Pin als Eingang definieren
echo "12" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio12/direction
# Pin als Ausgang def. per gpio-befehl
#gpio -g mode 17 out
# Den Zustand des Eingangs lesen

previous=$(cat /sys/class/gpio/gpio12/value)

# Endlose Schleife
while true
do
# Den Zustand des Eingangs lesen
pin=$(cat /sys/class/gpio/gpio12/value)

# Wenn der Eingang von 0 auf 1 gewechselt hat
if [ $pin -gt $previous ]
then
# Das Programm starten
echo "Taster wurde betätigt am $(date)"
# protokollierung wann taster gedrückt in taster.log. “>>” definiert das Einträge in .log  #addiert werden
#echo “Taster wurde betätigt am $(date)” >> taster.log
# status led ansteuern
#gpio -g write 17 1
#gpio -g write 17 0
else
# Definition des timeout, um CPU-Load zu Optimieren
sleep 0.05
fi

# variabel wird zum neuen Durchlauf auf den Wert “previous” gesetzt
previous=$pin
done
