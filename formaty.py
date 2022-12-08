# name = "Tomek"
name = "Radek"
if name == "Radek":
    print(f"Twoje imie to {name}")

# name = "Tomek"
if name := "Radek":
    print(f"Twoje imie to {name}")

przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
prompt = "Wybierz swoją przekąskę:"
print(przekaski)
# while True:
#     choice = input(prompt)
#     if choice in przekaski:
#         break
#     print("Nie ma i co mi zrobisz")
#
# print(f"Twoj wybor {choice}")
#
# while (choice := input(prompt)) not in przekaski:
#     if choice == 'exit':
#         break
#     print("Nie ma")
# print(f"Twoj wybor\" '{choice}'")

user = "Tomek"
wiek = 39
wersja = 3.90001  # float
liczba = 134632344532

# print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %(user)s masz teraz %(age)d lat" % {'user': user, "age": wiek})
# print("Witaj {} masz teraz {} lat".format(user, wiek))
# print(f"Witaj {user} masz teraz {wiek} lat")

print("Używamy wersji Python %i" % 3)
print("Używamy wersji Python %f" % 3.9)
print("Używamy wersji Python %.1f" % 3.9)
print("Używamy wersji Python %.f" % 3.9)
print("Używamy wersji Python {}".format(wersja))
print(f"Używamy wersji Python {wersja:.1f}")
print(f"Używamy wersji Python {wersja:.2f}")
print(f"{user:>10}")
print(f"{user:>20}")
print(f"{user:>30}")
print(f"{user:<30}")
print("Nasza duża liczba {:,}".format(liczba).replace(',', '.'))
print("Nasza duża liczba {:,}".format(liczba).replace(',', ' '))
print(liczba)
