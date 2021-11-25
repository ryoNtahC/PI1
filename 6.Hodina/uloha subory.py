pocet = int(input("zadaj pocet suborov:"))
slovo = []
a=0
slovo_v_subore = [a+1]
with open("./basnicka.txt", encoding="UTF-8") as subor:
    for riadok in subor:
        slovo += riadok.split()
dlzka_basnicky=len(slovo)
b = 0
for i in range(pocet):
    if i >= dlzka_basnicky:
        b = i - dlzka_basnicky

    open("%s.txt" % i, "w", encoding="UTF-8").write(slovo[b])
    filename = "%s.txt" % b
    novy_subor = open(filename, "w", encoding="UTF-8")
    print(slovo[b], file=novy_subor)
    novy_subor.close()