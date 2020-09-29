# Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 6 numere formate cu
# aceste cifre luate o singură dată. Exemplu : date de intrare : 3 4 2 Date de ieşire : 324
# 342 243 234 432 423.
a=str(input("a="))
b=str(input("b="))
c=str(input("c="))
print(a+b+c,a+c+b,b+a+c,b+c+a,c+a+b,c+b+a)