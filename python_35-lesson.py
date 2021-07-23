"""
Created  21:16:34   17/06/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#35 -dars: XATOLAR BILAN ISHLASH

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

# try-except bilan ishlash

#1

yosh = input("Yoshingizni kiriting: ")

try:
    yosh = int(yosh)
except ValueError :
    print("Butun son kiritmadingiz.")
else:
    print(f"Siz {2021-yosh}-yilda da tug'ilgan ekansiz.")
    
#2

x,y = 5,10

try:
   a = y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi. ")
else:
    print({a})

#yakunlandi














