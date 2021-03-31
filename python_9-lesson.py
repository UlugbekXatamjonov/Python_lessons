# Xatamjonov Ulugbek 
# 2021-01-14 / 21:21
# Dasturlash asoslari
# 8-dars For tsikli haqida
# Amaliyot

#1
# Kamida 5 ta ismdan tashkil topgan ismlar degan ro'yhat tuzing , va ro'yhatdagi har bir ismga takrorlanuvchi xabar yozing 
ismlar=("Anvar","Saidbek","Botir","Alisher","Xojiboy")
for ism in ismlar:
   print("Salom do'stim", ism)

#2
# Yuqoridagi tskil tugaganidan so'ng , ekranga "Kod n marta takrorolandi " degan xabar chiqaring (n o'rniga kod necha maratoba takrorlanganini yozing ).
print("Kod", len(ismlar) ,"marotaba takrorlandi")

#3
# 10 dan 100 gacha bo'lgan toq sonlar ro'yhatini tuzing . Ro'yhatning har bir elementining kubini yangi qatordan konsulga chiqaring
sonlar=list( range(11,100,2))
for son in sonlar:     
     print(son**3)

#4
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritishini so'rang, va kinolar dgan ro'yhatga saqlab qo'ying va konsulga chiqaring 
kinolar=[]
print("5 ta sevimli kinolaringiz qaysilar ?")
for k in range(5):
   kinolar.append(input(f"{k+1} - kino:"))
print(kinolar)

#5
# Foydalanuvchining bugun nechta odam bn suhbat qurganini so'rang  va har bir suhbatlashgan insonini ismini birma bir so'rab royhatga yozing va royhatni konsulga chiqaring  
people=int(input("Bugun nechta inson bilan suhbat qurdingiz ? >>>"))
ism=[]
for n in range(people):
     ism.append(input(f"{n+1} - suhbat qilgan odamlaringiz kim edi ?:"))
print(ism)

# yakunlandi









