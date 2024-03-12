'''
class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("Person Oluştu")
    def  ben_kimim(self):
        print("ben kişiyim")    

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch=branch
        print("Teacher Oluştu")
    def ben_kimim(self):
        print("ben öğretmenim")    
    

class Student(Person):
    def __init__(self,fname,lname,number):
        self.number=number
        Person.__init__(self,fname,lname)
        print("Student Oluştu")
    def ben_kimim(self):
        print("ben öclsğrenciyim")    
p1=Person(fname="Durukan",lname="Şahin")
print(p1)        
print(p1.fname)

t1=Teacher(fname="fadimana",lname="aladag",branch="Sınıf Ört")        
print(t1)
print(t1.fname,t1.lname,t1.branch)

s1=Student(fname="Abdulkadir",lname="Binan",number=1903)
print(s1)
print(s1.fname,s1.lname,s1.number)

p1.ben_kimim()
s1.ben_kimim()
t1.ben_kimim()#overreading, üzerine yazma 
'''
# class İşlem():
#     def __init__(self,sayi1,sayi2):
#         self.sayi1=sayi1
#         self.sayi2=sayi2
#     def sonucu_bulma(self):
#         pass    
    
# class Toplam(İşlem):
#     def __init__(self, sayi1, sayi2,toplam):
#         self.toplam=toplam
#         super().__init__(sayi1, sayi2)
#     def toplama(self):  
#         return self.sayi1+self.sayi2
               
# class Cikarma(İşlem):
#     def __init__(self, sayi1, sayi2,cikarma):
#         self.cikarma=cikarma
#         super().__init__(sayi1, sayi2,)
#     def cikarma(self):        
#         return self.sayi1-self.sayi2
          
# class Carpma(İşlem):
#     def __init__(self, sayi1, sayi2,carpma):
#         self.carpma=carpma
#         super().__init__(sayi1, sayi2)
#     def carpma(self):  
#         return self.sayi1*self.sayi2
        
# class Bölme(İşlem):
#     def __init__(self, sayi1, sayi2,bölme):
#         self.bölme=bölme
#         super().__init__(sayi1, sayi2)
#     def bölme(self):    
#         return self.sayi1/self.sayi2
# i1=İşlem(sayi1=25,sayi2=5)

# i1.sonucu_bulma()
# print(i1.sonucu_bulma())
  
'''        
class İşlem():
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
    def sonucu_bul(self):
        pass
class Toplam(İşlem):
    def sonucu_bul(self):
        return self.sayi1+self.sayi2
class Cikarma(İşlem):
    def sonucu_bul(self):
        return self.sayi1-self.sayi2
class Carpma(İşlem):
    def sonucu_bul(self):
        return self.sayi1*self.sayi2
class Bölme(İşlem):
    def sonucu_bul(self):
        return self.sayi1/self.sayi2
    
t1=Toplam(sayi1=25,sayi2=5)
print(t1.sonucu_bul())

c1=Cikarma(sayi1=25,sayi2=5)
print(c1.sonucu_bul())

c2=Carpma(sayi1=25,sayi2=5)
print(c2.sonucu_bul())

b1=Bölme(sayi1=25,sayi2=5)
print(b1.sonucu_bul())
'''
'''               
class Motor():
    def __init_(self,model,marka):
        self.model=model
        self.marka=marka 
class Power():
    def __init_(self,mpower):
        self.mpower=mpower
class Miras(Motor,Power):
    def __init__(self,mpower,model,marka,):
        Motor.__init__(self,model,marka)
        Power.__init__(self,mpower)
    def birlesim(self):
        return "Marka:",self.marka,"\nModel:",self.model,"\nMotor Gücü :",self.mpower          
m1=Miras(model="E60",marka="BMW",mpower=1500)

m1.birlesim()

class Arac:
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
    def arac_bilgi(self):
        print(f"marka: {self.marka} model: {self.model}")              
class Motor:
    def __init__(self,motor_gucu):
        self.motor_gucu=motor_gucu
    def motor_bilgi(self):
        print(f"motor gücü: {self.motor_gucu}")         
class Araba(Arac,Motor):
    def __init__(self,marka,model,motor_gucu):
        Arac.__init__(self,marka,model)
        Motor.__init__(self,motor_gucu)
    def araba_bilgi(self):
        self.motor_bilgi()
        self.arac_bilgi()
araba=Araba(marka="Mercedes",model="Cls",motor_gucu=1500)
araba.araba_bilgi()        

def floydüçgeni(satir):
    sayi=1 
    for i in range(satir):
        for e in range(i+1):
            print(sayi,end=" ")
            sayi+=1 
        print()         
satir=int(input("Kaç satırlık üçgen oluşsun?"))                   
floydüçgeni(satir)
'''
def floyd(satır):
    number=1
    for i in range(1,satır+1):
        for j in range(1,i+1):
            print(number,end=" ")
            number+=1
        print()    
satır=int(input("Kaç satırlık üçgen oluşsun?"))                   
floyd(satır)            
            
    





