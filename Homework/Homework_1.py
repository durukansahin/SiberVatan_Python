# 1- Kullanıcıdan bir cümle alın, cümlenin başındaki ve sonundaki boşlukları kaldırın, ardından tüm harfleri küçük harfe çevirin.

# cumle=str(input("Lütfen Bir Cümle Girer Misin ?"))
# cumle_strip=cumle.strip()#Cümlenin Başındaki boşlukları yok eder
# cumle_strip_lower=cumle_strip.lower()
# print(cumle_strip_lower)

# 2- Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın.

# string=str(input("Cümle ya da Kelime Yaz"))
# aranan_karakter = input("Kaç kez geçtiğini saymak istediğiniz karakteri girin: ")
# arama = string.count(aranan_karakter)
# print(aranan_karakter,"karakteri metin içinde",arama,"kez geçmektedir.")

# 3- Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğini kontrol edin.

# kelime = input("Kelimeyi girin: ")
# harf = input("Kaç kez geçtiğini kontrol etmek istediğiniz harfi girin: ")
# arama1 = kelime.count(harf)
# print(harf,"harfi",kelime,"kelimesinde",arama1,"kez geçmektedir.")


# 4- İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.

# string2=str(input("Cümle ya da Kelime Yaz"))
# string3=str(input("Cümle ya da Kelime Yaz"))
# birlesim=string2+string3
# kelime1=input("Kaç kez geçtiğini kontrol etmek istediğiniz kelimeyi girin: ")
# arama3=birlesim.count(kelime1)
# print(arama3)

# 5- Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.

#cumle = input("Bir cümle girin: ")
# kelimeler = sorted(cumle.split())
# print("Alfabetik sıraya göre sıralanmış kelimeler:")
# print('-'.join(kelimeler))

# 6- Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin.

# string4 = input("Birinci string'i girin: ")
# string5 = input("İkinci string'i girin: ")
# birlesik_string = string4 + string5
# kucuk_harfler = birlesik_string.lower()
# print("Birleştirilmiş ve küçük harfe çevrilmiş string:", kucuk_harfler)

# 7- Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin.

# ana_string = input("Bir string girin: ")
# aranan_substring = input("Aranacak substring'i girin: ")
# yeni_substring = input("Yerine eklenecek yeni substring'i girin: ")
# guncellenmis_string = ana_string.replace(aranan_substring, yeni_substring)
# print("Güncellenmiş String:", guncellenmis_string)

# 8- Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin.

# cumle=str(input("Lütfen Bir Cümle Gir "))
# cumle_replace=cumle.replace("a","@")
# print(cumle_replace.replace("A","@"))

# 9- Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin.

# cumle=str(input("Lütfen Bir Kelime Giriniz"))
# ters=(cumle[::-1])
# if ters==cumle:
#     print("palindrome bir kelime")
# else:
#     print("palindrome bir kelime değil")    

# 10- Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.




# 11- Bir liste oluşturun ve listenin ortasındaki elemanı bulun.

# liste = [1, 2, 3, 4, 5, 6, 7]
# orta_index = len(liste) // 2
# orta_eleman = liste[orta_index]
# print(len(liste))
# print("Listenin ortasındaki eleman:", orta_eleman)


# 12- Bir tuple oluşturun, tuplein 2. ve 4. elemanlarını yeni bir tuple olarak alın.

# tuple=(10,20,30,40,50,)
# newtuple=(tuple[1],tuple[3])
# print(type(newtuple))
# print(newtuple)

# 13- Bir set oluşturun, set içine bir sayı ekleyin, ardından bu sayıyı setden çıkarın.

# kume={7,33,94}
# kume.add(12)
# print(kume)
# kume.discard(12) # 'discard' kümeden eleman atmamızı sağlar zaten kelime anlamıda 'atmak' dır
# print(kume)


# 14- Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin.




# 15- Bir liste oluşturun, listenin ortasına yeni bir sayı ekleyin.

# liste = [1, 2, 3, 4, 5]
# eklenecek_sayi = int(input("Listenin ortasına eklemek istediğiniz sayıyı girin: "))
# orta_liste = len(liste) // 2
# liste.insert(orta_liste, eklenecek_sayi)
# print("Yeni Liste:", liste)

# 16- Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin.

# liste = [7, 33, 94, 5, 14]
# orta_liste1 = len(liste) // 2
# orta_eleman = liste[orta_liste1]
# tuple_olusturulan = (orta_eleman)
# print(liste)
# print("Oluşturulan Tuple:", tuple_olusturulan)

# 17- Bir set oluşturun ve setin elemanlarını içeren bir liste oluşturun, ardından bu liste elemanlarının toplamını hesaplayın.

# kume1={5,7,33,94}
# liste1=list(kume1)
# liste1_toplam=sum(liste1)#sum fonksiyonu listedeki sayıları toplamamıza yardımcı olur
# print(liste1_toplam)

# 18- Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun.




# 19- Bir liste oluşturun ve listenin içindeki en büyük sayıyı bulun, ancak sadece aritmetik operatörler (+, -, *, /) kullanmadan yapın.

# liste=[7,33,94,14,5]
# en_buyuk_liste=max(liste)
# print(en_buyuk_liste)

# 20- Bir dict oluşturun ve dictin içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin.



