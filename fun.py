a = 5
b = 14

x = 7
y = 10


#
#
# def dodaj():
#     print("wynik = ", a + b)


def odejmij(a, b, c=0):
    print("Wynik = ", a - b - c)


def oblicz_vat(cena, vat=23):
    wynik = cena * (100 + vat) / 100
    return wynik


def oblicz_vat2(cena, vat):
    return cena * (100 + vat) / 100


def odejmij3(a, b):
    return a - b


#
# # PEP8
#
#
# # dodaj()
# odejmij(6, 5)

# odejmij(1, 5)
# print(odejmij(1, 2, 3))
# print(oblicz_vat(1000))
# odejmij(oblicz_vat(100), 54)
# # oblicz_vat(odejmij(5, 4))  # bład
#
# oblicz_vat3 = lambda cena, vat: cena * (100 + vat) / 100
# vat1 = oblicz_vat3(1000, 3)
# print(vat1)
#
# odejmij2 = lambda a, b: a - b
# print(odejmij2(5, 4))
odejmij(x, y)
odejmij(a=x, b=y)
print(a)