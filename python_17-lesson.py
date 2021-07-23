"""
Created  20:27:25  04/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#17-dars: While tsikli

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1 
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

savol= "Sevimli kitobingizni kiriting:"
savol += "(kitoblar tugagach 'stop' deb yozing!)"

while True :
    kitob=input(savol)
    if kitob == 'exit' :
        break
print('Rahmat')

#2
#  Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
#  7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
#  65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini
#  so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda 
#  dastur to'xtasin (ikkita shartni ham tekshiring).

savol = "Yoshingiz nechida: "
a = 2000 # 0-7
b = 3000 # 7-18
c = 10000 # 18-65
d = 0 # 65-0
e = "exit"
q = "quit"

while True :
    qiymat=input(savol)
    if qiymat == e or qiymat == q:
        break
    
    
    yosh = int(qiymat)   
    
    if int(yosh)<=7 :
        print(f"Sizga kirish narxi {a} so'm.")
        
    elif int(yosh)>7 and int(yosh)<=18 :
        print(f"Sizga kirish narxi {b} so'm.") 
        
    elif int(yosh)>18 and int(yosh)<=65 :
        print(f"Sizga kirish narxi {c} so'm.")

    elif int(yosh)>65 :
        print("Sizga kirish bepul.")

        

#3
# Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
# Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. 
# Xatolarni to'g'rilay olasizmi?

# xato berilgan javob

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# # xato berilgan javob

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# to'g'ri berilgan javob

while True:
    qiymat = input(savol)
    
    if float(qiymat)<0:
        continue
    elif qiymat=='exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")


# yakunlandi















