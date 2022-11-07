# Schreiben Sie ein Python-Skript, das alle Positionsparameter mit Nummerierung in umgekehrter Reihenfolge ausgibt.

import sys

print("Input args: ")
print(sys.argv)

allArgs = len(sys.argv)
startindex = allArgs-1

while startindex > 0:
    print("Position:", startindex, " ", sys.argv[startindex]) 
    startindex = startindex - 1