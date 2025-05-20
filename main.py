def nakresli_riadok(sirka,index_riadku):
    print(index_riadku,end="")
    for i in range(sirka):
        nakresli_pole(index_riadku,i)
    print("|",end="")

def nakresli_pole(vyska_1,sirka_1):
    print("|",hra[vyska_1][sirka_1],end="")

def nakresli_cele_pole():
    nakresli_1_riadok(sirka)
    for j in range(vyska):
        plusminus(sirka)
        nakresli_riadok(sirka,j)
        print("")
    plusminus(sirka)
def nakresli_1_riadok(sirka):
    print(" ",end=" ")
    for i in range(sirka):
        print(i, end = " ")
    print("")

def plusminus(sirka):
    print("", end=" ")
    for i in range(sirka):
        print("+-",end="")
    print("+")

def herna():
    while True:
        vyska_1=int(input("zadaj cislo(v): "))
        sirka_1 =int(input("zadaj cislo(s): "))
        hra[vyska_1][sirka_1]= "X"
        nakresli_cele_pole()

vyska=int(input("zadaj cislo: "))
sirka=int(input("zadaj cislo: "))
hra=[ [] ]
for i in range(vyska):
    hra.append([])
    for j in range(sirka):
        hra[i].append(" ")



herna()

# riadok má 2 časti:
# - horny oddelovac     +-+-+-+-+
# - policko so znakom   |*|*|*|*|

# policko má 2 časti:
# - horny oddelovac     +-
# - policko so znakom   |*