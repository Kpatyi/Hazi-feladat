#1.feladat: Bekérünk 5 darab egész számot és vizsgáljuk meg hány olyan szám van amely nagyobb mint 50

db=0
for x in range(1,6,1):
    szam=int(input("Kérem a számot:"))
    if szam>50:
        db+=1
print(f"{db} db szám volt amely nagyobb mint 50")
#2.feladat: Függvény segítségével: Bekérünk 10 egész számot amelyeket tárolunk listában a függvény adja vissza a legnagyobb é legkisebb különbségét
def kulonbseg():
    szamok=[]
    for x in range(1,11,1):
        szam=int(input("Kérem a számot:"))
        szamok.append(szam)
    legnagyobb=max(szamok)
    legkisebb=min(szamok)
    kulonbseg=legnagyobb-legkisebb
    return f"A számok közül a legnagyobb és legkisebb különbsége: {kulonbseg}"
print(kulonbseg())

#3.feladat:
#a) olvasuk be az adatok.txt-t
class Adat():
    def __init__(onmaga,sor):
        egy=sor.rstrip("\n").split(";")
        onmaga.nev=egy[0]
        onmaga.eletkor=int(egy[1])
        onmaga.hobbi=egy[2]
fajl=open("adatok.txt", encoding="utf-8")
be=fajl.readlines()
adatok=[]
for x in be:
    adatok.append(Adat(x))
#b) hány diák szerepel?
diakok=[]
for x in adatok:
    diakok.append(x.nev)
diak=0
for x in diakok:
    diak+=1
print(f"A diákok száma: {diak}")

#c) Ádámnak mi a hobbia
for x in adatok:
    if x.nev=="Ádám":
        print(f"Ádám hobbia: {x.hobbi}")
        
#d) Van e olyan diák aki be töltöte a 30. élét évét és ha igaz ki az
van_benne=False
oreg=""
for x in adatok:
    if x.eletkor>=30:
        van_benne=True
        oreg+=x.nev
if van_benne:
    print(f"Van aki betöltöte a 30. élet évét ő pedig: {oreg}")
else:
    print("Nincs aki betöltöte a 30. élet évét")
    
#e) átlag életkor 2 tizedes
osszeg=0
for x in adatok:
    osszeg+=x.eletkor
atlag=osszeg/diak
print("Az diákok átlag életkora: {:.2f}".format(atlag))
#Készhíts egy statisztika álomány.txt ahol csak a diákok szóköz hobbi szerepel
ki=open("statisztika.txt","w")
for x in adatok:
    ki.write(x.nev+" "+x.hobbi+"\n")
ki.close()