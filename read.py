name = input("jméno souboru: ")

csv = open("C:/py/data/"+name+".csv" , "w")
csv3 = open("C:/py/data/"+name+"3.csv","w")
csvref = open("C:/py/data/"+name+"r.csv","w")
"""ještě dopsat první line s nadpisama"""

with open ("C:/py/"+name+".mux", "r", encoding="utf-16") as f:
    i = 0

    #obsahuje současný řádek
    pomocna = []
    
    for line in f:
        i = i + 1
        if i > 6:
            #to co se ukládá do jednoho řádku, obsahuje y hodnoty
            test = []
            pomocna = line.split()
            #debug
            for j in range(1, len(pomocna)+1):
                if (j+1) % 2 == 0:
                    #pokud je to druhá věc tak ji zkopni
                    test.append(pomocna[j])
            #zapiš řádek do csv souboru
            csv.write(pomocna[0].replace(".",",")+";"+";".join(test).replace(".",",")+"\n")
            #zapíše jenom třetí měření
            kazdytreti = []
            count = 0
            for thing in test:
                if count == 2:
                    kazdytreti.append(thing)
                    count = 0
                    continue
                count += 1
            csv3.write(pomocna[0].replace(".",",")+";"+";".join(kazdytreti).replace(".",",")+"\n")
            #reference
            ref = []
            count = 0
            for i in range(0,len(kazdytreti),2):
                ref.append(str(float(kazdytreti[i+1])-float(kazdytreti[i])))
            csvref.write(pomocna[0].replace(".",",")+";"+";".join(ref).replace(".",",")+"\n")
                    
                    
                    
            
                    
"""                
        if i == 100:
            break
"""

print("Hotovo")
csv.close()
csv3.close()
csvref.close()




