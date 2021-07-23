"""
Created  10:49:34   12/06/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#33 -dars: Fayllar bilan ishlash

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1 
# Bugun  Organgan narsalarimizni matnga yozing va mtinni python yordamida oching

fayl_nomi = "New_file.txt"
matn1 = "Men bugungi 33-darsda fayllar bilan ishlashni o'rgandim."
matn2 = "Yani fayllarni pythonda ochishning bir necha xil usullarini,"
matn3 = "pythonda matn yozishni va boshqa usullarni o'rgandim."
ism = "Xatamjonov Ulug'bek: "

with open(fayl_nomi,'w') as fayl:
    fayl.write(ism+"\n")
    fayl.write(matn1+"\n")
    fayl.write(matn2+"\n")
    fayl.write(matn3)
    
#2
# Quidagi "pi_million_digits.txt" faylini yuklab oling(faylda 'pi' soni nuqtadan keyin million xona aniqlik bilan yozilgan)

with open('pi_million_digits.txt') as file:
    pi = file.read() 
# print(pi)

pi = pi.rstrip()
pi = pi.replace('\n','')
# print(pi)
    
#3
# Sizning tg'ilgan kuningiz 'pi' soni  tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksia yozing
# Misol uchun , 25 fevral 2000-yil bo'lsa , 25022000 ketma ketligi yuqoridagi matnda uchraydimi yoqmi tekshiring

tk = input("Tug'ilgan kuningiz sanasini kiriting(misol un: 25-yanvar 1992-yil bo'lsa, 25011992 ko'rinishida kiriting): ")

def qidir():
    if tk in pi:
        print("yes")
    else:
        print("no")
qidir()


#4
# 'pi' fayli ichidagi matinni 'float' ko'rinishiga o'tkazing va 'pickle' yordamida boshqa faylga yuklang

import pickle

with open('pi_million_digits.txt') as file:
    pi = file.read() 
    pi = pi.rstrip()
    pi = pi.replace('\n','')
    pi = pi.replace('  ','')
    pi = float(pi)

with open('pkl_file.pkl','wb') as pkl:
    pickle.dump(pi,pkl)
    
#5
# Foydalanuvchidan turli hil ma'lumotlarni so'rab har bir kiritilgan yangi malumotni
# yangi qatordan yozib boruvchi dastur tuzing. Dastur qayta chaqirilganda 
# yangi ma'lumotlar fayl oxiridan qo'shib borilsin.

with open('file.txt','a') as file2:
    file2.write(input("Istalgancha matn yozing: ")) 
    
#yakunlandi














