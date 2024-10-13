merkit = ['1', '7', '9', '0']

def generoi_salasana(pituus, salasana =""):
    if pituus == 0:
        print(salasana)
    else:
        for merkki in merkit: 
            generoi_salasana(pituus - 1, salasana + merkki)
generoi_salasana(6)