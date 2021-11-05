#!/bin/python3
import turtle
turtle.speed(int(input("Speed[ 0 - fastest, 10 - slowest ]:"))) # geschwindigkeit einlesen und festlegen

def levy_c(n:int, tp:str="I", size:int=50):
    """
    n:int = rekursionstiefe
    tp:str = typ des anfangspunktes (I oder L)
    size:int = größe der gezeichneten linien
    """
    if n == 0:                   # abbruchsbedingung
        if tp=="I":              # je nach typ grundstruktur zeichnen
            turtle.forward(size) # einen einzelnen Strich für I
        else:
            turtle.forward(size) # eine L-förmige Struktur für L
            turtle.right(-90)
            turtle.forward(size)
            turtle.right(90)
    else:
        turtle.right(45)         # der rekursive aufruf von Levy C
        levy_c(n-1, tp, size)    # die nächst kleinere rekursion wird aufgerufen
        turtle.right(-90)
        levy_c(n-1, tp, size)    # ^
        turtle.right(45)

levy_c(int(input("Recursion Depth:")), tp=input("Type [I or L]"), size=int(input("Size Multiplier:")))
# rekursionstiefe, typ des anfangspunktes und größe der gezeichneten linien werden eingelesen
input("Done!")
