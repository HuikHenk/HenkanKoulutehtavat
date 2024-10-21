numerot = []

while True:
    syote = input("Anna numero (tai tyhjä lopettaaksesi): ")
    if syote == "":
        break
    numerot.append(int(syote)) 

jarjestetyt_numerot = []

for i in range(len(numerot)):
    pienin = numerot[0]
    for numero in numerot:
        if numero < pienin:
            pienin = numero
    jarjestetyt_numerot.append(pienin)
    numerot.remove(pienin)  

print("Järjestetyt numerot pienimmästä suurimpaan:")
print(jarjestetyt_numerot)
