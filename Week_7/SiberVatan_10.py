'''
tür=float(input("Ödeme kodunu Giriniz:(1=saatlik çalişan, 2=komisyon çalişanı)"))
def hesaplamasaatlik():
    if tür==1:
        saat=float(input("Çalişma Saatini Giriniz: "))
        if saat>40:
            hes=saat-40
            sonuc=(40*50)+(hes*(1.5*50))
            print(float(sonuc),"tl")
        else:
            hes=saat*50    
            print(float(hes),"tl")
            
    elif tür==2:
                 
    
        def hesaplamakomisyon():
            if tür==2:
                satis=float(input("Aylık toplam satış miktarınızı giriniz"))
                hes=((satis*0.05)+500)
                print(float(hes),"tl")
            else:
                print("HATALI")
        hesaplamakomisyon()        
hesaplamasaatlik()                        
'''

def sicaklik_araligi(sicakliklar):
    sicaklik_araliklari = {
        "(-20) -(0)": 0,
        "(0) -(20)": 0,
        "(20) -(40)": 0
    }
    for sicaklik in sicakliklar:
        if -20<=sicaklik<0:
            sicaklik_araliklari["(-20) -(0)"]+=1
        elif 0<=sicaklik<20:
            sicaklik_araliklari["(0) -(20)"]+=1
        elif 20<=sicaklik<40:
            sicaklik_araliklari["(20) -(40)"]+=1
    for aralik,sayi in sicaklik_araliklari.items():
        print(aralik,"arasında",sayi,"tane sicaklik var")
sicaklik_listesi=[5,-15,25,12,2,30,18,-5,35,-18,8]
sicaklik_araligi(sicaklik_listesi)                        
            
'''               
liste=[5,-15,25,12,2,30,18,-5,35,-18,8]

sayac=-20
liste1=[]
liste2=[]
liste3=[]
for i in liste:
    
    if i<0 and i >-20:
        liste1.append(i)
    elif i>0 and i<20:
         liste2.append(i)
    elif i>20 and i<40:
        liste3.append(i)
    else:
        print("aralıkda değil")    
    sayac+=i
print("(-20)-(0)=",len(liste1))
print("(0)-(20)= ",len(liste2))   
print("(20)-(40)=",len(liste3))                   
'''             
            
   
       
    
    

        
    

           
             

    
