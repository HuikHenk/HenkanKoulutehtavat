minun_ika = 20


while True:
    arvattu_ika = int(input ("Arvaa minun ikä. (15-30) "))
    if arvattu_ika <15 or arvattu_ika >30:
        print("Numero ei kelpaa! ")
        
    elif minun_ika != arvattu_ika:
        print("ARVASIT VÄÄRIN")
    else:
        while True:
          print("Arvasit OIKEIN OIKEIN!!!")

