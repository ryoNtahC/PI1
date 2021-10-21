start = 10
koniec = 0
while start>=koniec:
    if start <= 5:
        start -= 1
        continue
    print(start)
    start -= 1

print("-----------")

start = 10
while start >= koniec:
    if start == 5:
        break
    print(start)
    start -=1
"""Vypýtajte si od uzivatela pociatocne a koncove cislo 
a vypiste len nasobky cisla 3 medzi tymito cislami
"""
start = int(input("Zadaj odkial zacnem pocitat"))
koniec = int(input("zadaj pokial budem pocitat"))
while(start < koniec):
    if(start % 3 ==0):
        print(start, "je nasobok 3ky")
    start += 1


print("---------------")
print("---------------")
print("---------------")

for premenna in range(10):
    print(premenna)

samohlasky = "aáeéiíoóuúyý"
spoluhlasky = "hchkgdtnlčdžšžczjďťňľbmprsvzf"
cisla = "0123456789"
slovo = input("zadaj slovo")
pocet_samohlasok = 0
pocet_spoluhlasok = 0
pocet_cisel = 0
pocet_ostatnych = 0
for znak in slovo:
    if znak in samohlasky:
        pocet_samohlasok += 1
    elif znak in spoluhlasky:
        pocet_spoluhlasok += 1
    elif znak in cisla:
        pocet_cisel +=1
    else:
        pocet_ostatnych += 1
print("V Slove je:")
print("Samohlások:",pocet_samohlasok)
print("Spoluhlások:",pocet_spoluhlasok)
print("Čísel:",pocet_cisel)
print("Ostatné:",pocet_ostatnych)

riadky = int(input("Zadaj počet riadkov"))
stlpce = int(input("Zadaj počet stlpcov"))

for i in range(0,stlpce):
    for j in range (0,riadky):
        print("*", end="")
    print()