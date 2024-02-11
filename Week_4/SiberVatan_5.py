'''
a=90
b="Siber Vatan"

num1,num2,num3=5,55,65
print("Sayilaaar",num1,num2,num3)

num1=num1+50
num2=num2+55
num3=num3+90

num1+=num2
num1+=90
num1/=num2
'''
'''
numbers=(50,55,66)
#print(type(numbers))
num1,num2,num3,num4=numbers
print(num2)
print(num4) #hata verir çünkü yukarda tanımlı değil
'''
'''
a,b,c,d=50,100,50,75

sonuc=(a>b)
print(sonuc)

sonuc=(a==c)
print(sonuc)

sonuc=(a>d)
print(sonuc)

sonuc=(a!=c)
print(sonuc)


#(a < b)#a ve b operant '<' is operatördür
# print(a<b)
# print(str(a<b))
# print(int(a<b))
'''
'''
username1="Ceku"
username2="Arif"
print("A.R.O.G 'a hoş geldin.\n")
username_input=str(input("Adınızı Giriniz:"))


# sonuc = (username1==username_input)
# print("Eşleşmme sonucu...:",sonuc)

# sonuc = (username2==username_input)
# print("Eşleşmme sonucu...:",sonuc)


sonuc=(username1.lower()==username_input.lower())
sonuc2=(username2.lower()==username_input.lower())

sonuc3=((sonuc or sonuc2 )==True) #sonuc3(sonuc!=sonuc2)
print("Eşleşmme sonucu...:",sonuc3)

sonuc=((username1==username_input).lower())
'''

# dict={"crazyceku_78@gmail.com":244466666,"crayzarif_14@gmail.com":123456}
# gmail=input("Gmail Adresinizi Giriniz :")
# sifre=input("Gmail Şifrenizi Giriniz :")
# sonuc=dict.get(gmail)==sifre


# sonuc1=(sonuc==True)#sonuc3(sonuc!=sonuc2)
# print("bşaraıllı")


# gmail_sonuc=(gmail=="crazyceku_78@gmail.com")
# sifre_sonuc=(sifre==244466666)
# karar=((gmail_sonuc or sifre_sonuc)==True )
# print("giriş başarılı")
# # karar=((gmail_sonuc or sifre_sonuc)==False )
# # print("giriş başarısız")

# gmail_sonuc1=(gmail=="crayzarif_14@gmail.com")
# sifre_sonuc1=(sifre==123456)
# karar1=((gmail_sonuc1 or sifre_sonuc1)==True )
# print("giriş başarılı")
# # karar1=((gmail_sonuc1 or sifre_sonuc1)==False )
# # print("giriş başarısız")
'''
users={
    "garavel.usta@gora.com.tr":"garavel123",
    "216.robot@gora.com.tr":"robot123"
}

print("-*-*-*A.R.O.G Portalına Hoş Geldiniz-*-*-*-*")
print("-*-*-*Lütfen A.R.O.G bilgilerinizi Giriniz-*-*-*")
input_mail=input("Mail Adresinizi Giriniz... :")
input_sifre=input("Mail Şifrenizi Giriniz... :")
sonuc_mail=(input_mail in users.keys())
sonuc_sifre=(input_sifre in users.values())
sonuc_final=((int(sonuc_mail)+int(sonuc_sifre))==2)
print("Eşleşme Durumu ...:", sonuc_final)
'''
'''
fruits=['elma','muz','portakal','kivi']

print("kavun"in fruits)
'''
'''
x=y=[10,20,30]
z=[10,20,30]
print(x is y)
print(x is z)
print(x==z)

'''
'''
vize=int(input("Vize Notunu Gir:"))
final=int(input("Final Notunu Gir:"))
islem=(vize*40/100)+(final*60/100)
karar=(islem>50)
print("Geçme Durumu:",karar)
'''
'''
num=int(input("Sayı Gir?"))
islem=(num%2)
karar=bool(islem==0)
print("sayı:",karar)
'''
'''
if ():
    #<eğer koşul doğru(True) ise çalışacak kodlar>
else:
    #<eğer koşul yanlış(False) ise çalışacak kodalar>

'''
'''
x=98
y=98
if x>y:
    print("en büyük sayı",x,"dir")
elif x==y:
    print("sayılar birbirine eşittir.")    
else:
    print("en büyük sayı",y,"dir")  
'''
'''
username=str(input("Kullanıcı adını giriniz"))
passwrd=int(input("Şifrenizi Giriniz:"))

if username=="Durukan":
    if passwrd==12345:
        print("Giriş Başarılı")
    else:
        print("Şifre Yanlış")
elif username!="Durukan":
    if passwrd==12345:
        print("Kullanıcı adı yanlış")
    else:
        print("Kullanıcı Adı ve Şifre Yanlış")  
'''
from time import sleep

print("----------HESAP MAKİNESİNE HOŞGELDİNİZ----------")

secim=int(input("Hangi seçimi yapmak istersin;\nToplama(1)\nÇıkarma(2\nÇarpma(3\nBölme(4)\n"))
num1=int(input("Birinci Sayıyı Giriniz"))
num2=int(input("İkinci Sayıyı Giriniz"))  
if secim==1:
     sleep(1)
     print("Loading.")
     sleep(1)
     print("Loading..")
     sleep(1)
     print("Loading...")
     sleep(1)
     print("Loading....")
     print(num1+num2)
elif secim==2:
     sleep(1)
     print("Loading.")
     sleep(1)
     print("Loading..")
     sleep(1)
     print("Loading...")
     sleep(1)
     print("Loading....")
     print(num1-num2)  
elif secim==3:
     sleep(1)
     print("Loading.")
     sleep(1)
     print("Loading..")
     sleep(1)
     print("Loading...")
     sleep(1)
     print("Loading....")
     print(num1*num2)
elif secim==4:
    if num2==0:
        print("payda sıfır olamaz")
    else:    
         sleep(1)
         print("Loading.")
         sleep(1)
         print("Loading..")
         sleep(1)
         print("Loading...")
         sleep(1)
         print("Loading....")
         print(num1/num2)
else:
    print("Adam gibi seçeneklerden birini tuşla.")               
