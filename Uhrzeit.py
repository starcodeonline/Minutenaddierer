# Zu einer Uhrzeit werden beliebig viele Minuten dazugezählt

#################################################################
# Die Uhrzeit wird definiert:Stunden, Minuten. 
# Zusätzlich auch den Summand(Minuten die dazugezählt werden können)
def Uhrzeit_Minuten_Addieren(Stunden,minuten,summand):                                                                     
#################################################################
# Die Minuten werden mit den zusätzlichen Minuten zusammengerechnet  
    y = (minuten + summand)                                                                                                         
  
#################################################################
# Die Uhrzeit wird ausgegeben  
    if y>10:                                                                                                                          
        print(Stunden,":",y,"Uhr")
 
#################################################################
# Wenn die Minuten nicht zweistellig sind (>10) 
# wird noch eine 0 als Stelle zuvor dazugestellt
    elif y<10:
        print(Stunden,":","0",y,"Uhr")
    
##################################################################
# Beispiele die die Uhrzeit enthalten und den zusätzlichen Summand
Uhrzeit_Minuten_Addieren(10,10,5)                                                                       
Uhrzeit_Minuten_Addieren(20,10,4)
Uhrzeit_Minuten_Addieren(23,58,1)
Uhrzeit_Minuten_Addieren(15,8,1)
Uhrzeit_Minuten_Addieren(22,2,2)
Uhrzeit_Minuten_Addieren(11,1,1)
