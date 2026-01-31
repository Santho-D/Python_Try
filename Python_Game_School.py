import random
random.seed()

c = 0
versuch = 0
richtig = 0
anzahl = -1
zahl = c+1
while anzahl <1 or anzahl > 10:
    try:
        print ("Wie viele Aufgaben: ")
        anzahl = int (input())

    except :
        continue 

for aufgabe in range (1,anzahl + 1):
    opzahl = random.randint (1,4)
    if opzahl == 1:
        a = random.randint (-10,30)
        b = random.randint (-10,30)
        op = "+"
        c = a + b 
    elif opzahl ==2:
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "-"
        c = a - b
    elif opzahl == 3 :
        a = random.randint(1,10)
        b = random.randint(1,10)
        op = "*"
        c = a * b
    elif opzahl == 4:
        c = random.randint(1,10)
        b = random.randint(1,10)
        op = "/"
        a = c * b

    print (f"Aufgabe {anzahl} von {anzahl}: {a}{op}{b} =  ")
    for versuch in range (1,4):
        try :
            print("Bitte Lösungsvorschlag eingeben:")
            zahl = int(input())
        except :
            print("Sie haben keine ganze Zahl eingegeben")
            continue
        if zahl == c :
            print (zahl, "ist richtig!")
            richtig = richtig +1
            break
        else:
            print (zahl, "ist richtig!")

print (f"Richtig: {richtig} von {anzahl}")