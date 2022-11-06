import io
from unittest.mock import patch
from unittest import TestCase

from ulubione_auta import UlubioneAuta
from auto import Auto


class TestUlubioneAuta(TestCase):
    def test_dodanie_ulubionych_aut_zle_wprowadzenie(self):
        obiekt = UlubioneAuta()
        with self.assertRaises(TypeError):
            obiekt.dodaj_auto(42, "Ceed", 2001)
        with self.assertRaises(TypeError):
            obiekt.dodaj_auto("Kia", 32, 2001)
        with self.assertRaises(TypeError):
            obiekt.dodaj_auto("Kia", "Ceed", "2001")

    def test_znalezienie_duplikatow(self):
        obiekt = UlubioneAuta()
        obiekt.dodaj_auto("Kia", "Ceed", 2001)
        obiekt.dodaj_auto("Kia", "Ceed", 2001)
        obiekt.dodaj_auto("Kia", "Sportage", 2001)
        obiekt.dodaj_auto("Kia", "Sportage", 2001)
        self.assertEqual(obiekt.znajdz_duplikaty(),
                         [(Auto("Kia", "Ceed", 2001), 1), (Auto("Kia", "Sportage", 2001), 1)])
        obiekt.dodaj_auto("BMW", "E30", 2005)
        self.assertNotIn((Auto("BMW", "E30", 2005), 0), obiekt.znajdz_duplikaty())
        self.assertNotIn((Auto("BMW", "E30", 2005), 1), obiekt.znajdz_duplikaty())
        self.assertNotIn((Auto("BMW", "E30", 2005), 2), obiekt.znajdz_duplikaty())
        self.assertEqual(obiekt.znajdz_duplikaty(),
                         [(Auto("Kia", "Ceed", 2001), 1), (Auto("Kia", "Sportage", 2001), 1)])

    def test_wypisanie_duplikatow(self):
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
        expected = """Wykryto duplikaty:
Marka: Fiat, Nazwa: 500x, Rok produkcji: 2005 - 1
Marka: Fiat, Nazwa: Croma, Rok produkcji: 2020 - 1
Marka: Kia, Nazwa: Ceed, Rok produkcji: 2001 - 2
Marka: BMW, Nazwa: E30, Rok produkcji: 2005 - 1
"""
        with patch('sys.stdout', new=io.StringIO()) as text:
            lista.wypisz_duplikaty()
            self.assertEqual(text.getvalue(), expected)

    def test_usun_duplikaty(self):
        pass

    def test_sortuj_nazwa(self):
        pass

    def test_sortuj_nazwa_odwrotnie(self):
        pass

    def test_sortuj_marka(self):
        pass

    def test_sortuj_marka_odwrotnie(self):
        pass

    def test_sortuj_rok(self):
        pass

    def test_sortuj_rok_odwrotnie(self):
        pass
