from abc import ABC, abstractmethod


class Ptak(ABC):
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Startuje i lecę z prędkością:", self.szybkosc)

    @abstractmethod
    def wydajOdglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie!")

    def wydajOdglos(self):
        print("piiiiii")


# ptak = Ptak("1","asd") - nie da sie

ptak1 = Orzel('orzel', 100)
ptak1.lataj()
ptak1.poluj()
ptak1.wydajOdglos()
