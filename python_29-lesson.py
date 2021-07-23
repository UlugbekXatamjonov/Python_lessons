"""
Created  22:25:34   22/05/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#29-dars: Class

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""
#1
# Avto degan yangi class yarating unga avtomobillarga tegishli bo'lgan bir
# nechta xususiatarni qo'shing . Ayrim xususiatlarga standart qiymat bering.

class Avto:
    def __init__(self,kom,model,rang,karobka,narh,yil):
        self.kom= kom
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.yil = yil
        self.km = 0
#2
# Avtoga oid obyektlarning xususiatlarini qaaytaradigan metodlar yozing.
# get_info() metodi avto haidagi malumotlarni matn ko'rinishida to'liq qaytarsin
    def get_kom(self):
        return self.kom
    
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_karobka(self):
        return self.karobka

    def get_narh(self):
        return self.narh
    
    def get_yil(self):
        return self.yil
        
    def get_km(self):
        return self.km
        
    def get_info(self):
        return f"{self.kom} kompaniasining {self.model} modeldagi mashinasi. Rangi {self.rang}, boshqaruv {self.karobka}, {self.yil}-yili ishlab chiqarilgan,{self.km} km masofa yurgan, narxi {self.narh} $"
#3
# Avto ga oid obyektlarning xususiatlarini yangilaydigan metod yozing.
# update_km() metodi sn qabul qilib olib, avtomobilni yurgan masofasini yangilab ko'rsatsin

    def update_km(self):
        info = int(input("Yangi masofani kiriting:  "))
        self.km += info

#4
# Yangi Avtosalon degan class yarating va kerakli xususiatlar bilan to'ldiring.
# (salon nomi, manzil, sotuvdagi avtomobillar va hokazo)

class Avtosalon:
    """Avtosalon classi"""
    
    def __init__(self,nom,manzil,sotuv):
        self.nom = nom
        self.manzil = manzil
        self.sotuv = sotuv
        self.avtolar = []
        self.avtolar_soni = 0 
        
    def get_name(self):
        return self.nom
    
    def get_manzil(self):
        return self.manzil
    
    def get_sale(self):
        return self.sotuv
    
    def salon_info(self):
        return f"{self.nom} avto saloni.Manzil: {self.manzil}"
    
    def mashinalar(self):
        return self.avtolar
    
    def msoni(self):
        return self.avtolar_soni
    
#5
# Avtosalonga yangi avtolar qo'shish uchun metod yozing 
    def add_avto(self,avto):
        self.avtolar.append(avto)
        self.avtolar_soni += 1

#6
# Avtosalondagi avtomashinalar haqida malumot qaytaruvchi metod yozing
    def get_car_info(self,car):
        info1 = f"{self.nom} avtosalonidagi {car.kom} mashinasi haqida malumot: "
        info2 = f"{car.kom} kompaniasining {car.model} modeldagi mashinasi. Rangi {car.rang}, boshqaruv {car.karobka}, {car.yil}-yili ishlab chiqarilgan,{car.km} km masofa yurgan, narxi {car.narh} $"
        return info1 + info2

#7
# dir() va __dict__ metodi yordamida uzingiz yozgan va Pythondagi turli klass va obyektlarning
# xususiatlari va metodlarini toping(dir(str), dir(int) va hokazo ) 

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]


car1 = Avto("Lexux","D4","qora","avtomat",23000,2019)
car2 = Avto("Kia","mako","oq","avtomat",18000,2020)
car3 = Avto("Porshe","G9 siler ","silver","avtomat",31000,2021)

salon1 = Avtosalon("Avto Market","Namanan viloyai,Chust tumani Yorqishloq qishlogi,Bog'i eram ko'chasi 2-uy",231)
salon2 = Avtosalon("Best Avto","Toshkent viloyati,Norin tumani Dasturchilar ko'chasi 404-uy",135)
salon3 = Avtosalon("Gold Avto Tech", "Buxor viloyati sang tumani Ahmat Farg'oniy ko'chasi 1-uy",178)

# yakunlandi












