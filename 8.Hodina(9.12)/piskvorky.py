hracie_pole=[
    ["","1","2","3","4","5","6","7","8","9"],
    ["1"," "," "," "," "," "," "," "," "," "],
    ["2"," "," "," "," "," "," "," "," "," "],
    ["3"," "," "," "," "," "," "," "," "," "],
    ["4"," "," "," "," "," "," "," "," "," "],
    ["5"," "," "," "," "," "," "," "," "," "],
    ["6"," "," "," "," "," "," "," "," "," "],
    ["7"," "," "," "," "," "," "," "," "," "],
    ["8"," "," "," "," "," "," "," "," "," "],
    ["9"," "," "," "," "," "," "," "," "," "],
]

def usporiadanie(hracie_pole):
    for riadok in hracie_pole:
        for policko in riadok:
            print(policko,end="")
        print()

while True:
    usporiadanie(hracie_pole)
    print("Na tahu je hráč číslo 1")
    osaX = int(input("Zadaj osu X:"))
    osaY = int(input("Zadaj osu Y:"))
    symbol = hracie_pole[osaX][osaY] = "X"

    usporiadanie(hracie_pole)
    print("Na tahu je hráč číslo 2")
    osaX = int(input("Zadaj osu X:"))
    osaY = int(input("Zadaj osu Y:"))
    symbol = hracie_pole[osaX][osaY] = "O"

