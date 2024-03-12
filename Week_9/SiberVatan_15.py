# mayıs 15, yarışma
'''
cumle=str(input("Lütfen Bir Kelime Giriniz"))
ters=(cumle[::-1])
if cumle==ters:
    print("palindrome bir kelime")
else:
    print("palindrome bir kelime değil")   
   
def palindrom_mu(metin):
    temiz_metin = metin.lower()
    return temiz_metin == temiz_metin[::-1]
metin = input("Metin giriniz: ")
if palindrom_mu(metin):
    print("palindom bir kelimedir")
else:
    print("palindom bir kelime değildir")        

def ortak_elemanlar(liste1,liste2):
    ortaklar = liste = []
    for i in liste1:
        if i in liste2:
            liste.append(i)
    return ortaklar        
liste1 = [1,2,3,4,5]   
liste2 = [3,4,5,6,7,]
ortaklar= ortak_elemanlar(liste1,liste2)
print("ortaklar: ",ortaklar)

def eleman_frekansi(liste):
    frekanslar = {}
    for eleman in liste:
        if eleman in frekanslar:
            frekanslar[eleman]+=1
        else:
            frekanslar[eleman] = 1
    return frekanslar             
 
liste_ornegi = [2,3,5,7,9,29,42,13,7,2,96,5]
sonuc=eleman_frekansi(liste_ornegi)
for eleman,frekans in sonuc.items():
    print(f"{eleman}:{frekans}")
    
n=int(input("Sayi gir"))
liste=[]
liste1=[]
for i in range(n+1):
    liste.append(i)
    i+=1
a=liste[0]
b=liste[1] 
print(len(liste))
for i in liste:
    top = a+b
    liste1.append(top)
    a+=1
    b+=1
    if b==len(liste):
        print(liste1)
        print(liste)
    else:
        continue    
'''    
def fibonacci(n):
    fibo = [0,1]
    
    for i in range(2,n):# i yerine '_' de kullanılabişir di çünkü forun içinde başka i kullanmadık 
        next = fibo[-1] + fibo[-2]
        fibo.append(next)
    return fibo 
n = 10
fibo = fibonacci(n)
print(f"{fibo}")    
        

    
