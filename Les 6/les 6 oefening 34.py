
mijn_dictionary ={
    "Voornaam" : "Harry",
    "Geboortedatum" : "31-maart-139",
    "Registratienummer" : "AA18891"
}
mijn_dictionary["Achternaam"]= "de Vries"
mijn_dictionary.popitem()
print()
for k, v in mijn_dictionary.items():
    print (k, v)