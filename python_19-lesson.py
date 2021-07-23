"""
Created  05:23:34  14/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#19-dars: Funksia

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan,
# funksiya yozing.

def salom_ber() :
    """" Foydalanuvchi tug'ilgan yilini hisolaydigan funksia"""
    ism = input("Ismingiz nima ?")
    yosh = int(input("Yoshingiz nechida ?"))
    print(f"Assalomu aleykum {ism.title()}. Siz {2021-yosh}da tug'ilgansiz.")

salom_ber()


#2
# Foydalanuvchidan son olib, uning kvadrati va kubini 
# konsolga chiqaruvchi funksiya yozing.

def daraja() :
    """Sonni darajaga ko'taruvchi funksia"""
    son = int(input("Istalgan butun son kiriting: "))
    daraja_son = int(input("Ushbu kiritgan soningizni nechanchi darajaga ko'tarishni hohlaysiz: "))
    if son and daraja_son > 0 :
        print(f"{son}ning {daraja_son}-darajasi, {son**daraja_son} ga teng.")
    else:
        print(" ")
        
daraja() 


#3
# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing

def toq_juft() :
    son = int(input("Istalgan butun sonni kiriting: "))
    """Sonni toq yoki juft ekanini aniqlaydigan funksia"""
    if son%2 :
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")
    
toq_juft()


#4
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
#  Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def katta_kichik() :
    """Kiritilgan sonning eng kattasini o'rsatuvchi funksia """
    son1 = int(input("1- sonni kiriting: "))
    son2 = int(input("2- sonni kiriting: "))
    if son1 > son2 :
        print(f"{son1}")
    elif son1 < son2 :
        print(f"{son2}")
    else:
        print("Sonlar teng")
    
katta_kichik()
    


#5
# Foydalanuvchidan x va y sonlarini olib, x**y ni konsolga chiqaruvchi funksiya yozing.

def toq_juft() :
    son = int(input("Istalgan butun sonni kiriting: "))
    """Sonni toq yoki juft ekanini aniqlaydigan funksia"""
    if son%2 :
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")
    
toq_juft()


#6
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
# oldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def bolinish() :
    """berilgan sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksia """
    son = int(input("Istalgan butun sonni kiriting: "))
    for n in range(2,11):
        if  not son%n :
            print(f"{son} {n}ga qoldiqsiz bo'linadi")
        
bolinish()


#yakunlandi








