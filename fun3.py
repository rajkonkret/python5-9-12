odejmij = lambda a, b: a - b

print(odejmij(5, 3))
print(odejmij(9, 4))

oblicz_vat = lambda cena, vat: cena * (100 + vat) / 100

print(oblicz_vat(1000, 1))
vat1 = oblicz_vat(1000, 7)
print(vat1)

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(5))
print(wiek(15))
print(wiek(25))

lista = [1, 2, 7, 8, 10, 56]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 3, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
