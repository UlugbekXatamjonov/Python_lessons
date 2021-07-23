"""
Created  15:34:34   27/06/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#38 -dars:

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""
import datetime as dt
now = dt.datetime.now()
import re
bugun = dt.date.today()
#1
# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanaani konsulga chiqaring.

    
#2
# Ramazon va qurbon hayitigacha qolgan kunlarni konsulga chiqaring
# bu sanalar tahminan olingan 
ramazon = dt.date(2022, 3, 13) # ramazon kuni
qh = dt.date(2022, 7, 14) # qh - qurbon hayiti kuni

r_farqi = ramazon-bugun
print(f"Ramazongacha {r_farqi}  qoldi.")
qh_farqi = qh-bugun
print(f"Qurbo Hayitigacha {qh_farqi}  qoldi.")


#3
# Tug'ilgan kuningizdan bugungi kungacha qancha yil,oy,kun,o'tkanini hisoblovchi funksia yozng.
def Tkun():
    hozir = dt.datetime.now()
    tkun = dt.datetime(2001, 1, 18, 3, 00, 00)
    farq= tkun-hozir
    kunlar = farq.days
    oylar =  int(kunlar/30)
    yillar = int(oylar/12)
        
    print(f"Tug'ilgan kuningizdan bugungi kungacha bo'lgan farq:{yillar} yil , {oylar} oy , {kunlar} kun.")
Tkun()

#4
# Foydalanuvchidan telefon raqamini kiritishini so'rang. Kiritilgan raqamni andoza yordamida tekshiring.
nomer = input("Telefon raqamingizni kiriting:")
qolip = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
tekshir = re.findall(qolip,nomer)
print(f"Raqam to'g'ri: {tekshir}")

#yakunlandi












