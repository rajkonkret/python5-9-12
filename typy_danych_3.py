lista = []
lista.append("Radek")
lista.append("Tomek")
lista.append("Asia")
lista.append("Renata")
lista.insert(1, "Darek")
print(lista)
lista[1] = "Magda"
print(lista)
lista.remove("Asia")
print(lista.append("a"))
lista2 = lista.copy()
print(lista2)

liczby = [54, 999, 34, 22, 12.54, 876]
liczby.sort()
liczby.reverse()
print(liczby)
liczby_2 = liczby.copy()
liczby.clear()
print(liczby)
print(liczby_2)
liczby_2[0] = 6666
print(liczby_2[0:3])
print(liczby_2[:3])
print(liczby_2[2:])
print(liczby_2[:-1])
print(liczby_2)
print(len(liczby_2))
liczby_2.remove(54)
print(liczby_2)
print(len(liczby_2))  # len() - długosc listy
krotka = tuple(liczby_2)
print(krotka)
