
sayi1= 42
sayi2= -17
print(type(sayi1))#Burada bize sayi1 in değişken tipini vericek o da "int" yani tam sayı olacak olacak
print(type(sayi2))#Burada bize sayi2 nin değişken tipini vericek o da "int" yani tam sayı olacak

sayi3= 3.5
sayi4= -5.5
print(type(sayi3))#Burada bize sayi3 ün değişken tipini vericek o da "float" yani ondalıklı syaı olacak 
print(type(sayi4))#Burada bize sayi4 ün değişken tipini vericek o da "float" yani ondalıklı syaı olacak

dogru_mu= True
yanlis_mi= False
print(type(dogru_mu))#Burada bize dogru_mu nun değişken tipini vericek o da "bool" yani true ya da false mu olacak
print(type(yanlis_mi))#Burada bize yanlis_mi nin değişken tipini vericek o da "bool" yani true ya da false mu olacak

sayi_float= float(sayi1)#Burada int olan sayi1 değişkenini float değer olarak sayi_float değişenine atadı
print("int to float",sayi_float)

sayi_int= int(sayi3)#Burada float olan sayi3 değişkenini int değer olarak sayi_int değişenine atadı
print("float to int",sayi_int)

sayi_bool= int(dogru_mu)#Burada bool olan  dogru_mu değişkenini int değer olarak sayi_bool değişenine atadı
sayi_bool1= int(yanlis_mi)#Burada bool olan  yanlis_mi değişkenini int değer olarak sayi_bool1 değişenine atadı
print("bool to int",sayi_bool)
print("bool to int",sayi_bool1)
print(type(sayi_bool))

kullanici_ad= input("Lütfen adınız giriniz : ")#kullanıcıdan girdi istiyor
print("Hoşgeldin",kullanici_ad)

sayi3=int(input("1.sayıyı giriniz"))
sayi4=int(input("2.sayıyı giriniz"))               # **
print(sayi3+sayi4)
'''
sayi5=input("Lütfen 1. sayıyı giriniz")
sayi6=input("Lütfen 2. sayıyı giriniz")
sayiint=int(sayi5)
sayi2int=int(sayi6)
print(sayiint+sayi2int)                             # Yukardaki ve aşağıdaki örnek '**' lı örneğe nazaran aynı ama farklı yollardan yapılmıştır

sayi7=input("Lütfen 1. sayıyı giriniz")
sayi8=input("Lütfen 2. sayıyı giriniz")
print(int(sayi7)+int(sayi8))

'''

