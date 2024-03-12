'''
open("yeni dosya.txt","w")

"w" Write -> yazma modu, yoksa oluşturu, içeriği silip ekleme yapar
"a" Append -> ekleme modu 
"x" Create -> oluşturma modu, aynısı varsa hata verir
"r" Read -> okuma modu 

file=open("yeni dosya.txt","w")
print(file)
file.close()

file_dizin=open("C:/Users/Lenovo/Desktop/masaüstüdosyası.txt","w")
file_dizin.close()

file=open("yeni dosya.txt","w",encoding='utf-8')#utf-8 türkçe karakterleri tanımlıyoruz
file.write("Durukan Şahin")
file.close()

file=open("yeni dosya.txt","a",encoding='utf-8')
file.write("\nBeşiktaş\nTanrı Türkü Korusun")
file.close()



try:
    file=open("yeni dosya.txt","w",encoding='utf-8')
except FileNotFoundError:
    print("Dosya okunamadı")
except FileExistsError:
    print("Dosya zaten var")    
#else:
    #print("folder oluşturma başarılı")
finally:
    print("folder oluşturma başarılı")      
    #file.close()
'''
'''    
file=open("yeni dosya.txt","r",encoding='utf-8')    
for i in file:
    print(i,end="")
    
içerik=file.read()
print(içerik)
'''
'''
file=open("yeni dosya.txt","r",encoding='utf-8') 
içerik_karakter = file.read(0)
içerik_karakter = file.read(15)
print(içerik_karakter)
print("###########")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")

liste = file.readlines()
print(liste[0])
print(liste[1])
print(liste[2])
file.close()

with open("yeni dosya.txt","r+",encoding='utf-8') as file:
    content=file.read()
    print(content)
    file.seek(10)
    print(file.tell())
    content1=file.read()
    print(content1)
    
with open("yeni dosya.txt","w",encoding="utf-8") as file:
    file.seek(20)
    file.write("siber vatan") 
index=1      
citylist=['karabük','bayburt','izmir']    
with open("yeni dosya.txt","a",encoding='utf-8') as file:
    for i in citylist:
        if index==len(citylist):
            file.write(i)
        else:
            file.write(i+"\n")
        index+=1        
import math as islem
sonuc=islem.sqrt(144)
print(sonuc)

sonuc=islem.factorial(5) 
print(sonuc)
from math import factorial
print(factorial(5))
'''
'''
from math import *  #*=everything
print(factorial(5))
print(sqrt(5))
print(factorial(5))         
'''
'''
import random
sonuc= random.random()
print(sonuc)
import random
sayilar=[0,1,2,3,4,5,6,7,8]
list=[]
i=0
while i!=6:
    list+=str(sayilar[random.randint(0,len(sayilar)-1)])
    i+=1
print(list)


import random
sayilar=[0,1,2,3,4,5,6,7,8]
list=""
i=0
while i!=6:
    list+=str(random.choice(sayilar))
    i+=1
print(list)

import random
sayilar=[0,1,2,3,4,5,6,7,8]
list=[]
i=0
while i!=6:
    list.append(random.choice(sayilar))
    i+=1
print("before",list)    
random.shuffle(list)    
print(list)

import math
print(math.pow(6,6))
'''
''' 
import Siber  
sayi=Siber.sayimiz[2]
print(sayi)

sayi1=Siber.number
print(sayi1)
#'pypi.org' python kütüphaneleri var
'''
