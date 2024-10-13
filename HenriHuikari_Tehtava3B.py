ostoslista = []    
sälä = True
while sälä:
    kala = input("Mitä haluat lisätä ostoslistaan? Jos et, kirjoita valmis: ").capitalize()
    if kala == "Valmis":
        sälä = False
    elif kala != "":
        ostoslista.append(kala)
        print(ostoslista)
ostoslista.sort()
for i in ostoslista:
    print(i)