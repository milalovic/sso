import pandas as pd
import numpy as np

data = pd.read_csv('ERPdata.csv', sep=',', decimal='.', header=0)
ljudi = data.values[:, 0]
akcija = data.values[:, 1]
podaci = data.values[:, 2:]


while(1):
    temp = 0
    pocetak = 1

    print("kontrolna grupa: 1-24, 59-66\nispitanici: 25-58, 67-81\nunesite redni broj osobe: ")
    x = int(input())

    for osoba in ljudi:
        if osoba == x:
            temp += 1

    for i in range(0, len(ljudi)):
        if ljudi[i] == x:
            pocetak = i + 1
            break

    osoba_klikce = pocetak
    osoba_slusa = 0
    osoba_nista = 0

    for i in range(0, len(ljudi)):
        if ljudi[i] == x:
            if (akcija[i] == 2) & (akcija[i - 1] != 2):
                osoba_slusa = i + 2
            elif (akcija[i] == 3) & (akcija[i - 1] != 3):
                osoba_nista = i + 2

    print("pocetna pozicija: ", pocetak, "\nkranja pozicija: ", pocetak + temp)
    print("\npocetak 3 akcije\nosoba klikce: ", osoba_klikce, "\nosoba slusa: ", osoba_slusa, "\nosoba nista: ",
          osoba_nista)

