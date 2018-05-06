#OTKRIVA NAM NA KOJIM POZICIJAMA SE NALAZI BROJ U LISTI:



niz=[1,2,3,4,5,1,7]
broj=1
pozicije=[]

for i in range(len(niz)):
    print(i)
    if niz[i]==broj:

        pozicije.append(i)

print(pozicije)