age=input("What is your current age?\n")
age1 = int(age)
mjesec = 100*12
sedmica = 100*52
dan = 100*365
unesimjesec = age1*12
unesisedmica = age1*52
unesidan = age1*365
rezultatmjesec = mjesec - unesimjesec
rezultatsedmica = sedmica - unesisedmica
rezultatdan = dan - unesidan
print (f"You have {rezultatdan} days, {rezultatsedmica} weeks, and {rezultatmjesec} months left until 100 years of age.")


