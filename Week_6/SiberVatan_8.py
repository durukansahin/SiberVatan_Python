''''
def faktoriyel(n):#def=defined
    if n==0:
        return 1
    else:
        return n*faktoriyel(n-1) #rikörsif fonksiyon
sayi=4

print(faktoriyel(sayi))
'''
'''
def faktoriyel(n):
    sayac=1
    for i in range(n):
        sayac*=i+1               #iteratif fonksiyon
    print(sayac)
    return sayac
n=int(input("fak gir:"))
faktoriyel(n)    
'''
'''
x="global eşişken"

def func():
    x="local değişken"
    print(x)
func()
print(x)    
'''
#print(a)#name eror
#int("a19")#value eror
#print(10/0)#zero divsion eror(sıfıra bölünme hatatsı)
#print('hello'world)#sntax eror

    
#**NOTT**: İDENT=GİRİNTİLEME    
import re    
def parola_kontrol(parola):
    if len(parola)<8:
        raise Exception("parola yanlış")    
    elif not re.search("[a-z]",parola):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]",parola):
        raise Exception("Parola büyük harf içermelidir")
    
pasword=input("Parola gir")
try:
    parola_kontrol(pasword)
except Exception as ex:
    print(ex)
else:
    print("parola oluşturma başarılı")
