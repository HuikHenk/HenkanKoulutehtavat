sana = input("Anna sana: ")

kaannetty_sana = ""

for i in range(len(sana)-1, -1, -1):
    kaannetty_sana += sana[i].lower()  
print("Käännettynä: " + kaannetty_sana)
