
x = 15 + 3*(12+9)
print(x*3 - 25)

#Konverteringsfaktor
fot = 0.3048 

#Gjør om fot til meter
Antallfot = input("skriv inn antall fot:")
AntallfotVerdi = float(Antallfot)
Antallmeter = AntallfotVerdi * fot
print(Antallfot, "fot tilsvarer", Antallmeter, "meter")

#Gjør om meter til fot
Antallmeter2 = input("skriv inn antall meter:")
Antallfot2 = float(Antallmeter2) / fot
print(Antallmeter2, "meter tilsvarer", Antallfot2, "fot")


#Befolkning
start_befolkning = int(7800000000)
befolkningsokning_i_prosent = float(1.1)
antall_aar = int(75)

endelig_befolkning = int(start_befolkning * (1.0 + befolkningsokning_i_prosent/100)**antall_aar)

print(endelig_befolkning)
