import random

def _1():
    lista = ["låt_1", "låt_2", "låt_3", "låt_4", "låt_5"]
    for v in lista: print(v)
    print()
    print(f"Första element: {lista[0]} | Sista element: {lista[-1]}")

def _2():
    namn = []
    for i in range(5):
        namn.append(input("Skriv namn: "))
    for v in namn: print(v)

def _3():
    tal = [1, 2, 3, 4, 5]
    summa = 0
    for v in tal: summa += v
    print(f"Summa: {summa}")

def _4():
    färger = ["röd", "grön", "blå"]
    print(f"Före ersättning: {färger}")
    nyFärg = input("Ny färg: ")
    färger[1] = nyFärg
    print(f"Efter ersättning: {färger}")

def _6_1():
    talföljd_längd = int(input("Längd på talföljd: "))
    k = 3
    talföljd = [2]
    for i in range(talföljd_längd):
        talföljd.append(talföljd[-1] * k)
    print(talföljd)

def _6_2():
    in_heltal = input("Heltal (på formen a,b,c,...): ")
    heltal = in_heltal.strip().split(",")
    antal_negativa = 0
    for v in heltal:
        try:
            if int(v) < 0:
                antal_negativa += 1
        except:
            print("Fel vid formattering.")
    print(f"Antal negativa tal: {antal_negativa}")

def _6_3():
    rand_list = []
    summa = 0
    for i in range(100):
        värde = random.randint(1,1000)
        rand_list.append(värde)
        summa += värde
    
    minsta = min(rand_list)
    största = max(rand_list)
    medelvärde = summa/100
    print(f"Medelvärde: {medelvärde}")

def _6_4():
    heltal = [0,5,2,0,4]
    offset = 0
    for i in range(len(heltal)):
        if heltal[i-offset] == 0:
            del heltal[i-offset]
            offset += 1

def _6_5():
    # kontantkort, lägsta pris
    namn = []
    pris = []
    while True:
        s = input('namn och pris för ett kort: ')
        if s=='':
            break

        stup = s.rpartition(" ")
        print(stup)

        namn.append(stup[0])
        pris.append(float(stup[2]))
    m = min(pris)
    k = pris.index(m)
    print(namn[k] + ' är billigast')
    print(f'kostnad: {m:1.2f} kr/mån')


_6_5()