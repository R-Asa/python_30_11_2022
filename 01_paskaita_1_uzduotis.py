# 1 užduotis --->
# Parašyti programą, kuri:
# Leistų įvesti skaičius a ir b (int arba float)
# Išvestų į ekraną „a mažesnis už b“, jei taip yra
# Išvestų į ekraną „a lygu b“, jei taip yra
# Išvestų į ekraną „a didesnis už b“, jei taip yra
# Patarimas: naudoti if, elif, else sąlygas

a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))

if a < b:
    print("a maziau uz b")
if a > b:
    print("a daugiau uz b")
elif a == b:
    print("a lygu b")
else:
    print("Ivyko klaida, toks skaicius neegzistuoja")