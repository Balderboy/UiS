import sys
import turtle

"""
#Temperaturer
#Tidligere temperaturer
tidligere_ute_temp_morgen_verdi = float(11)
tidligere_ute_temp_ettermiddag_verdi = float(19.5)

#Ber bruker om nye temperaturer
ny_ute_temp_morgen = input("Skriv inn ny temperatur om morgen:")
ny_ute_temp_ettermiddag = input("Skriv inn ny temperatur om ettermiddag:")
ny_ute_temp_morgen_verdi = float(ny_ute_temp_morgen)
ny_ute_temp_ettermiddag_verdi = float(ny_ute_temp_ettermiddag)

#Beregner forskjell mellom ny og tidlgiere temperatur
(forskjell_temp_morgen) = ny_ute_temp_morgen_verdi - tidligere_ute_temp_morgen_verdi
(forskjell_temp_ettermiddag) = ny_ute_temp_ettermiddag_verdi - tidligere_ute_temp_ettermiddag_verdi

#Sjekker om forskjellen er positiv eller negativ og skriver ut resultatet
if forskjell_temp_morgen > 0:
    print("Verdien har steget med", forskjell_temp_morgen)
elif forskjell_temp_morgen == 0:
    print("Verdien har ikke endret seg")
else:
    print("Verdien har sunket med", -forskjell_temp_morgen)

if forskjell_temp_ettermiddag > 0:
    print("Verdien har steget med", forskjell_temp_ettermiddag)
elif forskjell_temp_ettermiddag == 0:
    print("Verdien har ikke endret seg")
else:
    print("Verdien har sunket med", -forskjell_temp_ettermiddag)


#Billettpris (d)
#Sjekker om gyldig alder
while True:
    try:
        alder_int = int(input("hvor gammel er du? "))
        if alder_int > 0 or alder_int <= 122:
            break
        else:
            print("Ugyldig alder. Skriv inn et tall mellom 0 og 122")
    except ValueError:
        print ("Du må skrive et tall!")

#Angir priser ut fra alder
if alder_int < 4:
    print("Det er gratis for barn under 4 år")
elif alder_int < 17:
    print("Pris: 50 kroner")
elif alder_int < 35:
    while True:
        student_svar = input("Er du student? (ja/nei):").strip().lower()
        if student_svar in ("ja", "nei"):
            break
        print("ugyldig svar, skriv ja eller nei")
    er_student = (student_svar == "ja")
    if er_student:
        print("Studentpris: 55 kroner")
    else:
        print("Pris: 100 kroner")
elif alder_int < 67:
    print("Pris: 100 kroner")
else:
    print("Pris: 55 kroner")


#Endring i en serie av verdier (e)
start_verdi = float(input("Skriv inn en start-verdi (positiv verdi): "))
while True:
    ny_verdi = float(input("Skriv inn en ny verdi (negativ verdi for å avslutte): "))
    endring = start_verdi + ny_verdi
    print("Endringen mellom de siste to verdiene er:", endring)
    start_verdi = start_verdi + ny_verdi
    if ny_verdi < 0:
            break

#Oppgave g
while True:
    try:
        tall_streng = input("Skriv inn et tall for en måned: ")
        maaned = int(tall_streng)
        if maaned < 1 or maaned > 12:
            print("ugyldig måned, prøv igjen")
        elif maaned <=2 or maaned == 12:
            print("vinter") 
        elif maaned <=5:
            print("vår")
        elif maaned <=8:
            print("sommer")
        else:
            print("høst")
    except ValueError:
        print("Ugyldig input, skriv inn et tall mellom 1 og 12")


#Oppgave h
def tegn_mangekant(antall_sider: int,  side_lengde: float):
    t = turtle.Turtle()
    t.speed(1)
    t.pensize(2)
    vinkel = 360 / antall_sider
    for _ in range(antall_sider):
        t.forward(side_lengde)  
        t.left(vinkel)   

def main():
    # Be brukeren om antall kanter
    try:
        n = int(input("Antall kanter (minst 3): "))
    except ValueError:
        print("Ugyldig input: skriv et heltall, tulling.")
        sys.exit(1)

    if n < 3:
       print("Feil: Antall kanter må være minst 3. Avslutter program.")
       sys.exit(1)
    #Tegne mangekanten
    screen = turtle.Screen()
    side_lengde = max(20, 400 / n)
    tegn_mangekant(n, side_lengde)
    screen.exitonclick()

if __name__ == "__main__":
    main()

#Oppgave i
Start med å skrive et Python script som tegner fire
sirkler som oppgitt i figur 1 under. Man kan gjøre dette ved å rotere skilpadda 90
grader mellom hver sirkel. Skriv deretter et script som tegner fire sirkler på denne
måten flere ganger med større og større sirkler hver gang. Roter litt, for eksempel
10 grader, mellom hver gang. Eksperimenter med mønstrene du får med å bruke
ulike rotasjonsvinkler og ulike antall sirkler av ulik størrelse. Du kan for eksempel
få mønsteret oppgitt i figur 2 under.


def tegn_sirkel(t: turtle.Turtle, radius: float):
    t.circle(radius)
    
def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    radius = 20
    antall_sykluser = 10
    antall_sirkler = 4
    for _ in range(antall_sykluser):
        for i in range(antall_sirkler):
            tegn_sirkel(t, radius)
            t.right(90)
        radius += 5
        t.right(10)
    screen.exitonclick()
    
if __name__ == "__main__":
    main()
"""