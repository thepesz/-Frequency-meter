godzina_rozpoczecia = int(input("Podaj godzinę rozpoczęcia zajęć 0-24: "))
minuta_rozpoczecia = int(input("Podaj minute rozpoczęcia zajęć 0-60: "))
dlugosci_przerw = []
i=0
przerwa=1
while przerwa !=0:
    przerwa = int(input("Podaj długość przerwy: "))
    dlugosci_przerw.append(przerwa)

ilosc_przerw =len(dlugosci_przerw)-1

for i in range(0,len(dlugosci_przerw)-1):
    suma = minuta_rozpoczecia + dlugosci_przerw[i]
    if suma>60:
        godzina_rozpoczecia+=1
        minuta_rozpoczecia = suma - 60
        print(godzina_rozpoczecia + '.' + minuta_rozpoczecia)
        continue
    else:
        print(godzina_rozpoczecia + '.' + suma)
    





#print(suma_minut_lekcyjnych)
