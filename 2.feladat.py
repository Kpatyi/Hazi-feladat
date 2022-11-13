#Kérjünk be 5 számot és írjuk ki azokat amelyek osztható 2-vel és 3-al is
for x in range(1,6,1):
  szam3=int(input("Kérem a számot:"))
  if szam3 %2 ==0 and szam3 %3 ==0 :
    print(szam3)
