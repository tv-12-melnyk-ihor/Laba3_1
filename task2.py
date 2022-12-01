class Notebook:

    def __init__(self):
        self.elements = []

    def __add__(self, person):
        self.elements.append(person)

    def __sub__(self, person):
        self.elements.remove(person)

    def __mul__(self, search_el):
        for p in self.elements:
            for el in p.alldata:
                if (el == search_el):
                    return p
        raise Exception("There are no elements that have this data")


class Person:

    def __init__(self, n, sur, ph, bd):
        self.name = n
        self.surname = sur
        self.phone = ph
        self.birthday = bd
        self.alldata = []
        self.alldata.append(self.name)
        self.alldata.append(self.surname)
        self.alldata.append(self.phone)
        self.alldata.append(self.birthday)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, n):
        self.__surname = n

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, n):
        self.__phone = n

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, n):
        self.__birthday = n


if __name__ == '__main__':
    n1 = Notebook()
    p1 = Person("Pavlo", "Petrenko", "+380501232121", "04.11.2004")
    p2 = Person("Artem", "Shevchenko", "+380669878989", "24.05.2004")
    p3 = Person("Yaroslav", "Antonenko", "+380509638271", "15.06.2005")
    p4 = Person("Yan", "Bayan", "+380664201738", "02.12.2002")
    print("//adding elements by overloading the + operator:\n")
    n1 + p1
    n1 + p2
    n1 + p3
    n1 + p4
    for person in n1.elements:
        print(person.alldata)
    print("\n//removing elements by overloading the - operator:\n")
    n1 - p3
    for person in n1.elements:
        print(person.alldata)
    print("\n//searching for elements by data by overloading the * operator (two examples):\n")
    print((n1 * "24.05.2004").alldata)
    print((n1 * "Petrenko").alldata)