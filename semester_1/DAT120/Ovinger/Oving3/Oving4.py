#Oppgave a
"""Skriv en funksjon som tar inn et tall som representerer en total og et tall som
representerer antall målinger. Funksjonen skal returnere gjennomsnitt, som er totalen
delt på antall målinger"""

def main_a():
    try:
        total = float(input("Skriv inn totalen: "))
        antall_malinger = int(input("Skriv inn antall målinger: "))
        if antall_malinger <= 0:
            print("Antall målinger må være større enn 0.")
            return
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")
        return
    gjennomsnitt = total / antall_malinger
    print(f"Gjennomsnittet er: {gjennomsnitt:.2f}")

#Oppgave b
"""Skriv om programmet fra øving 2 oppgave a-c slik at det
bruker unntakshåndtering til å håndtere at brukeren skriver inn noe som ikke er et lovlig
flyttall. Hvis brukeren skriver inn noe som ikke er et lovlig flyttall skal brukeren få beskjed
om det og få prøve på nytt."""

main_b():
    tidligere_ute_temp_morgen_verdi = float(11)
    tidligere_ute_temp_ettermiddag_verdi = float(19.5)
    #Ber bruker om nye temperaturer
    while True:
        try:
            ny_ute_temp_morgen_verdi = float(input("Skriv inn ny temperatur om morgen:"))
            ny_ute_temp_ettermiddag_verdi = float(input("Skriv inn ny temperatur om ettermiddag:"))
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn tall.")
        break
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

#Oppgave c
"""Ei fil med vindmålinger fra Sola værstasjon for perioden august 2024 til
august 2025 er lagt ved oppgaven. Fila heter «max_vind_sola_2024_2025_enkelttall.txt»
og inneholder data hentet fra Meteorologisk Institutt, men redigert og forenklet for å
passe til oppgaven. Å håndtere den opprinnelige fila vil være en frivillig
mengetreningsoppgave til øving 5. Du skal skrive et script som:
a. Lese hver linje i fila
b. Konverterer hver linje fra en streng til en float
c. Regner ut maksimal vind for alle målingene i fila
d. Regner ut gjennomsnittlig vind. Du kan gjøre dette ved å summere alle målingene
og telle antall målinger. Deretter bruker du funksjonen fra oppgave a) for å regne
ut gjennomsnittet
e. Etter at programmet har gått gjennom hele fila, skriv ut resultatene som tekst
med print-setninger."""

main_c():



def velg_oppgave():
    while True:
        oppgave_valg = input("Velg oppgave (a, b, c, d) eller 'q' for å avslutte:").strip().lower()
        if oppgave_valg == "a":
            main_a()
        elif oppgave_valg == "b" or oppgave_valg == "c":
            main_b()
        elif oppgave_valg == "d":
            main_d()
        elif oppgave_valg == "e" or oppgave_valg == "f":
            main_e()
        elif oppgave_valg == "g":
            main_g()
        elif oppgave_valg == "h" or oppgave_valg == "i":
            main_h()
        elif oppgave_valg == "j" or oppgave_valg == "k":
            main_j()
        elif oppgave_valg == "l":
            main_l()
        elif oppgave_valg == "q":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg, skriv en bokstav")

velg_oppgave()
        