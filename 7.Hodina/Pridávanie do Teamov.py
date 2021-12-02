import random
timA = []
timB = []
timC = []

while True:
    nickname = input("Zadaj svoj nick:")
    tim = random.randrange(0, 3)
    if tim == 0:
        timA.append(nickname)
    elif tim == 1:
        timB.append(nickname)
    elif tim == 2:
        timC.append(nickname)
    print("V tíme A sú: ", timA)
    print("V tíme B sú: ", timB)
    print("V tíme C sú: ", timC)



