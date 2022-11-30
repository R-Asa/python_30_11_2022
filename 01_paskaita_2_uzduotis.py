# 2 užduotis --->
# Parašyti programą, kuri su eilute "Zen of Python" darytų šiuos veiksmus:
# Atspausdintų paskutinį antro žodžio simbolį
# Atspausdintų pirmą trečio žodžio simbolį
# Atspausdintų tik pirmą žodį
# Atspausdintų tik paskutinį žodį
# Atspausdintų visą frazę atbulai
# Atskirtų žodžius ir juos atspausdintų
# Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
# Patarimas: naudoti string karpymo įrankius, funkcijas split(), replace()

zodis = "Zen of Python"
print(zodis[5])
# f
print(zodis[-6])
# P
print(zodis[:3])
# Zen
print(zodis[7:])
# Python
print(zodis[::-1])
# nohtyP fo neZ
print(zodis.split())
# ['Zen', 'of', 'Python']
print(zodis.replace("Python", "Programming"))
# Zen of Programming