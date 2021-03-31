# Xatamjonov Ulugbek 
# 2021-01-08 / 09:33
# Dasturlash asoslari
# 7-dars List (Jadval)
# Amaliyot

#1
# Ismlar degan ro'yhat yaratingda kamida 3 ta eng yaqin do'stingizni ismini kiriting
# Ro'yhatdagi har bir do'stingizga qisqa habar yozib konsulga chiqaring .
 
dostlar=['Quvonchbek','Nodirjon', 'Umarbek','Asadbek','Turdali']
print("Salom do'stim " , dostlar[0], ".""Yaxshi yurubsizmi ?")
print(dostlar[1] ,"bugun yig'ilmaymizmi , do'stlar birgalikda ? ")
print("Ishlar yaxshimi", dostlar[2], "." ,"IIA dan qachon qaytasan , imtihonlar tugab qoldimi ?" )

#2
# Sonlar dep nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang . 

sonlar=[]
sonlar.append(2)
sonlar.append(6)
sonlar.append(-9)
sonlar.append(8.1)
sonlar.append(34)
sonlar.append(3.3)
sonlar.append(-4.5)
print(sonlar)

#3
# Yuqoriagi ro'yhatdagi (#2) sonlar ustida turli arifmetik ammalar bajarib ko'ring . 

print(sonlar[0]  + sonlar[2])
print(sonlar[3]  + sonlar[6])
print(sonlar[4]  - sonlar[3])
print(sonlar[0]  - sonlar[5])
print(sonlar[1]  * sonlar[2])
print(sonlar[3]  / sonlar[2])
print(sonlar[2]  // sonlar[6])

# elementlarni o'zgartiramiz.
sonlar[5]=6
sonlar[3]=0
sonlar[2]=0.1

# Yangi element qo'shamiz.
sonlar.append(24)
sonlar.append(11)
sonlar.insert(3, 4)
sonlar.insert(8, -21)
print(sonlar)

#4
# t_shaxslar va z_shaxslar degan ikkita ro'yhat yarating va birinchisiga o'zingiz hurmat qiladigan tarixiy shaxslarni ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini  kiriting.
t_shaxslar=["Amir Temur","Ibn Sino","Al Xorazimiy","Mirzo Ulug'bek"]
z_shaxslar=["Pavel Durov","Bill Geyts","Lionel Messi","Mark Andre Ter Stagen","Asli Enver","Emma Vatson"]
print(t_shaxslar)
print(z_shaxslar)

#5
# Yuqoridagi (#4) ro'yhatlarning har biridan  bittadan qiymatni sug'urub olib ( .pop() ) , konsilga chiqaring.
print("Men tarihiy shahslardan ", t_shaxslar.pop(0),"bilan, zamonaviy shahslardan esa", z_shaxslar.pop(2),"bilan suhbat qurishni hohlardim.")
print("Men tarihiy shahslardan ", t_shaxslar.pop(1),"bilan, zamonaviy shahslardan esa", z_shaxslar.pop(1),"bilan suhbat qurishni hohlardim.")
print("Men zamonaviy aktirisalardan", z_shaxslar.pop(2), "va", z_shaxslar.pop(1), "bilan birga suratga tushishni istardim :) .")

#6
# friend nomli bo'sh ro'yhat tuzing va unga .append() yordamida 4 5 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends=[]
friends.append("Asadbek")
friends.append("Ilg'or")
friends.append("Mirazim")
friends.append("Nursaid")
print(friends)

#7
# Yuqoridagi ro'yhatdan(#6) mehmonga kela olmaydignlarni .remove( ) metodi orqali chiqarib tashlang.
friends.remove("Ilg'or")
print(friends)

#8
# Ro'yhatning(#6) boshiga , o'rtasiga va ohiriga yangi odamlarni qo'shing
friends.append("Javohir")
friends.append("Hojiakbar")
friends.insert(2,"Sunnatali")
friends.insert(6,"Dilshodbek")
print(friends)

#9
# Yangi mehmonlar dep nomlangan bo'sh ro'yhat yarating ,(.pop()) va .append() metodlari yordamida mehmonga kelgan do'stingizning ismini friends ro'yhatidan sug'ururib olib , mehmonlar ro'yhatiga qo'shing.
mehmonlar=[]
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))
# ushbu iiki isimni friends ro'yhatidan sug'urib oldik va mehmonlar ro'yhatiga qo'shdik.
print(mehmonlar)

# yakunlandi


