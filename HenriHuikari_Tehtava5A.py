import datetime
joulu = datetime.datetime(2024, 12, 24)
nykyhetki = (datetime.datetime.now())

kayttaja_valinta = int(input("Montako päivää jouluun on, kirjoita 1. Montako päivää jouluun on omasta syntymäpäivästäsi, kirjoita 2. "))
paivia_jouluun = joulu - nykyhetki

if kayttaja_valinta == 1:
    print(paivia_jouluun)

elif kayttaja_valinta == 2:
    synttarit = input("Milloin on seuraava syntymäpäiväsi (pp.kk.vvvv)? ")

    syntymapaiva = datetime.datetime.strptime(synttarit, "%d.%m.%Y")
    print(f"Syntymäpäiväsi on: {syntymapaiva}")
    paivia_syntymasta_jouluun = (joulu - syntymapaiva).days


    if paivia_syntymasta_jouluun >= 0:
     print("Synttäreistäsi jouluun on ", paivia_syntymasta_jouluun, "päivää.")

    else:
       print("Jouluaatto on jo ollut tänä vuonna syntymäpäiväsi jälkeen.")

