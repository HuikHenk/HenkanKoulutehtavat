from collections import Counter
teksti = input("Anna teksti tai lause: ")

laskin = Counter(teksti)
yleisimmat = laskin.most_common(5)
sanakirjasälä = dict(yleisimmat)

print("Viisi yleisintä merkkiä:")
print(sanakirjasälä)
