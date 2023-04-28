class Adat():
    def __init__(self,sor):
        egy=sor.rstrip("\n").split(";")
        self.hegycsucs=egy[0]
        self.hegyseg=egy[1]
        self.magassag=int(egy[2])

f=open("hegyek.txt",encoding="utf-8")
be=f.readlines()
hegyek=[]
for x in be[1:]:
    egysor=Adat(x)
    hegyek.append(egysor)

#teszt
"""
for x in hegyek:
    
    print(x.hegyseg)
"""


hegyek_szama=len(hegyek)

print(f"3.feladat: Hegycsúcsok száma: {hegyek_szama}")

magassagok=[]

for x in hegyek:
    magassagok.append(x.magassag)
    

ossz_magassagok=sum(magassagok)

atlag= ossz_magassagok/hegyek_szama

print("4.feladat: Hegycsúcsok átlag magassága: {:.2f}".format(atlag),"m")

legmagasabb=max(magassagok)
print("5.feladat: A legmagasabb hegycsúcs adatai:")
for x in hegyek:
    if x.magassag==legmagasabb:
        print(f"Név: {x.hegycsucs}")
        print(f"Hegység: {x.hegyseg}")
        print(f"Magasság: {x.magassag}")
        

borzsony=[]
for x in hegyek:
    if x.hegyseg=="Börzsöny":
        borzsony.append(x.magassag)
beker=int(input("6.feladat: Kérem a magasságot:"))

van=False
for x in borzsony:
    if x>beker:
        van=True
if van:
    print(f"Van {beker} m-nél magasabb hegycsúcs a Börzsönyben!")
else:
    print(f"Nincs {beker} m-nél magasabb hegycsúcs a Börzsönyben!")
    
hegycsucsok_szama=0
for x in hegyek:
    if x.magassag>500:
        hegycsucsok_szama+=1
print(f"7.feladat: 500 m-nél magasabb hegycsúcsok száma: {hegycsucsok_szama}")


#8.feladat: magassagok.txt -- amiben a méterer egymás alatt!
"""
ki= open("magassagok.txt","w")
for x in magassagok:
    ki.write(str(x) + "\n")

ki.close()

print("A kiíratást befejeztem!")
"""

ki=open("otszaz.txt","w")
for x in hegyek:
    if x.magassag>500:
        ki.write(x.hegyseg + "\n")
ki.close()
print("A kiíratást befejeztem!")

    

        