# czy_znasz_Python = True
#
# if czy_znasz_Python:
#     print("Brawo")
# else:
#     print("Musisz sie jeszcze uczyć")
#
# print("Jestem poza warunkiem")
#
# podatek = 0.0
#
# zarobki = int(input("Podaj swoj dochod: "))
#
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.35
# else:
#     podatek = 0.4
#
# print(f"Zapłacisz {zarobki * podatek} zł")

# lista_bledow = []
# alert_system = 'email'
# error = 'critical'
# error_message = "Stało sie coś strasznego!"
#
# if alert_system == 'console':
#     print(error_message)
# elif alert_system == 'email':
#     if error == 'critical':
#         lista_bledow.append('critical')
#     elif error == 'medium':
#         lista_bledow.append('medium')
#     else:
#         lista_bledow.append('nieznany')
#
# print(lista_bledow)
#
# suma_zam = 247
# rabat = 25 if suma_zam > 100 else 0
# print(rabat)
# if suma_zam > 100:
#     rabat = 25
# else:
#     rabat = 0
#
# print("suma zam:", suma_zam, "rabat:", rabat)

lista = []
# lang = input("Wpisz znany Ci język programowania")
#
# match lang:
#     case "python":
#         lista.append(lang)
#     case "java":
#         lista.append(lang)
#     case _:
#         print("nie ma takiego języka")
#
# print(lista)

temp = -115
alert = True

if temp < 0:
    print("mróz")
    if temp < -100:
        pass
    if temp < -10:
        if alert:
            print("Alert pogodowy")

elif temp == 0:
    print("przymrozek")
elif 10 < temp < 20:
    print("dodatnia")
elif temp >= 20:
    print("upał")
