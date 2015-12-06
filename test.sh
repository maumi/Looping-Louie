#!/bin/bash

# Pin als Eingang definieren
echo "12" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio12/direction
# Pin als Ausgang def. per gpio-befehl
i2cset -y 1 0x20 0x01 0x00

previous=$(cat /sys/class/gpio/gpio12/value)
running=false

# Endlose Schleife
while true
do
# Den Zustand des Eingangs lesen
pin=$(cat /sys/class/gpio/gpio12/value)

# Wenn der Eingang von 0 auf 1 gewechselt hat
if [ $pin -gt $previous ]
then
	if [ "$running" = false]; then 
		# Das Programm starten
		sudo python /home/pi/main.py &
		echo "Taster wurde betätigt am $(date), spiel starten"
		#LED anschalten
		i2cset -y 1 0x20 0x15 0x01
		running=true
		sleep(2)
	else
		# Das Programm stoppen
		sudo killall python
		echo "Taster wurde betätigt am $(date), spiel stoppen"
		#LED ausschalten
		i2cset -y 1 0x20 0x15 0x00
		running=false
		sleep(2)
	fi		
	
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
