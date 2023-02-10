#1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a  legkisebb értéket ezek közül!
"""
szam=int(input("Kérem a számot:"))
szam1=int(input("Kérem a számot:"))
szam2=int(input("Kérem a számot:"))
if szam <szam1 and szam<szam2:
    print(szam)
else:
    if szam1<szam and szam1<szam2:
        print(szam1)
    else:
        if szam2<szam and szam2<szam1:
            print(szam2)

#2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy három különböző értéket kapott-e!
szam3=int(input("Kérem a számot:"))
szam4=int(input("Kérem a számot:"))
szam5=int(input("Kérem a számot:"))
if szam3!= szam4 and szam3!=szam5 and szam4!=szam5:
    print("Az értékek különbőzőek")
else:
    print("Az értékek nem különbözőek")

#3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.
pontszam=int(input("Kérem a pontszámot:"))
if pontszam <50:
    print("Az érdemjegy 1-es")
else:
    if 50<=pontszam<60:
        print("Az érdemjegy 2-es")
    else:
        if 60<= pontszam <70:
            print("Az érdemjegy 3-mas")
        else:
            if 70<=pontszam<85:
                print("Az érdemjegy 4-es")
            else:
                if pontszam >=85:
                    print("Az érdemjegy 5-ös")

#4. Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre, hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!
szam=int(input("Kérem a számot:"))
if szam %3==0 or szam %5==0:
    print("A szám osztható 3-mal vagy 5-tel")
else:
    print("A szám nem osztható 3-mal vagy 5-tel")

#5. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre, hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!
szam6=int(input("Kérem a számot:"))
szam7=int(input("Kérem a számot:"))
szam8=int(input("Kérem a számot:"))
if szam6+szam7==szam8:
    print("Az első és a második szám összege egyenlő a harmadikkal")
else:
    if szam6+szam8==szam7:
        print("Az első és a harmadik szám összege egyenlő a másodikkal")
    else:
        if szam8+szam7==szam6:
            print("A második és a harmadik szám összege egyenlő az elsővel")

#6. Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a képernyőre, hogy mind a három páros szám-e (igen/nem)!
szam9=int(input("Kérem az egész számot:"))
szam10=int(input("Kérem az egész számot:"))
szam11=int(input("Kérem az egész számot:"))
if szam9%2==0 and szam10 %2==0 and szam11%2==0:
    print("Mind a három szám páros")
else:
    print("Nem mind a három szám páros")

#7. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!
szam=int(input("Kérek egy pozitív számot:"))
x=1
while szam>x>0 :
    x+=1
    if x %3==0:
        print(x)

#8.Írj egy Python programot, amely bekér egy valós (A) és egy egész (K) számot a felhasználótól és kiírja a képernyőre az AK hatvány értékét anélkül, hogy használnád a ** operátort
A=float(input("Kérek egy egész számot:"))
K=int(input("Kérek egy valós számot:"))
hatvany=A**K
print(hatvany)

#9. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi a megadott szám értéke!
szam12=int(input("Kérek egy 20-nál nem nagyobb pozitív egész számot:"))
szam13=szam12*" "
print(szam13,"START")

#12.Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között
szam14=float(input("Kérek egy kisebb pozitív valós számot:"))
szam15=float(input("Kérek egy nagyobb pozitív valós számot:"))
while szam15 >szam14:
    szam14=szam14+1
    print(szam14)

#13. Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban találhatóak!
szam16=int(input("Kérek egy számot:"))
szam17=int(input("Kérek egy szamot:"))
while szam16 > szam17:
    szam17+=1
    if szam17%2==0:
        print(szam17)
while szam17>szam16:
    szam16+=1
    if szam16%2==0:
        print(szam16)

#27. Írj egy Python programot, amelyben megadsz egy tetszőleges egészeket tartalmazó listát, majd a lista elemeit csökkenő sorrendbe rendezed anélkül, hogy használnád a sort() metódust.
lista=[1,2,40,60,200,50]
lista.sort()
lista.reverse()
print(lista)
"""