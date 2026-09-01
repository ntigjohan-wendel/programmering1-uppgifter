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

### Uppgifter från dokument

def _2_15():
    import random
    tärning_1 = random.randint(1,6)
    tärning_2 = random.randint(1,6)
    summa = tärning_1 + tärning_2
    print(f"Tärning 1: {tärning_1}\nTärning 2: {tärning_2}\nSumma: {summa}")

def _2_25():
    poäng_1 = float(input("Poäng 1: "))
    poäng_2 = float(input("Poäng 2: "))
    poäng_3 = float(input("Poäng 3: "))
    poängSumma = poäng_1+poäng_2+poäng_3
    poängMedel = poängSumma/3
    print(f"Summa: {poängSumma}\nMedelvärde: {poängMedel}")

# Svårare uppgifter för kapitel 2
def _2_s2():
    HEADER = "===== RESEKALKYLATOR ====="

    def strToFirstT(string: str, T: type) -> type:
        return T(string.split()[0])
    
    def input_ext(input_str: str, T: type) -> type:
        return strToFirstT(input(input_str), T)
    """
    INPUT:
        avstånd
        bilens förbrukning
        bensinpris
        antal personer
        eventuell kostnad för parkering
        eventuell kostnad för färja
        antal dagar
    OUTPUT:
        antal liter bensin
        bensinkostnad
        total resekostnad
        kostnad per person
        kostnad per dag
    """
    print(HEADER)
    # Input
    i_avstånd = input_ext("Avstånd: ", float)                       # avstånd (m)
    i_förbrukning = input_ext("Förbrukning: ", float)               # bilens förbrukning (liter)
    i_bensinpris = input_ext("Bensinpris: ", float)                 # bensinpris (kr)
    i_antal_personer = input_ext("Antal personer: ", int)           # antal personer
    i_kostnad_parkering = input_ext("Parkering: ", float)           # eventuell kostnad för parkering
    i_kostnad_färja = input_ext("Färja: ", float)                   # eventuell kostnad för färja
    i_antal_dagar = input_ext("Antal dagar: ", int)                 # antal dagar
    
    # Beräkningar
    bensin_liter        = i_avstånd * i_förbrukning                 # liter
    kostnad_bensin      = bensin_liter * i_bensinpris               # kr
    kostnad_per_person  = i_kostnad_färja * i_antal_personer        # kr
    total_resekostnad   = i_kostnad_färja + kostnad_bensin + (i_kostnad_färja * i_antal_personer) # kr
    kostnad_per_dag     = -1                                        # kr
    total_kostnad       = total_resekostnad + i_kostnad_parkering

    # Presentation
    print(f"Bensin: {bensin_liter} liter")
    print(f"Bensin kostar: {kostnad_bensin} kr")
    print(f"Total kostnad: {total_kostnad} kr")
    print(f"Per person: {kostnad_per_person} kr")

def _2_s3():
    pass
_2_s2()