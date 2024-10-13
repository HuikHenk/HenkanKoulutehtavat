from random import randrange
def kayttajatunnus (etunimi, sukunimi): 
    random_numero = randrange(100, 999)
    kokonimi = etunimi[:3] + sukunimi[:3] + str(random_numero)
    return kokonimi
etunimi = input("Kerro etunimesi: ").lower()
sukunimi = input("Kerro sukunimesi: ").lower()
pelinimi = kayttajatunnus(etunimi, sukunimi)
print(pelinimi)