# a = int(input("podaj liczbe 1"))
# b = int(input("podaj liczbe 2"))
#
# print(a + b)

slownik = {}
slownik["imie"] = "Radek"
slownik["imie"] = "Andrzej"
slownik["wiek"] = 39

print(slownik.items())
print(slownik.values())
print(slownik.keys())

print(slownik)
print(slownik['imie'])

lista = [44, 55, 66, 77, 88, 33, 22, 11, 55, 33, 11]
slownik['liczby'] = lista
print(slownik)
print(slownik['liczby'][0])
lista2 = [44, 55, 66, 11]
nowa_lista = lista + lista2
print(nowa_lista)

slownik2 = {"imie": ["Radek", "Andrzej"], "wiek": 39}
print(slownik2)

slownik3 = {"imie": "name", "kot": "cat"}

# key = input("Podaj wyraz")
# key2 = key.replace(" ", "")
# print(slownik3[key2])
# slownik3.update({"klucz": "Radek"})
# print(slownik3)

a = int("34")
print(a)
print(type(a))
b = str(17)
print(b)
print(type(b))
print(str(a) + b)
