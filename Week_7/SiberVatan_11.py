'''
def sayikontrol(sayi):
    rakam_str = str(sayi)
    if len(set(rakam_str))==1:
        return 1
    else:
        return 0

a=[233,45,777,999999,36,90,88,11,61]
for sayi in a:
    if sayikontrol(sayi):
        print(f"{sayi}:basamakları aynı")
    else:
         print(f"{sayi}:basamakları farklı") 
'''           
'''
print("############################")
liste=[10,20,30]
# print(type(liste))
class Person:
    address = "bilgi yok"
    bornyear = "bilgi yok"
    def __init__(self,name,lname,bornyear):
        self.name = name
        self.lname = lname
        self.bornyear =bornyear
    def intro(self):
        print("merhaba ben "+self.name+"",self.lname+" ben şu yılda doğdum:",self.bornyear)
    def hesap(self):
        hes=(2024-self.bornyear)
        print("Benim yaşım:",hes)    
            
p1 = Person(name="Ali",lname="KOÇ",bornyear=1956)
# print(p1)
# print(type(p1))        
# print("benim adım:",p1.name)
# print("benim adresim:",p1.address)
# print("benim adım:",p1.name,"\nbenim soyadım:",p1.lname,"\nbenim adresim:",p1.address)
p2 = Person(name="Durukan",lname="ŞAHİN",bornyear=2008)
# print(p2)
# print("benim adım:",p2.name)
p1.intro()
p2.intro()
p2.hesap()
p1.hesap()
'''
# class Person1:
#     address = "bilgi yok"
    
#     def __init__(self,name,lname,tel):
#         self.name = name
#         self.lname = lname
#         self.tel = tel
# p1 = Person1(name="Durukan",lname="Şahin",tel="+9005464436314",)
# print("adım:",p1.name,"\nsoyadım:",p1.lname,"\nadresim:",p1.address,"\ntelefon numaram",p1.tel)

# class Daire:
#     def __init__(self,pi,r):
#         self.pi=pi
#         self.r=r       
#     def çevrealan(self):
#         cevre=2*(self.pi*self.r)
#         alan=(self.pi*(self.r*self.r))
#         print("Çevre:",cevre,"\nAlan :",alan)
# p1=Daire(pi=3.14,r=10)
# p1.çevrealan()        
''' 
class Daire:
    pi= 3.14
    def __init__(self,yarıcap):
        self.yarıcap=yarıcap
    def cevre_hesaplama(self):
        return 2*self.pi*self.yarıcap
    def alan_hesaplama(self):
        return self.pi*(self.yarıcap*self.yarıcap)
daire1=Daire(5)

print("çevre=",daire1.cevre_hesaplama(),"\nalan=",daire1.alan_hesaplama())
'''

class Square:
    def __init__(self,kenar):
        self.kenar=kenar
    def hesaplama(self):
        return self.kenar*self.kenar
kare1=Square(5)
print("Karenin Alanı:",kare1.hesaplama())        
                    
