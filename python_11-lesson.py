# Xatamjonov Ulugbek 
# 2021-03-27 / 6:18
# Dasturlash asoslari
# 11-dars Bir nechta shartlarni tekshirish 
# Amaliyot

#1
# Foydalanuvchidan juft son kirirtishini so'rang . Agar u juft son kirirtsa ""Rahmat , juft son kiriritmasa "Kechirasiz bu juftb son emas " degan yozuvni konsulga chiqaring.

son = float(input('Juft son kiriting >>>'))
if son%2!= 0 :
    print('Bu juft son emas !')
else :
    print("Rahmat")

#2
# Foydalanuvchi yoshini so'rang va muzeyga kirish uchun chipta narxini quidagicha belgilang :
# 1) Agar foydalanuvchi 4 yoshdan kichik va 60 yoshdan katta bo'lsa bepul : 
# 2) Agar foydalanuvchi 18 yoshdan kichik bo'lsa 10000 so'm :
# 3) Agar foydalanuvchi 18 yoshdan katta bo'lsa 20000 so'm .

yosh = int(input("Yoshingiz nechida ? >>>"))
if yosh<=4 or yosh >=60 :
    narx=0 
elif yosh<=18 :
    narx=10000
elif yosh>18 :
    narx=20000 
print(f"Chipta {narx} so'm ")

#3
# Foydalanuvchidan 2 ta son kiritishini so'rang , sonlarni taqoslang va teng , kata yoki kichikligi haqida habar bering .

a = float(input("1-sonni kirirting:"))
b = float(input("2-sonni kirirting:"))
if a>b:
    print(f"{a}>{b}")
elif a<b:
    print(f"{a}<{b}")
else :
    print(f"{a}={b}")

#4
# mahsulot degan ro'yhat yarating va kamida 10ta mahsulotni kirirting . yngi savat degan ro'yhat yarating va foydalanuvchidan savatga kamida 5ta mahsulotni kiritishini so'rang . savatdagi elementlarni mahsulotlar ro'yhati  bilan solishtiring va qaysi birir ro'yhatda bo'lsa , "mahsulot do'konimizd abor"  aks holda, "mahsulot do'konimizda yo'q " degan xabarni chiqaring .

mahsulotlar = ["olma","non","gurunch","go'sht","sabzi","garoh","yog'","shakar","novvot","salfetka"]
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
   
if savat :   
    for mahsulot in savat :
        if mahsulot in mahsulotlar :
          print(f"Do'konimizda {mahsulot} bor.")
        else:
          print(f"Do'knimizda {mahsulot} yo'q.")
else:
    print("Savatingiz bo'sh.")
    
#5

users = ["admin", "ulug'bek","paol","admiral","sergey"]
login = input("login tanlang:")
if login in users :
    print("Login band ! Yangi login tanlang>")
else:
    print("Hush kelibsiz !")

#6

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# yakunlandi



















