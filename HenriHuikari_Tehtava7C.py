# Tyhjä lista numeroille
numerot = []

# Pyydetään käyttäjältä numeroita, kunnes syötetään tyhjä rivi
while True:
    syote = input("Anna numero (tai tyhjä lopettaaksesi): ")
    if syote == "":
        break
    numerot.append(int(syote))  # Lisätään numero listaan

# Uusi lista järjestettyjä numeroita varten
jarjestetyt_numerot = []

# For-silmukalla lajitellaan numerot pienimmästä suurimpaan
for i in range(len(numerot)):
    pienin = numerot[0]
    for numero in numerot:
        if numero < pienin:
            pienin = numero
    jarjestetyt_numerot.append(pienin)
    numerot.remove(pienin)  # Poistetaan pienin numero alkuperäisestä listasta

# Tulostetaan järjestetty lista
print("Järjestetyt numerot pienimmästä suurimpaan:")
print(jarjestetyt_numerot)
