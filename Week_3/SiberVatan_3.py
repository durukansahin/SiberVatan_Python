ad = "Durukan"
soyad="Şahin"
yas=16

karsilama="Benim Adım" +" " + ad + " " + soyad + " " + "Yaşım" +" "+str(yas)+" "+"Hoşgeldin"
uzunluk=len(karsilama)
print(karsilama)
print(uzunluk)
print(karsilama[3]) #burda 3. indisi istiyoruz ve bu indisler 0 dan başlar
print(karsilama[-1])
print(uzunluk-1)
print(karsilama[0:10])
print(karsilama[:24])
print(karsilama[25:])
print(karsilama[2:10:5]) #2.indisten 3 er 3 er atlayarak 25. indise kadar 
print(karsilama[:-3])
print(karsilama[::-1])

karsilama_upper=karsilama.upper()
print(karsilama_upper)

karsilama_lower=karsilama.lower()
print(karsilama_lower)

karsilama_strip=karsilama.strip()
print(karsilama_strip)

karsilama_split=karsilama.split()
print(karsilama_split)
print(karsilama_split[5])

karsilama_join="-".join(karsilama)
print(karsilama_join)

karsilama_find=karsilama.find("Durukan")
print(karsilama_find)

karsilama_startswith=karsilama.startswith("B")
print(karsilama_startswith)

karsilama_endswith=karsilama.endswith("n")
print(karsilama_endswith)

karsilama_replace=karsilama.replace("Durukan","Ömer")
print(karsilama_replace)

