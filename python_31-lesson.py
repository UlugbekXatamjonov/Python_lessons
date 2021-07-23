"""
Created   :23:34   /06/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#31-dars:   INKAPSULYATSIYA VA KLASSGA OID
          XUSUSIYAT VA METODLAR

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

# 1
# Shaxs va talaba degan classlar yarating va ularga yopiq xususiatlar qo'shing
# va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi funksialar yozing  

# 2
# Yuqoridagi classlarga talabalar_soni va odamlar_soni degan classga oid xususiatlar qo'shing 

# 3
# Classga oid xususiatlar  bilan ishlash uchun @classmethod lar yozing


class Shaxs:
    """Shaxs haqidagi class"""
    
    def __init__(self,ism,familya,yosh,passport):
        self.__ism = ism
        self.__familya = familya
        self.yosh = yosh 
        self.passport = passport
    
    def get_ism(self):
        return self.__ism.title()
    
    def get_sname(self):
        return self.__familya.title()
    
    def get_age(self):
        return self.yosh
    
    def update_age(self,age2):
        self.yosh = age2
        return self.yosh
    
    def get_passport(self):
        return self.passport

    
class Talaba:
    """Talaba haqidagi class"""
    ts = 0
    def __init__(self,name,surname,age,idn,group):
        self.__name = name
        self.__surname = surname
        self.age = age
        self.idn = idn 
        self.group = group
        
        Talaba.ts += 1
        
    @classmethod
    def get_stn(cls,ts):
       """uuu"""
       return cls.ts
    
    def get_name(self):
        return self.__name 
    
    def get_surname(self):
        return self.__surname
    
    def get_age(self):
        return self.age
    
    def get_idn(self):
        return self.idn

    def get_group(self):
        return self.group.title()
    

talaba1 = Talaba("ilgor","jamoliddinov",20,1290874,"qurilish")
talaba2 = Talaba("turdali","tursinaliyev",18,3456711,"energetika")
talaba3 = Talaba("sevinch","xasanova",22,4537751,"tibbiyot")
talaba4 = Talaba("aaa","ddd",22,6575832,"mm")

shaxs1 = Shaxs("ulugbek","xatamjonov",20,"AB6414036") 
shaxs2 = Shaxs("jahongir","isaqov",24,"AA3457724") 
shaxs3 = Shaxs("nodirjon","jorayev",20,"AB5679120") 

#yakunlandi
