# Xatamjonov Ulugbek 
# 2021-01-06 / 11:22
# Dasturlash asoslari
# 5-dars Srting (Matn)
# Amaliyot

#1
#  Quidagi o'zgaruvchilarni yarating
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"

# #2
#  Yuqoridagi o'zgaruvchilarni jamlab , quidagi ko'rinisha knsulga chiqaring.
print( kocha , "ko'chasi," , mahalla , "mahallasi,", tuman , "tumani," , viloyat , "viloyati," ,)

#3
# Yuqoridagi o'zgaruvchilarni qiymatini foydalanuvchilardan so'rang, va avvalgi mashqni takrorlang.
print("Iltimos , quidagi ma'lumotlrni kiriting:")

kocha=input("Ko'changiz:")
mahalla=input("Mahallangiz:")
tuman=input("Tumaningiz:")
viloyat=input("Viloyatingiz:")
print( "Sizning manzilingiz:" , kocha ,"ko'chasi" , mahalla , "mahallasi" , tuman , "tumani" , viloyat  , "viloyati")


# #4
#  yuqoridagi manzilni f"" yordamida yangi , manzil deb nomlangan o'zgaruvchig yuklang.
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
manzil=f" {kocha} ko'chasi , {mahalla} mahallasi ,{tuman} tumani  ,{viloyat} viloyati "
print(manzil)

# #5
#  manzil ga title() , upper() , lower() , metodlarini qo'llang.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())

#yakunlandi.













