def mijn_functie_1 (argument):
    tabel = {
        2: 4,
        4: 16, 
        10: 100,
        12: 144
    } 
    return tabel.get(argument, argument **2)
print(mijn_functie_1(2))
print(mijn_functie_1(4))
print(mijn_functie_1(10))
print(mijn_functie_1(12))
