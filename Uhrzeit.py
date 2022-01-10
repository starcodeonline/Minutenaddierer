

def Uhrzeit_Minuten_Addieren(Stunden,minuten,summand):      # oder so, wenn ohne If-Statements: def Uhrzeit_Minuten_Addieren(Stunden,minuten,summand):
    y = (minuten + summand)                                 #y=(minuten+summand)
    if y>10:                                                #print(Stunden,":",y)
        print(Stunden,":",y,"Uhr")
    elif y<10:
        print(Stunden,":","0",y,"Uhr")
    


Uhrzeit_Minuten_Addieren(10,10,5)                           # <-- Alles von da drüben auch
Uhrzeit_Minuten_Addieren(20,10,4)
Uhrzeit_Minuten_Addieren(23,58,1)
Uhrzeit_Minuten_Addieren(15,8,1)
Uhrzeit_Minuten_Addieren(22,2,2)
Uhrzeit_Minuten_Addieren(11,1,1)
