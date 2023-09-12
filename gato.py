# x.|_|x.
# _|X|_
# x.|_|x.

import random
tablero = {
    "fila1" :[0,0,0],
    "fila2" :[0,0,0],
    "fila3" :[0,0,0],
}

print(tablero["fila1"])

def Jugar():
    turn = random.choice([0,1])
    if(turn == 0): #El Bot comienza
        print("Comienza el Bot")
    else: #El jugador Comienza
        print("Comienza el Jugador")


Jugar()