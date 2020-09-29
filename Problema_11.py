# Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
# începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
# realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
# iepuri sunt în crescătorie? Exemplu : Date de intrare : nr. Iepuri la început de luna 10
# nr. iepuri morti 2 nr. iepuri nascuti 6 Date de ieşire : 14 iepuri.
nr1=int(input("nr. Iepuri la început de luna "))
nr2=int(input("nr. iepuri morti "))
nr3=int(input("nr. iepuri nascuti "))
print(nr1+(nr3-nr2),"iepuri")