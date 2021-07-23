
"""
Created  22:06:23  03/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#16-dars: Nesting

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""
#1
# Adabiyot (ilm fan , sanat, internet) olamidagi 4ta mashxur shaxslar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
# lug'atlarni bita ro'yhatga joylang. va har bir shaxs haqidagi malumotlarni konsulga chiqaring .

shaxslar1 = {
"ism":"Stiv Jobs",
"tyil":1945,
"kasbi":"dasturchi",
"davlat":"AQSH",
"asar":"Boy bo'lish siri"
}

shaxslar2 = {
"ism":"Stalin",
"tyil":1897,
"kasbi":"Prizident",
"davlat":"Rossia",
"asar":"Harbiy strategia va boshqaruv"    
}

shaxslar3 = {
"ism":"Tyson Fury",
"tyil":1983,
"kasbi":"bokschi",
"davlat":"Angilya",
"asar":"Men bokschiman :)"
}

shaxslar4 ={
"ism":"Anvar Narzullayev",
"tyil":1980,
"kasbi":"dasturchi",
"davlat":" O'zbekiston ",
"asar":"Dasturlash asoslari"
}

shaxslar = [ shaxslar1 , shaxslar2 , shaxslar3 , shaxslar4 ]

for shaxs in shaxslar :
    ism = shaxs["ism"]
    tyil = shaxs["tyil"]
    kasb = shaxs["kasbi"]
    davlat = shaxs["davlat"]
    asar = shaxs["asar"]
    print(f" {ism.title()} {tyil}-yili {davlat.title()}da tug'ilgan. Kasbi {kasb}.")


#2
# Yuqoridagi lug'atga har bir shahsning mashxur asarlari ro'yhatini ham tuzing . 
# for tsikli yordamida mualifning ismi va uning asarlarini konsulga chiqaring .
for shaxs in shaxslar :
    ism = shaxs["ism"]
    asar = shaxs["asar"]
    print(f" {ism.title()}ning mashhur asari {asar}dir.")
    

#3
# Oila azolaringiz(do'stlaringiz)dan ularning sevimli kino-seriallari haqida so'rang.
# do'stingizni ismi kalit uning sevimli kinolarini esa ro'yhat ko'rinishida lug'atlarga saqlang.
# natijani konsulga chiqaring.

kinolar = {
"ali":["Samolardan balandda", "Qahr","T-34"], 
"vali":["Omadli jentelmenlar","'Ы' operatsiasi", "Ivan vasilevich o'z kasbini o'zgartiradi."],
"hasan":["Mahallada duv-duv gap", "Osmondagi bolalar","Taqdir hazili"], 
"husan":["Yangi o'rgimchak odam", "Temir odam", "Tor" ],
"aziz":["Izquvar", "Ichkarida", "Jumong"]
}

for ism, kinolar in kinolar.items() :
    print(f"\n{ism.title()}ning sevimli filmlari: ")
    for kino in kinolar :
        print(kino)


#4
# Davlatlar deganlug'at yarating , lugat ichida davlatlar haqidagi malumotlarni lugat ko'rinishida saqlang ..
# har bir davlat haqidagi malumotni konsulga chiqaring.

davlatlar ={
"o'zbekiston":

{"maydon":48833,
"aholi":36_345_242 ,
"pul":"so'm",
"domen":".uz",
"qita":"osio"}    
,


"rossiya":

{"maydon":1298302,
"aholi":436_283_243 ,
"pul":"rubl",
"domen":".ru",
"qita":"yevropa"}    
,
    

"madakaskar":

{"maydon":34912,
"aholi":48_873_783 ,
"pul":"dollar",
"domen":".mr",
"qita":"afrika"}    
,


"brazilya":

{"maydon":239754,
"aholi":647_682_763 ,
"pul":"brazilya dollari",
"domen":".br",
"qita":"janubiy amerika"}    
}

for davlat, info in davlatlar.items() :
    print(f"\n{davlat.title()} haqida:"
          f"\n{info['qita'].title()}da joylashgan "
          f"\nAholisi: {info['aholi']}ta"
          f"\nMaydoni: {info['maydon']} kv.km"
          f"\nPul birligi: {info['pul']} "
          f"\nInternet domeni: {info['domen']}" )

#5
# 


davlat = input("Davlat nomini kiriting:").lower()
if davlat in davlatlar:
    info = davlatlar[davlat] 
    print(f"\n{davlat.title()} haqida:"
              f"\n{info['qita'].title()}da joylashgan "
              f"\nAholisi: {info['aholi']}ta"
              f"\nMaydoni: {info['maydon']} kv.km"
              f"\nPul birligi: {info['pul']} "
              f"\nInternet domeni: {info['domen']}" )
else :
    print("Kechirasiz, bizda bu davlat haqida ma'lumot yo'q.")


# yakunlandi





