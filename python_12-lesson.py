"""
Created  22:31:17 30/03/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#12-dars: Xatolar bilan ishlash

Amaliyot https://python.sariq.dev  web sahifasi asosida

"""
# Biz ushbu darsimizda xatolar ustida ishlaymz. bizga malum bir kodlar berilgan biz esa anashu kodlardagi xatolarni topishimiz va to'g'irlashimiz kerak bo'ladi.

#1
# berilishi
# son = int(input("Juft son kiriting: ")
# if son 2!=0 :
#     print("Bu son juft emas.')
# else:
#     print("Rahmat!"))

# yechim
son = int(input("Juft son kiriting: "))
if son%2!= 0 :
    print("Bu son juft emas.")
else:
    print("Rahmat!")        



#2
# berilishi
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18 
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")

# yechim
yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18 :
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


#3
# berilishi
# x = float(input("Birinchi sonni kiriting: ")
# y = float(input("Ikkinchi sonni kiriting: ")
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}")
# else
#     print(f"{x}>{y}")

# yechim
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
if x==y :
    print(f"{x}={y}")
elif x<y :
    print(f'{x}<{y}')
else :
    print(f"{x}>{y}")
    
    
#4 a)
# berilishi
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun'


# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

# yechim

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat :
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")            

#4 b) 
# berilishi 

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:" ))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#    print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# yechim

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:" ))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
for mahsulot in mavjud_emas:
  print(mahsulot)


#5
# berilishi
# users = ['alisher1983','aziza','yasina' 'umar']

# login = input("Yangi login tanlang:' )

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!"

# yechim

users = ['alisher1983','aziza','yasina' ,'umar']
login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")


#6
# berilishi
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# yechim

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,10000000000000000000000000):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# yakunlandi













