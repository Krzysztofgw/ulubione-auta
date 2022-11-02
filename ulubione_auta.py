# zad 1 Napisz klase ktora bedzie posiadala metode obliczajaca nww i nwd, napisz do tej klasy klase testowa sprawdzajaca NWD i nww
# zad 2 Napisz klase posiadajaca liste ulubionych aut, napisz mchanizm sortowania, wypisywania duplikatow, usuwania duplikatow
# napisz niezbedne testy pod zadane funkcjonalnosci
# zad 3 Calosc zamiesc na gitHub

from auto import Auto
import operator


class UlubioneAuta:
    def __init__(self):
        self.auta = []

    def __getitem__(self, item):
        return self.auta[item]

    def dodaj_auto(self, marka, nazwa, rok_produkcji):
        if not (isinstance(marka, str) and isinstance(nazwa, str)):
            raise TypeError("Nieprawidłowy typ danych - nazwa oraz marka powinna być tekstem.")
        if not isinstance(rok_produkcji, int):
            raise TypeError("Nieprawidłowy typ danych - rok produkcji powinien być liczbą całkowitą.")
        nowe_auto = Auto(marka, nazwa, rok_produkcji)
        self.auta.append(nowe_auto)

    def wypisz_auta(self):
        for auto in self.auta:
            print(auto)

    def znajdz_duplikaty(self):
        zbior_porownaczy = set(self.auta)
        if len(zbior_porownaczy) == len(self.auta):
            return []
        else:
            duplikaty = []
            for i in zbior_porownaczy:
                if (licznik := self.auta.count(i)) != 1:
                    duplikaty.append((i, licznik - 1))
            return duplikaty

    def wypisz_duplikaty(self):
        if self.auta:
            if duplikaty := self.znajdz_duplikaty():
                print("Wykryto duplikaty:")
                for i, licznik in duplikaty:
                    print(i, f"- {licznik}")
                return True
            else:
                print("Nie wykryto duplikatów.")
                return False
        else:
            print("Nie wprowadzono ulubionych aut.")
            return False

    def usun_duplikaty(self):
        if self.auta:
            if duplikaty := self.znajdz_duplikaty():
                for auto, licznik_duplikatow in duplikaty:
                    for licz in range(licznik_duplikatow):
                        del self.auta[self.auta.index(auto)]

    def sortuj_nazwa(self, odwrotnie=False):
        return sorted(self.auta, key=operator.attrgetter('nazwa'), reverse=odwrotnie)

    def sortuj_marka(self, odwrotnie=False):
        return sorted(self.auta, key=operator.attrgetter('marka'), reverse=odwrotnie)

    def sortuj_rok(self, odwrotnie=False):
        return sorted(self.auta, key=operator.attrgetter('rok_produkcji'), reverse=odwrotnie)


if __name__ == "__main__":

    lista = UlubioneAuta()

    lista.dodaj_auto("Kia", "Ceed", 2000)
    lista.dodaj_auto("Kia", "Ceed", 2001)
    lista.dodaj_auto("Kia", "Ceed", 2001)
    lista.dodaj_auto("Kia", "Ceed", 2001)
    lista.dodaj_auto("Kia", "Ceed", 2002)
    lista.dodaj_auto("BMW", "E30", 2005)
    lista.dodaj_auto("BMW", "E30", 2005)
    lista.dodaj_auto("Fiat", "500", 2005)
    lista.dodaj_auto("Fiat", "500x", 2001)
    lista.dodaj_auto("Fiat", "500x", 2003)
    lista.dodaj_auto("Fiat", "500x", 2005)
    lista.dodaj_auto("Fiat", "500x", 2005)
    lista.dodaj_auto("Fiat", "Bravo", 2005)
    lista.dodaj_auto("Fiat", "Croma", 2020)
    lista.dodaj_auto("Fiat", "Croma", 2020)
    # lista.wypisz_auta()

    lista.wypisz_duplikaty()

    lista.usun_duplikaty()

    lista.wypisz_duplikaty()

    lista.wypisz_auta()
    print(lista.sortuj_nazwa(False))
    print(lista.sortuj_nazwa(True))
    print(lista.sortuj_marka(False))
    print(lista.sortuj_marka(True))
    print(lista.sortuj_rok(False))
    print(lista.sortuj_rok(True))