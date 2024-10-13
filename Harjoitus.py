# Pyydetään käyttäjää syöttämään numerot listaan
merkit = input("Syötä haluamasi numerot pilkuilla erotettuina: ").split(",")
merkit = [merkki.strip() for merkki in merkit]

# Funktio, joka generoi salasanat ja laskee, montako kertaa se kutsutaan
def generoi_salasana(pituus, salasana =""):    
    if pituus == 0:
        print(salasana)
    else:
        for sälä in merkit:
            generoi_salasana(pituus - 1, salasana + sälä)

# Pyydetään käyttäjää syöttämään haluamansa salasanan pituus
pituus = int(input("Syötä salasanan pituus: "))

# Generoidaan kaikki mahdolliset salasanat käyttäjän antamilla merkeillä
generoi_salasana(pituus)

