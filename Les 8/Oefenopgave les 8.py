a = 10
def maal_drie(a):
    return a * 3

def mijn_functie(a):
    a = maal_drie(a)
    uitvoer = maal_drie(a)
    return uitvoer * 2

print(mijn_functie(20))
    