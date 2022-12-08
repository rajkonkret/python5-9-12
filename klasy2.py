class Human:
    """
    Klasa Human, opisujaca człowieka jao obiekt w Pytonie
    """

    def __init__(self, imie, wiek=0, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        """
        Metoda w klasie Human
        :return: print z imieniem
        """
        print("Nazywam sie:", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w droge")


czl1 = Human("radek")
print(czl1.imie)

czl1.ruszaj()
czl1.plec = "m"
czl1.ruszaj()
print(czl1.wiek)

print(Human.__doc__)