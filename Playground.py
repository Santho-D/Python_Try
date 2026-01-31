gehalt = 0
gehälter = [1800,2200,2500,2900]

def steuer (gehalt):
    if gehalt >= 2500 :
        gehalt_netto = gehalt * 0.78
        return gehalt_netto
    else :
        gehalt_netto = gehalt * 0.82
        return gehalt_netto

for gehalt in gehälter:
    print (f"Brutto: {gehalt}\nNetto: {steuer(gehalt)}\n")