#Piedra, Papel o Tijera
#import random para numeros aleatorios
from random import randint

print("""Elije tu número:
1.Piedra
2.Papel
3.Tijera""")

Jugador = input(":")
player = int(Jugador)       #convierte string a numero entero
computadora = randint(1,3)  #Crea numero aleatorio 1-3
#Piedra = 1, Pape l = 2, Tijera = 3

if player != 1 and player != 2 and player != 3:
    print("Elige un numero del 1 al 3, IDIOTA")
elif player == 1 and computadora == 2:
    print("Perdiste. Elegiste Piedra y Yo Papel jajajajaj!!")
elif player == 2 and computadora == 3:
    print("Perdiste. Elegiste Papel y Yo Tijeras jajajajaj!!")
elif player == 3 and computadora == 1:
    print("Perdiste. Elegiste Tijera y Yo Piedra jajajajaj!!")
elif player == computadora:
    print("Empatamos")
else:
    print("Ganaste, pero te ganaré PUTO!!")

#Resultados
print("Jugador", player)
print("Computador", computadora)
