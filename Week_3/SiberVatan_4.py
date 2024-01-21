#1- liste : sıralı değitirilebirir

liste = [1,2,3,4,5]
print(liste)
print(liste[4])
print(type(liste))

liste[4]=35
print(liste)
print(liste[4])

alt_liste= liste[2:4] #Başlangıç dahil sonuncu hariç 
print(alt_liste)

#2- tuple : sıralı değistirilmez

tuple = (10,20,30,40)
print(tuple)
print(tuple[1])

#tuple[1]=50 #   böle bişey yapılamaz hata verir tuple değitirilemez 
print(tuple)
alt_tuple = tuple[1:4]
print(alt_tuple)

#3- kümeler : sırasız veriri ve birden fazla aynı değer yazılısa tek defa yazayr
kume={100,200,300,400,500,100,200,500,400,100,"durukan","durukan"}
print(kume)
kume.add(700)
print(kume)
print(type(kume))
kume.update([800,900])
print(kume)

#4- dict dictionary sözlük
dict={"anahtar1":"deger1","anahtar2":"deger2"}
print(dict)

deger = dict['anahtar1']
print(deger)

dict=set(dict)
print(dict)


dict_key=dict["anahtar1","anahtar2"]
print(dict_key)
dict=list(dict)
print(dict)

list_values=list(dict.values())
list_keys=list(dict.keys())
print(list_values,list_keys)
print(type(list_keys))
print(type(list_values))

sayilar = [10,8,5,3,15,10]
en_buyuk=max(sayilar)
en_kucuk=min(sayilar)
print(en_buyuk)
print(en_kucuk )
sayilar.append(20)
sayilar.append(1)
yeni_en_buyuk=max(sayilar)
yeni_en_kucuk=min(sayilar)
print(yeni_en_buyuk)
print(yeni_en_kucuk)
print(sayilar)

sayilar.pop() # FIFO \ LIFO mantığından pop LIFOya girer (FIFO:First İn First Out / LIFO:Last İn First Out) 
print(sayilar)

sayilar.sort() # küçükte büyüğe sıralar
print(sayilar)

sayilar.reverse()
print(sayilar) # büyükten küçüğe sıralar

print(sayilar.count(10)) # içerisine 10 saysısının kaç tane olduğunu veriri

aralik = range(1,100) #1 dahil 100 dahil değil
print(list(aralik))

import random

rastgele_sayi=random.randint(1,100)#random kütüphanesinden (randint):random dan bir int sayı verir
print("tutulan sayi :",rastgele_sayi)
