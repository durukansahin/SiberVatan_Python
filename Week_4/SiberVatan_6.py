'''
meyveler=["elma","kivi","limon","böğürtlen"]
print(meyveler[2])
print(meyveler)
'''
'''
sayilar=[10,20,30,40,50]
'''
# sayilar[0]+=sayilar[1]
# sayilar[1]+=sayilar[2]
# sayilar[2]+=sayilar[3]
# sayilar[3]+=sayilar[4]
#print(sayilar[4])
'''
toplam=0
for sayi in sayilar:
    toplam+=sayi
    
print(toplam)    
'''
'''
meyveler=["elma","kivi","limon","böğürtlen"]

for meyve in meyveler:
    print(meyve)
'''
'''
sayilar=[1,2,3,4,5,6,7,8,9,10]
for sayi in sayilar:
    if sayi%2==0:
        continue#'Continue' bu satırı atlayarak #print("Çift:",sayi)
    else:
        print("Tek :",sayi) 
'''        
'''    
sayi=int(input("Bir sayı giriniz"))    
sayac=0        
while sayac<=sayi:
    print(sayac)
    sayac+=1
'''

liste = []

sayac=1
adet=int(input("Kaç adet sayı girmek istiyorsun"))
while sayac <=adet:
    sayi=int(input("sayı gir")) 
    liste.append(sayi)
    sayac+=1
print("girilen sayılar:",liste)    





            
    




