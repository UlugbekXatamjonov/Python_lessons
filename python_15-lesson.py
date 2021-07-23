"""
Created  21:06:23  30/03/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#14-dars: Funksiya  bilan ishlash

Amaliyot https://python.sariq.dev  web sahifasi asosida

"""
#1
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
pyhton_izohli_lugati = {
"print":"matnni konsulga chiqaradi",
".upper":"matnni katta harif bn chiqaradi",
".title":"birinchi harfni katta qilib beradi",
"if":"agar",
"elif":"agar, yoki",
"else":"yoki",
"float()":"o'nlik son",
"int()":"butun son",
"input":"malumot qabul qilai",
}

for k , v in sorted(pyhton_izohli_lugati.items()) :
    print(f"{k.title()}-{v}")


#2
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

print('Dunyo davlatlari:')
for davlat in sorted(davlatlar):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())


#3
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

#4
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
"osh":15000,
"dimlama":12000,
"norin":20000,
"non":2000,
"choy":1000,
"salat":5000,
"shashlik":6000,
"musqaymoq":3000,
"pirojni":3000,
"somsa":5000
}
print("3 ta  taom nomini kiriting:")
buyurtmalar = []
for n in range(3) :
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar :
    if buyurtma in menu :
        print(f" {buyurtma.title()}  {menu[buyurtma]} so'm. ")
    else:
        print(f"Kechirasiz, bizda {buyurtma.title()} yo'q.")

#yakunlandi










