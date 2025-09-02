

from asyncio import base_events
from pickle import TRUE
import sys
from tkinter import N
import turtle

#Oppgave a
def be_om_antall_linjer():
    try:
        antall_linjer = int(input("Skriv inn antall linjer i spiralen: "))
        if antall_linjer <= 0:
            print("Ugyldig input. Vennligst skriv inn et positivt heltall.")
            sys.exit(1)
        return antall_linjer
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn et positivt heltall.")
        sys.exit(1)

def tegn_spiral(antall_linjer: int):
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    for i in range(antall_linjer):
        t.forward(5 + i)
        t.right(90)

def main_a():
    antall_linjer = be_om_antall_linjer()
    screen = turtle.Screen()
    tegn_spiral(antall_linjer)
    screen.exitonclick()

#Oppgave b og c
def be_om_input():
    while True:
        s = input("Skriv inn et heltall (eller 'total' for å se summen og 'q' for å avslutte): ").strip().lower()
        if s == "total":
            return "total"
        elif s == "q":
            return "q"
        try:
            return int(s)
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et heltall eller 'total'.")
            return None
           
def sjekk_tall(n: int):
    if n > 0:
        print("Verdien har økt med", n)
    elif n < 0:
        print("Verdien har sunket med", abs(n))
    else:
        print("Tallet er null, verken økt eller sunket.")

def main_b():
    total = 0
    while True:
        verdi = be_om_input()
        if verdi == "total":
            print("Totalen av alle tallene er:", total)
        elif verdi == "q":
            print("Tilbake til meny")
            velg_oppgave()
        elif verdi is not None:
            sjekk_tall(verdi)
            total += verdi

#Oppgave d
def belop_etter_antall_aar(startbelop, rente_prosent, antall_aar):
    nytt_belop_ett_aar = 1.0 + (rente_prosent/100.0)
    resultat = startbelop*(nytt_belop_ett_aar**antall_aar)
    return resultat

def main_d():
    while True:
        try:
            startbelop = float(input("Skriv inn startbeløp: "))
            rente_prosent = float(4.5)
            antall_aar = int(input("Skriv inn antall år: "))
            if startbelop < 0 or rente_prosent < 0 or antall_aar < 0:
                print("Ugyldig input. Vennligst skriv inn positive verdier.")
                continue
            sluttbelop = belop_etter_antall_aar(startbelop, rente_prosent, antall_aar)
            print(f"Etter {antall_aar} år vil beløpet være: {sluttbelop:.2f}")
            velg_oppgave()
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn tall.")

#Oppgave e

def sirkel_input():
    while True:
        try:
            radius = float(input("Skriv inn radiusen til sirkelen: "))
            if radius < 0:
                print("Ugyldig input. Vennligst skriv inn en positiv verdi.")
                continue
            return radius
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")

def areal_av_sirkel(radius):
    pi = 3.14159
    areal = pi * (radius ** 2)
    return areal

def main_e():
    radius = sirkel_input()
    areal = areal_av_sirkel(radius)
    print(f"Arealet av sirkelen med radius {radius} er: {areal:.2f}")

#Oppgave g
def beregn_resistans(rho, lengde, areal):
    resistans = rho * (lengde / areal)
    return resistans

def beregn_spenningsfall(resistans, strom):
    spenningsfall = resistans * strom
    return spenningsfall

def main_g():  
    while True:
        try:
            rho = float(input("Skriv inn resistiviteten (i ohm meter): "))
            lengde = float(input("Skriv inn lengden på lederen (i meter): "))
            areal = float(input("Skriv inn tverrsnittsarealet (i kvadratmeter): "))
            strom = float(input("Skriv inn strømmen (i ampere): "))
            break
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn tall.")
    resistans = beregn_resistans(rho, lengde, areal)
    spenningsfall = beregn_spenningsfall(resistans, strom)
    print(f"Resistansen er: {resistans:.2f} ohm og spenningsfallet er {spenningsfall:.2f}")

