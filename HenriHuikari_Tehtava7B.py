# Kysytään käyttäjältä sanaa
sana = input("Anna sana: ")

# Luodaan tyhjä merkkijono käännetylle sanalle
kaannetty_sana = ""

# Käydään sana läpi for-silmukalla lopusta alkuun
for i in range(len(sana)-1, -1, -1):
    kaannetty_sana += sana[i].lower()  # Muutetaan kirjain pieneksi ja lisätään merkkijonoon

# Tulostetaan käännetty sana
print("Käännettynä: " + kaannetty_sana)
