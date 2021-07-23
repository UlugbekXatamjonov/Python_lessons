"""
Created  21:00:34  06/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#18-dars: while-list-dict

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""
#1
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang

print("Bozordan olmoqchi bo'lgan mahsulotlar ro'yhatini tuzamiz. ")
mahsulotlar =[]
while True :
    mahsulot = input("Mahsulot nomini kiriting: ")
    mahsulotlar.append(mahsulot)
    savol = input("Yana mahsulot kiritasizmi(ha/yo'q'): ")
    if savol == "yo'q" :
        break
print(" ")
print("Bozorlik ro'yhati: " ,
      f"{mahsulotlar}")


#2
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

mahsulotlar = {}
while True :
    mahsulot = input("Mahsulot nomini kiriting: ")
    narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
    mahsulotlar[mahsulot] = int(narx)
    savol = input("Davom etasizmi(ha/yo'q') ?")
    if savol != "ha" :
        break
print(mahsulotlar)


#3
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir 
# mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz 
# mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda
# "Bizda bu mahsulot yo'q" degan xabarni kor'sating.


print("Bozordan olmoqchi bo'lgan mahsulotlar ro'yhatini tuzamiz. ")
mahsulotlar =[]
while True :
    mahsulot = input("Mahsulot nomini kiriting: ")
    mahsulotlar.append(mahsulot)
    savol = input("Yana mahsulot kiritasizmi(ha/yo'q'): ")
    if savol != "ha" :
        break

e_bozor = {
"olma":5000,
"gilos":9000,
"non":2000,
"go'sht":55000,
"yog'":2100,
"makaron":6000,
"gurunch":13000,
"krem":6000
}

while mahsulotlar :
    mahsulot = mahsulotlar.pop()
    if mahsulot in e_bozor.keys() :
        narx = e_bozor[mahsulot]
        print(f"{mahsulot.title()}-{narx} so'm")
    else:
        print(f"Bizda {mahsulot} yo'q")


# yakunlandi















