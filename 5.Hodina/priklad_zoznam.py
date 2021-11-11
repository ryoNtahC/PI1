zoznam_cisel=[10,9,8,7,6,5,4,3,2,1]
for cislo in zoznam_cisel:
    print(cislo)


zadaj = input("Zadaj nazov ovocia alebo zeleniny:")
zoznam_ovocia=["jablko","hruska","banan","pomaranc","mandarinka","ceresna","ananas","citron","jahoda"]
zoznam_zeleniny=["brokolica","salat","kalerab"]
if zadaj in zoznam_ovocia:
    print("je to ovocie")
elif zadaj in zoznam_zeleniny:
    print("je to zelenina")
else:
    print("nepatrí nikam")
opakovanie = input("chces pokracovat ano/nie")
pokracovat=["ano"]
koncit=["nie"]
if opakovanie in pokracovat:
    while(True):
        zadaj = input("Zadaj nazov ovocia alebo zeleniny:")
        if zadaj in zoznam_ovocia:
            print("je to ovocie")
        elif zadaj in zoznam_zeleniny:
            print("je to zelenina")
        else:
            print("nepatrí nikam")
elif opakovanie in koncit:
    print("koniec")
