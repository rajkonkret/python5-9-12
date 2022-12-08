a = 10


def dodaj():
    global a
    a = 1
    b = 2
    print("Wynik ", a + b)


def dodaj2(a):
    b = 2
    return a + b


print("Wartość z góry a", a)
# dodaj()
print("Wartość z góry a", a)
print(dodaj2(a))
print("Wartość z góry a", a)
