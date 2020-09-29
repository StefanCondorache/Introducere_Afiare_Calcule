# Afişaţi tabla înmulţirii cu numărul n. Exemplu: pentru n=5, se va afişa pe verticală
# 1x5=5 2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50.
n=int(input("n="))
for a in range(11):
 print(n,"*",a,"=",n*a)