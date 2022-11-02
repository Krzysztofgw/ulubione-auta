class Auto:
    def __init__(self, marka, nazwa, rok_produkcji):
        self.marka = marka
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji

    def __str__(self):
        return f"Marka: {self.marka}, Nazwa: {self.nazwa}, Rok produkcji: {self.rok_produkcji}"

    def __repr__(self):
        return f"<Marka: {self.marka}, Nazwa: {self.nazwa}, Rok produkcji: {self.rok_produkcji}>"

    def __eq__(self, other):
        if self.marka == other.marka and self.nazwa == other.nazwa and self.rok_produkcji == other.rok_produkcji:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.rok_produkcji < other.rok_produkcji:
            return True
        else:
            return False

    def __le__(self, other):
        if self.rok_produkcji <= other.rok_produkcji:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.rok_produkcji > other.rok_produkcji:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.rok_produkcji >= other.rok_produkcji:
            return True
        else:
            return False

    def __hash__(self):
        hash_value = 0
        for i in str(self):
            hash_value += ord(i)
        return hash_value


if __name__ == "__main__":
    new1 = Auto("m", "m", "1990")
    new2 = Auto("m", "m", "1990")
    new3 = Auto("m", "m", "1990")
    new4 = Auto("m", "m", "1991")

    print(new1.__hash__())
    print(new2.__hash__())
    print(new3.__hash__())
    print(new4.__hash__())

    new_set = {new1, new2, new3, new4}

    print(new1 > new2)
    print(new_set)
    new_list = [new1, new2, new3, new4]
    for i in new_list:
        print(i)