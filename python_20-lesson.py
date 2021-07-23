"""
Created  07:25:34  14/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#19-dars: FUNKSIYADAN QIYMAT QAYTARISH

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
# email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya
# yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni
# ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

#2
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
# ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.


def mijiz_info(ism,familya,tjoy,tyil,tel=" ",gmail=" ") :
    """Mijoz haqidagi ma'lumotlarni shakllantiruvchi funksia"""
    mijoz = {'ism': ism,
              'familya':familya,
              'tyoy': tjoy,
              'yoshi': 2021-tyil,
              "tel":tel,
              "gmail": gmail,}
    return mijoz

print("Mijoz haqidagi malumotlarni kiriting: ")
mijozlar = []

while True:
    ism = input("Ismi: ")
    familya = input("Familyasi: ")
    tjoy = input("Tug'ilgan joyi': ")
    tyil= int(input("Tug'ilgan yili: "))
    tel = input("Telefon raqami: ")
    gmail = input("Gmailli: ")
    
    mijozlar.append(mijiz_info(ism,familya,tjoy,tyil,tel,gmail))
    savol = input("Davom etasizmi(yes/no)? ")
    if savol != "yes" :
        break
    
print("Mijozlar: ")
for mijoz in mijozlar :
    print(f"{mijoz['ism'].title()} {mijoz['familya'].title()}",
          f"{mijoz['yoshi']} yoshda , telefon raqami {mijoz['tel']}")
    

#3
#Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def kattasi(x,y,z):

    if y>=x:
        x = y
    if z>=x:
        x = z
    return x


#4
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
# diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def aylana_info(radius,p=3.14):
    aylana = {"radius":radius,
              "diametr":radius*2,
              "perimetr":p*radius*2,
              "yuza":p*radius**2}
    return aylana



#5
# Berilgan oraliqdagi tub sonlarni qaytaruvchi funksia yozing

def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar


#6
# Foydalanuvchidan son qabul qilib , shu son miqdoricha Fibonachchi ketma ketligidagi 
# sonlar ro'yhatni qaytaruvchi funksia yozing .

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(10))

# yakunlandi 


























