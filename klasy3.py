class Dom:
    """
    To jest klasa DOM,
    """

    def __init__(self, metraz, kolor, ilosc_okien):
        self.__metraz = metraz
        self.kolor = kolor
        self.ilosc_okien = ilosc_okien

    def zmien_metraz(self):
        wybor = int(input("Podaj metraż:"))
        self.__metraz = wybor
        print("Metraz wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj kolor:")
        self.kolor = wybor
        print("Kolor wynosi", self.kolor)
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj okna:"))
        self.ilosc_okien = wybor
        print("okna wynosi", self.ilosc_okien)
    
    def __farba(self):
        print("Skonczyła sie farba")


bud1 = Dom(100, "czerwony", 5)
print(bud1.kolor)
bud1.zmien_metraz()
bud1.zmien_okna()
