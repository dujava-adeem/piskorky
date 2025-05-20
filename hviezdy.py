def nakresli_riadok(sirka,index_riadku):
    print(index_riadku,end=" ")
    for i in range(sirka):
        nakresli_pole()

def nakresli_pole():
    print("*",end=" ")

def nakresli_cele_pole():
    nakresli_1_riadok(sirka)
    for j in range(vyska):
        nakresli_riadok(sirka,j)
        print("")
def nakresli_1_riadok(sirka):
    print(" ",end=" ")
    for i in range(sirka):
        print(i, end = " ")
    print("")

vyska=int(input("zadaj cislo: "))
sirka=int(input("zadaj cislo: "))
nakresli_cele_pole()
