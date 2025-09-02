#Tidligere temperaturer
tidligere_ute_temp_morgen_verdi = float(11)
tidligere_ute_temp_ettermiddag_verdi = float(19.5)

#Ber bruker om nye temperaturer
ny_ute_temp_morgen = input("Skriv inn ny temperatur om morgen:")
ny_ute_temp_ettermiddag = input("Skriv inn ny temperatur om ettermiddag:")
ny_ute_temp_morgen_verdi = float(ny_ute_temp_morgen)
ny_ute_temp_ettermiddag_verdi = float(ny_ute_temp_ettermiddag)

#Beregner forskjell mellom ny og tidlgiere temperatur
forskjell_temp_morgen = ny_ute_temp_morgen_verdi - tidligere_ute_temp_morgen_verdi
forskjell_temp_ettermiddag = ny_ute_t emp_ettermiddag_verdi - tidligere_ute_temp_ettermiddag_verdi

ddeeprint("Forskjell mellom ettermiddagstempteraturene er", forskjell_temp_ettermiddag, "grader celcius")
