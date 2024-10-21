luku1 = int(input("Anna ensimmäinen luku (pienempi): "))
luku2 = int(input("Anna toinen luku (suurempi): "))

prosentti = (luku1 / luku2) * 100

print(f"{luku1} on {prosentti:.2f}% luvusta {luku2}.")

palkki = int(prosentti // 10)  
print("Latauspalkki:")
print("●" * palkki + "○" * (10 - palkki)) 