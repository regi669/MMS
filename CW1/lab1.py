import os 
import numpy as np
import statistics as stat

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

dane_cale = []
with open(dir_path + '/lab1_dane.txt', 'r') as f:
    for line in f:
        if line.split():
            line = [float(x) for x in line.split()]
            dane_cale.append(line)

dane4 = []
dane1 = []
dane2 = []
dane3 = []
for item in dane_cale:
    dane1.append(item[0])
    dane2.append(item[1])
    dane3.append(item[2])
    dane4.append(item[3]) 

def policz_wartosci(items):
    liczebnosc = len(items)

    x_sr = round(np.mean(items), 2)
    var = round(np.var(items), 2)
    s = round(np.std(items), 2) 
    s_p = round(np.std(items, ddof=1), 2) 
    Q1 = round(np.percentile(items, 25), 2)
    M = round(np.percentile(items, 50), 2)
    Q3 = round(np.percentile(items, 75), 2)
    min = np.min(items)
    max = np.max(items)

    t1_l = round(x_sr - s, 2)
    t1_p = round(x_sr + s, 2)
    typowe1 = [x for x in items if (x > t1_l and x < t1_p)]
    ptypowe1 = round(len(typowe1)/len(items), 2)

    t2_l = round(x_sr - 2*s, 2)
    t2_p = round(x_sr + 2*s, 2)
    typowe2 = [x for x in items if (x > t2_l and x < t2_p)]
    ptypowe2 = round(len(typowe2)/len(items), 2)

    odstajace = [x for x in items if (x <= t2_l or x >= t2_p)]
    if(len(odstajace) == 0):
        odstajace = 'brak'

    Q = round((Q3-Q1)/2, 2)
    Ktypowe1_l = M-Q
    Ktypowe1_r = M+Q
    Ktypowe1 = [x for x in items if (x > Ktypowe1_l and x < Ktypowe1_r)]
    Ktypowe2_l = round(Q3 - 3*Q , 2)  
    Ktypowe2_r = round(Q3 + 3*Q)
    Ktypowe2 = [x for x in items if (x > Ktypowe2_l and x < Ktypowe2_r)]
    Kodstajace = [x for x in items if (x <= Ktypowe2_l or x >= Ktypowe2_r)]
    WspZmiennosci = round((s/x_sr), 2)
    Kwz = round((Q/M), 2)
    Kwa = round(((Q3 - M) - (M - Q1))/(2*(Q3 - Q1)), 2)
    Mas = round(3 * ((x_sr - M)/s), 2)
 
    print('1. Liczebnosc proby: ', liczebnosc) 
    print('2. Srednia: ', x_sr)  
    print('3. Wariancja populacji: ', var) 
    print('4. Odchylenie standardowe populacji: ', s) 
    print('5. Typowe 1: ', typowe1) 
    print('6. Procent wartosci typowe 1: ', ptypowe1) 
    print('7. Typowe 2: ', typowe2) 
    print('8. Procent wartosci typowe 2: ', ptypowe2) 
    print('9. Wartosci odstajace: ', odstajace)  
    print('10.  Klasyczny wspolczynnik zmiennosci: ', WspZmiennosci) 
    print('11.  Mediana: ', M)  
    print('12.  Kwartyl pierwszy: ', Q1) 
    print('13.  Kwartyl trzeci: ', Q3) 
    print('14.  Odchylenie cwiartkowe: ', Q) 
    print('15.  Kwartylowe typowe 1: ', Ktypowe1) 
    print('16.  Kwartylowe typowe 2: ', Ktypowe2) 
    print('17.  Kwartylowe wartosci odstajace: ', Kodstajace)  
    print('18.  Kwartylowy wspolczynnik zmiennosci: ', Kwz) 
    print('19.  Kwartylowy wspolczynnik asymetrii: ', Kwa) 
    print('20.  Mieszany wspolczynnik asymetrii: ', Mas) 

print('\n\nDane1\n\n')
policz_wartosci(dane1)
print('\n\nDane2\n\n')
policz_wartosci(dane2)
print('\n\nDane3\n\n')
policz_wartosci(dane3)
print('\n\nDane4\n\n')
policz_wartosci(dane4)