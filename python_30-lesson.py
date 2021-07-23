"""
Created   13:23:34   23/05/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#30-dars: Vorislik va polimorfizm

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1
# Talaba klasiga yana bir fanlar degan hususiat qo'shing. Bu hususiat parametr sifatida
# uzatilmasin va obyrkt yaratilganida bo'sh ro'yhattan iborat bo'lsin

class Shahs:
    def __init__(self,ism,familya,passport,tyil):
        """Shahs haqida malumot"""
        self.ism =ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Malumot beruvcgi funksia"""
        return f"{self.ism} {self.familya} , passport raqami>>> {self.passport}, {self.tyil}-yilda tug'ilgan "


#3        
# Talaba klasiga fanga_yozil() degan metod yozing. bu metod parametr sifatida 
# Fan klasiga tegishli obyektlarni qabul qilsin va talabaning fanla ro'yhatiga qo'shib qo'ysin

class Talaba(Shahs):
    """Talaba klassi"""
    def __init__(self,ism,familya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_fanlar(self):
        return self.fanlar
            
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        return self.fanlar  
 
#4
# Talabaning fanlar ro'yhatidan biror fanni o'chirib tashlash uchun remove_fan()
# metodini yozing agar bu metodaga ro'yhatda yo'q fan yozilsa "Siz bu fanga yozilmagan siz" 
# degan habarni qaytarsin  
 
    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return f"Siz bu fanga yozilmagansiz"
    
    
#2    
# Fan degan alohida klass yarating va bu kassdan turli fanlar uchun alohida obyektlar yarating

class Fan:
    """Fan clasi"""
    def __init__(self,nom,tur):
        self.nom = nom
        self.tur = tur
    
    def get_name(self):
        return self.nom
    def get_info(self):
        return  f"{self.nom} fani {self.tur} fanlar qatoriga kiradi."
 


shahs1 = Shahs("Ulugbek","Xatamjonov","AB6414036",2001)
shahs2 = Shahs("Doniyor","Mamajonov","AB3457722",2005)
shahs3 = Shahs("Vali","Aliyev","AC5671988",1994)

talaba1 = Talaba("Mahmud","To'lanov","AB2908764",2000,1237783)
talaba2 = Talaba("Asadbek","Mirzaanvarov","AB4539855",1997,6458299)
talaba3 = Talaba("Aziz","Soliyev","AN5447123",1987,7864562)

fan1 = Fan("Algebra","aniq")
fan2 = Fan("Ona tili","ichtimoiy")
fan3 = Fan("Kimyo","tabiy")

#yakunlandi







