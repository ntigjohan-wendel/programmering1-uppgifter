def _5_1():
    print("\u265A \u03C0")

def _5_2():
    text = input("Text: ")
    if text[0] == text[len(text)-1]:
        print("Första och sista bokstaven är samma.")

def _5_3():
    text = "pytonorm"
    s1 = text[2:5]
    s2 = text[4:]
    s3 = text[4:1:-1]
    print(s1, s2, s3)

def _5_4():
    s = input('Skriv en text: ')
    i = 0
    currI : int = None
    for c in s:
        if c == ' ' or c == '\t':
            currI = i
        i = i + 1
    if i < len(s) or currI != None:
        print(f'Sista vita tecknet fanns på plats nr {currI}')
    else:
        print('Inget vitt tecken')

def _5_5():
    s = input('Skriv en text: ')
    i = 0
    for c in range(len(s)):
        c = s[c]
        if c == ' ' or c == '\t':
            break
        i = i + 1
    if i < len(s):
        print(f'Första vita tecknet fanns på plats nr {i}')
    else:
        print('Inget vitt tecken')

def _5_6():
    dSE = input("Datum på formen åååå-mm-dd: ")
    d_d = dSE[8:10]
    d_m = dSE[5:7]
    d_y = dSE[:4]
    dUS = f"{d_m}/{d_d}/{d_y[2:4]}"
    print(f"Datum på formen mm/dd/åå: {dUS}")