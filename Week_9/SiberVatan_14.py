'''
import os
print(os.getcwd())
# mevcut_dizin=os.getcwd()
for i in os.listdir(os.getcwd()):
    print(i)
#print(os.listdir(mevcut_dizin))
os.makedirs('C:/Users/Lenovo/Desktop/Siber Vatan/Abuzittin', exist_ok=True)
os.chdir('C:\\Users\\Lenovo\\Desktop\\Siber Vatan\\Abuzittin')
print(os.getcwd())
file=open("New File.txt","w",encoding='utf-8')
file.write("Hello World")
file.close()
os.remove("New File.txt")
os.chdir('C:\\Users\\Lenovo\\Desktop\\Siber Vatan')
print(os.getcwd())
os.rmdir('Abuzittin')
'''


import os
gecerli_dizin=os.getcwd()

for i in os.listdir(os.getcwd()):
    print(i)
new_directary= os.path.join(gecerli_dizin,"yeni_dizin")
os.mkdir(new_directary)
print(f"{new_directary} oluştu")    
    
os.chdir(new_directary)
print(f"{new_directary} dizisine girildi")

dosya_yolu=os.path.join(new_directary,"example.txt")
with open(dosya_yolu,"w",encoding='utf-8') as file:
    file.write("hello world")

