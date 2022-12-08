lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
zbior = set(lista)

print(lista)
print(zbior)
zbior.add(18)
zbior.add(18)
zbior.add(62)
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
lista2 = list(zbior)
print(zbior)
print(type(zbior))
print(lista2)

zbior2 = {66, 11, 44, 18, 55, 62, 999}
print(zbior2)
print(zbior | zbior2)
print(zbior & zbior2)
print(zbior - zbior2)
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
