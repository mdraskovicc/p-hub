import random
import math

def ucitaj_iz_fajla(naziv_fajla):
    x = []
    y = []
    with open(naziv_fajla, 'r') as file:
        for linija in file:
            kolone = linija.split()
            x.append(float(kolone[0]))
            y.append(float(kolone[1]))
    return x,y
    
def izmijesaj_liste(x,y,n):
    parovi = list(zip(x,y))
    random.shuffle(parovi)
    x1,y1 = zip(*parovi)
    return x1[:n],y1[:n]

def matrica_rastojanja(x, y):
    n = len(x)
    matrica = []
    for i in range(n):
        matrica.append([math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2) for j in range(n)])

    return matrica

def ispisi_fajl(matrica, naziv_fajla):
    with open(naziv_fajla, 'w') as file:
        for red in matrica:
            for x in red:
                file.write(f'{x : .4f} ')
            file.write('\n')

x,y = ucitaj_iz_fajla('koordinate.txt') 
velicine = [5, 10, 15, 20, 25]
for i in range(5):
    x1,y1 = izmijesaj_liste(x,y, velicine[i])
    matrica = matrica_rastojanja(x1, y1)  
    ispisi_fajl(zip(x1,y1), f'./nlp_instance/koordinate{i}.txt')
    ispisi_fajl(matrica, f'./nlp_instance/udaljenosti{i}.txt')

  

