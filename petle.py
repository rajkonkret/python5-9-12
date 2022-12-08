# lista = []
#
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
#         lista.append(i)
# print(lista)
#
# for cyfra in lista:
#     if cyfra == 2:
#         cyfra += 1  # cyfra = cyfra + 1 -= *=
#     print(cyfra)
#
# lista = [j for j in range(10) if j % 2 == 0]
# print(lista)
#
# imiona = ["Radek", "Zenek", "Marta"]
# for p in range(len(imiona)):  # range(3)
#     print(p, imiona[p])
#
# imie = "Radek"
# for p in range(len(imie)):
#     print(p, imie[p])
#
# imie = "Radek"
# for pozycja, wartosc in enumerate(imie):
#     print(pozycja, wartosc)
#
# for pozycja, wartosc in enumerate(imiona):
#     print(pozycja, wartosc)
#
# # enumerate(imie)
# # pozycje = p
# # wartosc = imie[p]
#
# ludzie = ["Radek", "Janek", "Asia", "Michał"]
# wiek = [47, 67, 32, 34]
# jezyk = ["Python", "java"]
#
# for pozycja, osoba in enumerate(ludzie, start=1):
#     print(pozycja, osoba)
#
# for pozycja, osoba in enumerate(ludzie):
#     print(pozycja, osoba, wiek[pozycja])
#
# # for i in range(1, 10, 2):
# #     print(i)
#
# for osoba, wiek, jezyk in zip(ludzie, wiek, jezyk):
#     print(osoba, wiek, jezyk)
#
# slownik = {"imie": "Radek", "nazwisko": "Kowalski"}
#
# for k in slownik:
#     print(k)
#
# for v in slownik.values():
#     print(v)
#
# for k, v in slownik.items():
#     print(k, "=>", v)

napis = "Radek"

for i in range(-1, -len(napis), -1):
    j = i + 1
    if j == 0:
        print(napis[i::])
    else:
        print(napis[i:j])
