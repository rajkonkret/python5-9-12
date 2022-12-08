zbior = "Tomek", "Michał", "Asia", "Daniel"
zbior2 = "radek",
zbior3 = 43, 55, 22.43, 11, 200

print(type(zbior2))
print(zbior)
print(zbior.count("Tomek"))
print(zbior3)
print(zbior3.count(55))
print(zbior.index("Asia"))
asia = zbior[2]

print(asia)
print(zbior)

*imie1, imie2, imie3 = zbior
print(imie1)
print(imie2)
print(type(imie1))

lista = list(zbior)
print(lista)