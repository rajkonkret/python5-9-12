# # licznik = 0
# #
# # while True:
# #     licznik += 1
# #     print("Komunikat....")
# #     if licznik == 10:
# #         break
# #
# # licznik = 0
# # while licznik < 10:
# #     print("Komunikat...")
# #     licznik += 1
#
# lista = []
# while True:
#     wejscie = input("Wprowadź liczbę:")
#     if wejscie == "s":
#         break
#     lista.append(int(wejscie))
#
# print(lista)

lista = [4, 6, 8, 10]
people = ["Radek", "Kuba", "Agata", "Krystyna"]
# pos = 2

# while pos < len(people):
#     person = people[pos]
#     liczba = lista[pos]
#     print(person, liczba)
#     pos += 1
#
# liczby = []
# while True:
#     print("Wprowadz liczbe")
#     liczba = input(":")
#     liczby.append(liczba)
#     if liczba == "stop":
#         for i in liczby:
#             print(i * 2)
#
#         break
#     print(liczby)

# a = "Radek"
# if (n := len(a)) > 3:
#     print(n)
#
# n = len(a)
# if n > 3:
#     print(n)
#
# while True:
#     print("""
#         1. Dodawanie
#         2. Odejmowanie
#         3. Koniec
#     """)
#     wybor = input("wprowadz numer (1-3):")
#     if wybor == "1":
#         print("Dodajemy")
#     elif wybor == "2":
#         print("Odejmujemy")
#     else:
#         print("Diekujemy, do widzenia")
#         break


slownik = {1: "Tomek", 2: "Kuba"}
print(slownik)
print({value: key for key, value in slownik.items()})

dictio = {}
for key, value in slownik.items():
    dictio[value] = key
print(dictio)
