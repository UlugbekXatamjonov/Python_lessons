"""
Created  20:00:34   18/06/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#36 -dars: Funksialarni tekshirish

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

# Quidagi funksialarni yarating a ularning har biri uchun test dasturlarni yozing

#1
# Uchta son qabul qilib ulardan eng kattasini qaytaruvchi funksia

def eng_kattasi(x,y,z):
    print("3 ta butun son kiriting, biz eng kattasini qaytaramiz...")
    while True:
        x = input("1-butun sonni kiriting: ")
        if x.isdigit():
            x = int(x)
            break
        
    while True:
        y = input("2-butun sonni kiriting: ")
        if y.isdigit():
            y = int(y)
            break
        
    while True:
        z = input("3-butun sonni kiriting: ")
        if z.isdigit():
            z = int(z)
            break
        
    if y<x>z:
        print(f"Eng katta son bu {x}")
    elif x<y>z:
        print(f"Eng katta son bu {y}")
    elif x<z>y:
        print(f"Eng katta son bu {z}")
    elif x==y==z :
        print("Barcha sonlar teng ")
        
eng_kattasi(3,5,7)       

#yakunlandi

 













