"""
Created  21:13:44  20/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#22-dars: Funksialar. *args va **kwargs

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1
# Istalgancha sonlarni qabul qilib , ularning ko'paytmasini qaytaruvchi funksia yozing.

def kopaytiruvchi(*sonlar):
    kopaytma=1
    for son in sonlar :
        kopaytma*=son
    return kopaytma

print(kopaytiruvchi(2,5,3,11,4))


#2
# Talabalar haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksia yozing,
# Talabalarning ismi va familyasi majburiy argument, qolgan argumentlar esa ixtiyoriy
# ko'rinishda istalgancha berilishi mumkin bo'lsin 

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')

# yakunlandi



























