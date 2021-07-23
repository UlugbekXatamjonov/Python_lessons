
"""
Created  20:05:09  20/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#19-dars: Funksia ustida ammallar 

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1
# Matinlardan iborat ro'yhat qabul qilib, ro'yhatdagi har bir matining
# birinchi harfini katta harfga o'zgartiruvchi funksia yozing 

def katta_harf(matnlar) :
    for i in range(len(ismlar)):
        matnlar[i] = matnlar[i].title()
  
ismlar = ["umarbek","nodirjon","ilg'orjon","quvonchbek"]
katta_harf(ismlar)
print(ismlar)


#2
# Darsimiz davomida yozilgan Baholar funksiasini .pop() metodidan foydalanmasdan 
# va asl ro'yhatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing .


talabalar = ['ali', 'vali', 'hasan', 'husan']      

def bahola(ismlar):
    baholar = {}
    for ism in ismlar :
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
baholar = bahola(talabalar)
print(baholar)
print(talabalar)

#yakunlandi

































