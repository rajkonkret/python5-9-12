class Human:
    """
    Klasa Human opisujaca człowieka
    """

    imie = ""
    wiek = None
    plec = ""

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


czlowiek1 = Human()
print(czlowiek1)
print(type(czlowiek1))
print(czlowiek1.plec)
print(czlowiek1.wiek)
print(czlowiek1.imie)

czlowiek1.imie = "Radek"
print(czlowiek1.imie)
print(czlowiek1.powitanie())
czlowiek1.powitanie()
czlowiek1.ruszaj()

czlowiek2 = Human()
czlowiek2.plec = 'k'
czlowiek2.ruszaj()
