





print("Olet opettajana luokassa, joka on täynnä oppilaita. Oppilas kysyy kysymyksen, johon et tiedä vastausta. Mitä teet? Vastaa VAIN numeroilla 1-2. EI 3.")

kayttajavalinta = int(input("1: Pakenet ikkunasta vai 2: Improvisoit? \n>>"))
if kayttajavalinta == 1:
    print("Valitsit siis paeta ikkunasta.")
    print("Päädyit paettuasi oppilaitoksesi parkkipaikalle jossa törmäät rehtoriin.")
    print("Rehtori huomattuaan sinut kysyy, mitä teet ulkona oppituntisi aikana. Miten toimit?")


    kayttajavalinta = int(input("1: Valehtelet hänelle päin naamaa vai 2: Kerrot totuuden? \n>>"))
    if kayttajavalinta == 1:
        print("Valehtelet unohtaneesi työläppärin autoon ja palaisit tuota pikaa takaisin työn pariin.")
        print("Valehtelusi menee läpi. Ei mitenkään yllättävää sillä sinut tunnetaan koulussa psykopaattina haha")
        print("Hyppäät autoon ja poistut maasta.")
    elif kayttajavalinta >= 3:
        print("Änkesit itsesi paperisilppuriin silkasta häpeästä :(")
    
    else:
        print("Selität rehtorille nolon tilanteensi. Hän katsoo sinua ymmärtäväisesti")
        print("Rehtori selittää sinulle, miten kaikkea ei aina tarvitse tietää eikä aina tarvitse olla oikeassa.")
        print("Hän rohkaisee sinua palaamaan tunnille ja keksimään tekosyyn ikkunasta pakenemiseen.")


else:
    print("Päätit siis improvisoida.")
    print("Sälääääääää säläääääääää sälääääääääääääääää")
    print("Oppilaat eivät ole vakuuttuneita.")
   
    kayttajavalinta = int(input("1: Myönnät ettet oikeasti tiedä vai 2: Gaslightaa oppilaat uskomaan ettei millään ole mitään merkitystä.\n>>"))
    if kayttajavalinta == 1:
        print("Myönsit oman tietämättömyytesi aiheeseen.")
        print("Oppilaat nauroivat.")
        print("Oppitunti jatkui normaalisti ja säästyit suurelta sotkulta.")
   
    elif kayttajavalinta >= 3:
        print("Änkesit itsesi paperisilppuriin silkasta häpeästä :(")
    else:
        print("Oppilaat be like mitä vittua?")
        print("--> Hetken aisiaa pohodittuaan he ymmärtävät ajatuksesi ja ovat samaa mieltä.")
        print("TIME PASSES")
        print("Seuraavana päivänä oppilaat eivät saavu enää kouluun. Rehtorin Wilma on täynnä vihaisia viestejä vanhemmilta,")
        print("kuinka heidän lapsensa ovat menettäneet elämänhalunsa yhden oppitunnin takia. SAIT POTKUT. HÄVISIT PELIN.")