# Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească
# cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion.
# Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. Ajutaţi-l pe Vasile să găsească răspunsul mai repede.
Ion=int(input("Ion a spus numarul "))
print("Ion spune",Ion,",Vasile spune",Ion-2,Ion-1,Ion,Ion+1,Ion+2)
