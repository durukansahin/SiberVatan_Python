'''
liste=[]
listeson=[]
sayac=0
for i in range(0,5):
    
    liste1=int(input("Sayı gir:"))
    if liste1%3==0:  
        liste.append(liste1)
    else:
        listeson.append(liste1)
            
    sayac+=i
# print(liste)
# print(listeson)
listebirlesim=liste+listeson
print(listebirlesim) 
#####################################
toplam =5 
liste=[]
for i in range(toplam):
    deger = int(input("Sayı gir:"))
    if deger % 3 == 0:
        liste.insert(0,deger)        
    else:
        liste.append(deger)
print("yeni liste:",liste)             
###################################
# sorsay=3
#     for i in range(sorsay):
#         soru=input("Başkent Neresidir ?") 

class Kisi:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
k1 = Kisi(name="Durukan",age=16)
print(k1)

liste=[]
class Soru:
    def __init__(self,soru,cevap,tahmin):
            self.tahmin = tahmin
            self.soru = soru
            self.cevap = cevap 
o1 = Soru(soru=input("Başkent neresidir?"),cevap="Ankara",tahmin=input(""))
liste.append(o1.soru)
print(liste)
'''
class Soru:
    def __init__(self,soru,cevap):
        self.soru = soru
        self.cevap = cevap
    def dogru_mu(self,tahmin):
        return self.cevap == tahmin    
soru1 = Soru("Başkent neresi: ","Ankara")
soru2 = Soru("En kalabalık şehir: ","İstanbul")
soru3 = Soru("En güzel şehir: ","Konya")

sorular = [soru1,soru2,soru3]
dogru_cevaplar = 0
for i in sorular:
    cevap = input(i.soru)
    if i.dogru_mu(cevap):
        dogru_cevaplar+=1
print(f"doğru sayısı {dogru_cevaplar}")       
                  
