"""upráva načítacího skriptu na grafickou část"""

name = input("jméno souboru: ")

with open ("C:/py/"+name+".mux", "r", encoding="utf-16") as f:
    i = 0

    #obsahuje současný řádek
    pomocna = []
    #obsahuje x souřadnice
    x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    
    for line in f:
        i = i + 1
        if i > 6:
            #to co se ukládá do jednoho řádku, obsahuje y hodnoty
            test = []
            pomocna = line.split()
            x.append(pomocna[0])
            for j in range(1, len(pomocna)+1):
                if (j+1) % 2 == 0:
                    #pokud je to druhá věc tak ji zkopni
                    test.append(pomocna[j])
            #zapíše jenom třetí měření
            kazdytreti = []
            count = 0
            for thing in test:
                if count == 2:
                    kazdytreti.append(thing)
                    count = 0
                    continue
                count += 1
            #zapiš y1,y2,y3,y4,y5
            y1.append(kazdytreti[1])
            y2.append(kazdytreti[3])
            y3.append(kazdytreti[5])
            y4.append(kazdytreti[7])
            y5.append(kazdytreti[9])
                        
                    
"""                
plotting part
"""
import matplotlib.pyplot as plt

plt.plot(x, y1, 'b', x, y2, 'm', x, y3, 'g',x,y4,'y',x,y5,'r')
plt.ylabel("I/mA")
plt.xlabel("E/V")
plt.show()