#Oppgave h og i
def be_om_strom():
    while True:
        try:
            strom = float(input("Skriv inn strømmen (i meter per sekund): "))
            if strom < 0:
                print("Ugyldig input. Vennligst skriv inn en positiv verdi.")
                continue
            return strom
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")

def effekt_turbin(strom, tetthet=1000, turbin_effekt=0.3, diameter=1):
    radius = diameter / 2
    areal = areal_av_sirkel(radius)
    effekt = 0.5 * turbin_effekt * tetthet * areal * (strom ** 3)
    return effekt

def main_h():
    strom = be_om_strom()
    while True:
        s = input("Skriv inn turbintype (vann eller vind): ").strip().lower()
        if s in ("vann", "vind"):
            break
        print("Ugyldig turbintype. Vennligst skriv inn 'vann' eller 'vind'.")
        
    if s == "vann":
        vannturbin_effekt = effekt_turbin(strom, tetthet=1000, turbin_effekt=0.3, diameter=1)
        print(f"Effekten til vannturbinen er: {vannturbin_effekt:.2f} watt")
    else:
        vindturbin_effekt = effekt_turbin(strom, tetthet=1.29, turbin_effekt=0.3, diameter=1)
        print(f"Effekten til vindturbinen er: {vindturbin_effekt:.2f} watt")

# Oppgave j og k
def fot_til_meter(fot):
    meter = fot * 0.3048
    return meter

def main_j():
    while True:
        try:
            fot = float(input("Skriv inn antall fot: "))
            if fot < 0:
                print("Ugyldig input. Vennligst skriv inn en positiv verdi.")
                continue
            meter = fot_til_meter(fot)
            print(f"{fot} fot er {meter:.2f} meter.")
            break
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")

#Oppgave l
def input_int(prompt, min_verdi=None):
    while True:
        try:
            i = int(input(prompt))
            if min_verdi is not None and i < min_verdi:
                print(f"Ugyldig input. Vennligst skriv inn et heltall ≥ {min_verdi}.")
                continue
            return i
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et heltall.")

def input_float(prompt, min_verdi=None):
    while True:
        try:
            f = float(input(prompt))
            if min_verdi is not None and f < min_verdi:
                print(f"Ugyldig input. Vennligst skriv inn et tall ≥ {min_verdi}.")
                continue
            return f
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")

def stjerne(t: turtle.Turtle, antall_tagger: int, side_lengde: float):
    start_heading = t.heading()
    t.pensize(1)
    vinkel = 180 - (180 / antall_tagger)
    for _ in range(antall_tagger):
        t.forward(side_lengde)
        t.backward(side_lengde)
        t.left(vinkel)
    t.setheading(start_heading)

def galakse(t: turtle.Turtle,
            antall_tagger: int,
            side_lengde: float,
            antall_spiralarmer: int,
            antall_stjerner: int,
            steg_radius: float = 12.0,
            vri_per_stjerne: float = 12.0):
    for i in range(antall_stjerner):
        r = (i + 1) * steg_radius
        base_vinkel = i * vri_per_stjerne
        for a in range(antall_spiralarmer):
            t.penup()
            t.home()
            t.setheading(base_vinkel + a * (360 / antall_spiralarmer))
            t.forward(r)
            t.pendown()
            stjerne(t, antall_tagger, side_lengde)

def main_l():
    antall_tagger = input_int("Skriv inn antall tagger i stjernen (minst 3): ", 3)
    side_lengde = input_float("Skriv lengden på taggene: ", 1)
    antall_spiralarmer = input_int("Skriv antall spiralarmer: ", 1)
    antall_stjerner = input_int("Skriv antall stjerner per arm: ", 1)

    screen = turtle.Screen()
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0) 

    galakse(
        t,
        antall_tagger=antall_tagger,
        side_lengde=side_lengde,
        antall_spiralarmer=antall_spiralarmer,
        antall_stjerner=antall_stjerner,
        steg_radius=12,
        vri_per_stjerne=12

    )
    screen.exitonclick()
    

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