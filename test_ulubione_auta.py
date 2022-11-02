import unittest

from ulubione_auta import UlubioneAuta


class TestUlubioneAuta(unittest.TestCase):
    def test_dodanie_ulubionych_aut_zle_wprowadzenie(self):
        obiekt = UlubioneAuta()
        with self.assertRaises(TypeError):
            obiekt.dodaj_auto(42, "Ceed", 2001)
        with self.assertRaises(TypeError):
            obiekt.dodaj_auto("Kia", 32, 2001)
        with self.assertRaises(TypeError):
            obiekt.dodaj_auto("Kia", "Ceed", "2001")

    def dodanie_ulubionych_aut_blednie(self):
        pass

    def znalezienie_duplikatow(self):
        pass

    def wypisanie_duplikatow(self):
        pass

    def usun_duplikaty(self):
        pass

    def sortuj_nazwa(self):
        pass

    def sortuj_nazwa_odwrotnie(self):
        pass

    def sortuj_marka(self):
        pass

    def sortuj_marka_odwrotnie(self):
        pass

    def sortuj_rok(self):
        pass

    def sortuj_rok_odwrotnie(self):
        pass
