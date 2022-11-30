# 5 užduotis --->
# Parašyti programą, kuri:
# Leistų įvesti skaičių
# Išvesti į ekraną „Skaičius yra lyginis“, jei taip yra
# Išvesti į ekraną „Skaičius yra nelyginis“, jei taip yra
# Išvesti į ekraną „Skaičius dalinasi iš 3“, jei skaičius dalinasi iš trijų
# Patarimas: naudoti input(), if, print, %, <, >

skaicius = int(input("Įveskite skaičių: "))

if skaicius % 2 == 0:
    print("Įvestas skaičius yra lyginis!")
else:
    print("Įvestas skaičius yra nelyginis!")

if skaicius % 3 == 0:
    print("Įvestas skaičius dalinasi iš trijų")
if skaicius % 2 == 0:
    print("Įvestas skaičius dalinasi iš dviejų")