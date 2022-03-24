import random


class Cat:
    # KONŠTRUKTOR --> Vykoá savždy keďVYTVÁRAM inštanciu triedy
    def __init__(self, name, vek):
        print("Vytvaram objekt mačky")
        self.name = name
        self.vek = vek

    def __str__(self):
        print("Meno mačky je: " + self.name)
        print("Vek mačky je: " + str(self.vek))
        return " ";

    def zamnaukaj(self):
        print(self.name + " mňau")

    def zjedz(self, jedlo):
        print(self.name + " zjdela/zjedlo " + jedlo)


# vytvorenie INŠTANCIE OBJEKTU mačka
cat = Cat("Mica", 4)


# volanie metodys
cat.zamnaukaj()
cat.zjedz("rybu")

cat2 = Cat("Murko", 5)
cat2.zamnaukaj()

print(cat2)



class Auto:
    def __init__(self,autko, znacka, rok_vyroby, farba, pocet_miest_sedenie, nastartovane ):
        self.autko = autko
        self.znacka = znacka
        self.rok = rok_vyroby
        self.farba = farba
        self.miesta = pocet_miest_sedenie
        self.start = False

    def toggleMotor(self, state):
        self.start = state


    def __str__(self):
        print("má značku " + str(self.znacka), " ,rok výroby " + str(self.rok), " ,farbu " + self.farba)
        print(" rok výroby " + str(self.rok))
        print("farbu" + self.farba)
        print("Auto je nastartované: " + str(self.start))
        return "-----------"
    def trubenie(self):
        print(self.znacka + " TUTU!")

    def chodDopredu(self):
        print("chodDopredu")

auticko = Auto("autko","BMW", 2006, "červená", "5 miest nasedenie", "je nastartovane")
auticko.trubenie()
auticko.chodDopredu()
print(auticko)








cislo1 = int(input("Zadaj číslo 1: "))
cislo2 = int(input("Zadaj číslo 2: "))

class Kalkulacka:

    def __init__(self, cislo1, cislo2):
        self.cislo1 = cislo1
        self.cislo2 = cislo2

    def sucet(self):
        return cislo1+cislo2
    def rozdiel(self):
        return cislo1-cislo2
    def sucin(self):
        return cislo1*cislo2
    def podiel(self):
        return cislo1/cislo2

kalkulacka = Kalkulacka(cislo1,cislo2)
print("sucet je " + str(kalkulacka.sucet()))
print("rozdiel je " + str(kalkulacka.rozdiel()))
print("sucin je " + str(kalkulacka.sucin()))
print("podiel je " + str(kalkulacka.podiel()))

pocet = int(input("Zadaj počet strán: "))

class Kocka:
    def __init__(self, pocet):
        self.pocet = pocet

    def hod(self):
        return random.randrange(1,pocet)

kocka = Kocka(pocet)
kocka2 = Kocka(pocet)
print("Hod prvou kockou: ")
for i in range (10):

    print(str(kocka.hod()))
print("-------------")
print("Hod druhou kockou: ")
for y in range (10):
    print(str(kocka2.hod()))
print("-------------")
