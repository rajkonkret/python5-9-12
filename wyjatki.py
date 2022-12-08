# def mnozenie(a, b):
#     try:
#         return int(a) * int(b)
#     except (TypeError, ValueError):
#         print("Bład typu, zwracam bezpieczne zero")
#         return 0


def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        print("Bład typu, zwracam bezpieczne zero")
        return 0
    except ValueError:
        print("Bład wartości, zwracam bezpieczne zero")
        return 0


def dzielenie(a, b):
    try:
        return int(a) / int(b)
    except TypeError:
        print("Bład typu, zwracam bezpieczne zero")
        return 0
    except ValueError:
        print("Bład wartości, zwracam bezpieczne zero")
        return 0
    except ZeroDivisionError:
        print(" Nie dziel przez zero, zwracam bezpieczne zero")
        return 0


print(mnozenie(5, 6))
print(mnozenie("3", "4"))
print(mnozenie("a", "b"))
print("Skonczylem mnozenie")
print(mnozenie(2.8, 5.6))
print(mnozenie((2.8,), (5.6,)))
dzielenie(2, 0)


def mnozenie3(a, b):
    try:
        print(int(a) * int(b))
    except Exception as e:
        print("wystapił", e)
        print(0)
    else:
        wynik = []
        wynik.append(a)
        wynik.append(b)
        print(wynik)
    finally:
        print("Wykonałem instrukcje z funkcji mnożenia")


# print(mnozenie3("a", "b"))
# print(mnozenie3(3, 3))
mnozenie3(3, 3)
mnozenie3("q", "w")
