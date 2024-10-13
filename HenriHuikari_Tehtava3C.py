from random import randrange
tarkistus_numerot = []

voittaneet_numerot = [1, 3, 11, 28, 30, 34, 39]
i = 0
while tarkistus_numerot != voittaneet_numerot:
  muuttuja = 0
  lotto_nuumerot = []
  while muuttuja < 7:
    random_numero = randrange(1,41)
    if random_numero not in lotto_nuumerot:
      lotto_nuumerot.append(random_numero)
      muuttuja += 1
  
  lotto_nuumerot.sort()
  tarkistus_numerot = lotto_nuumerot
  i += 1
 

print("Ostit",i, "lottoriviä")
print("VOITIT BILJOONA ZILJOONAA SUOMEN DOLLARIA")

#https://www.youtube.com/watch?v=MSL1lMkjNi4