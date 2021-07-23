"""
Created  14:34:34   16/06/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#34 -dars: JSON

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""
import json

#1
# Ushbu(data) o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsulga saqlang

data = {"Model":"Malibu","Rang":"Qora","Yil":2020,"Narx":40000}
data_json = json.dumps(data)
print(data_json)

#2
# Ushbu JSON(talaba_json) matnini ko'chirib oling, va talabaning ismi va familyasi konsulga chiqaring

talaba_json = """{"ism":"Hasan","familya":"Husanov","tyil":2000}"""
print(type(talaba_json))

talaba = json.loads(talaba_json)
talaba = {'ism': 'Hasan', 'familya': 'Husanov', 'tyil': 2000}
ism = talaba['ism']
familya = talaba["familya"]

print(talaba)
print(type(talaba))

fullname =  f"Talaba: {ism} {familya}"
print(fullname)

#3
# Yuqoridagi ikki o'zgaruvchini alohida JSON faylga yuklang 

ism = talaba['ism']
familya = talaba["familya"]

with open('ism.json','w') as ij:
    json.dump(ism,ij)
with open('familya.json','w') as fj:
    json.dump(familya,fj)

#4 
# Quidagi JSON faylni('students.json') yuklab oling. Faylda 3 ta talabaning 
# ism familyasini saqlang. Ularni har birini alohida qatordan konsolga chiqaring

with open('students.json') as st:
    stj = json.load(st)
    
print(stj)
name1 = stj['student'][0]['name']
name2 = stj['student'][1]['name']
name3 = stj['student'][2]['name']

print(name1,name2,name3)

#5
# Quisdagi bog'lamaga(       ) kirasiz , Wikipediadagi Python dasturlash tili haqidagi 
# maqolani JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan malumotni 
# JSON ko'rinishida saqlang . Faylni Pyhton da oching  va maqolani konsulga chiqaring .

file = 'wiki_python.json'
with open(file) as w:
    wiki = json.load(w)

print(wiki)

#yakunlandi


