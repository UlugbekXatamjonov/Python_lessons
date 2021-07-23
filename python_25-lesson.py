"""
Created  21:30:34  22/04/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#25-dars: Son topish o'yini

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

# Start
print("Keling o'ylagan sonni topish o'ynaymiz!")

import random

def sontop(x=10):
    
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi? ", end="")
    taxminlar = 0
    
    while True:
        taxminlar +=1
        taxmin = int(input(">>>"))
        if taxmin > tasodifiy_son :
            print(f"Men o'ylagan son {taxmin} dan kichikroq, Yana urunib ko'ring.")
        elif taxmin < tasodifiy_son :
            print(f"Men o'ylagan son {taxmin} dan kattaroq, Yana urunib ko'ring.")
        else:
            break
        
    print(f"Tabriklayman siz {taxminlar}ta taxmin bilan topdingiz.  ")
    return taxminlar

def sontop_kom(x=10):
    input(f"1 dan {x} ga son o'ylang va istalgan tugmani bosing , men topaman >>>")
    yuqorison = x
    quyison = 1
    taxminlar = 0
    while True:
         taxminlar += 1
         if quyison != yuqorison:
            taxmin = random.randint(quyison,yuqorison)
         else:
            taxmin = quyison
         javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
         if javob == "-":
            yuqorison = taxmin - 1
         elif javob == "+":
            quyison = taxmin + 1
         else:
             break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_kom = sontop_kom(x)
        taxminlar_user = sontop(x)        
        
        if taxminlar_user>taxminlar_kom:
            print(f"Men {taxminlar_kom} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_kom:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))
            
play(10)

# yakunlandi




















