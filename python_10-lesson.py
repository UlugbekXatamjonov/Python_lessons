# Xatamjonov Ulugbek 
# 2021-01-18 / 15:50
# Dasturlash asoslari
# 10-dars "IF-Else"
# Amaliyot

#1
# yangi cars degan ro'yhat tuzing , ro'yhat elementlari birinchi harfini katta qilib konsulga chiqaring . GM uchun ikkala harifni katta qiling 
cars=["toyota","mazda","hyundai","gm","kia"]
for car in cars :
  if car=="gm"  :
    print(car.upper())
  else:
    print(car.title())

#2
# Yuqoridagi mashqni (!=) operatori yordamida bajaring
# for car in cars 
#  if car != "gm" :
#     print(car.upper())
#  else:
   

#3
# Foydalanuvchi login ismini so'rang . Agar login admin bo'lsa, "Xush kelibsiz , Admin. Foydalanuvchilar ro'yhatini ko'rasizmi ?" habarini konsulga chiqaring . Akis holda , "Hush kelibsiz , {Foydalanuvchi_ismi } ! " matnini konsulga chaqiring .
foydalanuvchi_ismi = input("Isminngiz nima ? ")
if foydalanuvchi_ismi == "admin" :
    print("Xush kelibsiz Admin. Foydalanuvchilar ro'yhatini ko'rasizmi ?")
else :
    print(f"Xush keibsiz,  {foydalanuvchi_ismi}!")

# yakunlandi



