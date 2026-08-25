def _2_2():
    tal = float(input("Tal: "))
    print(f"I kvadrat: {tal**2}")

def _2_4():
    sida = float(input("Kvadratens sida: "))
    omkrets = sida * 4
    area = sida**2
    print(f"Area: {area}cm2\nOmkrets: {omkrets}")

def _2_5():
    pris_moms = float(input("Pris: ")) # Inklusive moms
    moms_satts = int(input("Momssatts: ")) # %
    moms = pris_moms*moms_satts*0.01 # kr
    pris = pris_moms-moms # kr
    print(f"Moms: {moms}kr\nPris före momssatts: {pris}")

def _2_6():
    tid_sek = int(input("Tid i sekunder: "))

    tim = tid_sek/3600
    tim_diff = round(tim) - tim

    min = tim_diff/60
    min_diff = round(min) - min

    sek = min/60
    
    #print(f"{tim_hela} timmar | {min_hela} minuter | {sek} sekunder")

def _2_7():
    pass

_2_6()