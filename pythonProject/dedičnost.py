class zvieratko:
    def __init__(self, meno):
        self.meno = meno

    def jedz(self,jedlo):
        print(f"{self.meno}: {jedlo} mi chutná!")

# Inherit -> dedenie
#Dedim od zvieratka jeho metody
class Macka(zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Mňau!")

    def jedz(self,jedlo):
        super().jedz( jedlo)
        print(f"{self.meno}: {jedlo} vypľula!")

#Dedim od zvieratka jeho metody
class Pes(zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Haf!")

macka = Macka("Micka")
pes = Pes("Falko")

#Možem používať jedz ktoré som definoval v triede Zvieratko
macka.jedz("Šunka")
macka.urob_zvuk()

#Možem používať jedz ktoré som definoval v triede Zvieratko
pes.jedz("Granulka")
pes.urob_zvuk()


#POLYMORFIZMUS
zvieratka = [Macka("Naginy"), Pes("Azor")]

for zvieratko in zvieratka:
    zvieratko.jedz("Granulka")
    zvieratko.urob_zvuk()

# Generalizacia