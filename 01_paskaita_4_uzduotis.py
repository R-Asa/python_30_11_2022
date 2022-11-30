# 4 užduotis --->
# Parašyti programą, kuri:
# Leistų įvesti pirmą skaičių
# Leistų įvesti antrą skaičių
# Paklaustų, kokį matematinį veiksmą reiktų atliktų
# Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.
# Patarimas: naudoti input(), if, print

a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))
c = input("Pasirinkite matematinį veiksmą (+, -, *, /): ")

if c == "+":
    print("Skaičių suma lygi: ", a + b)
if c == "-":
    print("Skaičių atimtis lygi: ", a - b)
if c == "*":
    print("Skaičių daugyba lygi: ", a * b)
if c == "/":
    print("Skaičių dalyba lygi: ", a / b)