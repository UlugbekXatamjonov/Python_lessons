"""
Created  21:43:34   09/06/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulug'bek 

#32 -dars: Dunder metodlar bilan ishlash

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

#1
# Avvalgi darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metolarni qo'shisgni mash qiling
# Obyekt haqida malumot(__repr__) , talabalarni bosqichi bo'yicha solishtirish(__lt__, __eg__ va hokazo)

# Avvaliga #32- darsimizdagi claslarni yozib olamiz.
# keyin esa berilgan shartni bajaramiz

class Shaxs:
    """ Shaxs classi """
    
    def __init__(self,ism,familya,yosh,passport):
        self.ism = ism.title()
        self.familya = familya.title()
        self.yosh = yosh 
        self.passport = passport
    
    def get_ism(self):
        return self.ism.title()
    
    def get_sname(self):
        return self.familya.title()
    
    def get_age(self):
        return self.yosh
    
    def update_age(self,age2):
        self.yosh = age2
        return self.yosh
    
    def get_passport(self):
        return self.passport
    
    def __repr__(self):
        return f"Shaxs: {self.ism.title()}  {self.familya.title()}. {self.ism.title()} hozirda {self.yosh} yoshda. Uning passport raqami: {self.passport}  "

    
class Talaba:
    """ Talaba classi """
    ts = 0
    def __init__(self,name,surname,age,idn,group,bosqich):
        self.name = name
        self.surname = surname
        self.age = age
        self.idn = idn 
        self.group = group
        self.bosqich = bosqich
        Talaba.ts += 1
        
    @classmethod
    def get_stn(cls,ts):
       """Ro'yhatdan o'tgan talabalarning sonini qaytaradi"""
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
    
    def get_bosqich(self):
        return self.bosqich
    
    def __repr__(self):
        return f"Talaba: {self.name.title()} {self.surname.title()}. {self.name.title()} hozirda {self.age} yoshda va {self.group.title()} guruhi talabasi. Talabaning raqami: {self.idn}"
    
    def __lt__(self,y):
      return self.bosqich > y
     
    def __ge__(self,y):
      return self.bosqich <= y
   
    def __eq__(self,y):
      return self.bosqich == y    
        
#2 
# Fan degan yangi class yarating. fan obyektlari tarkibida shu fanga yozilgan
# talabalarning ro'yhati saqlansin . Buning uchun fanga add_studens(),
# __getitem__ , __len__ kabi metodlarni qo'shing.

class Fan:
    """Fan classi"""
    talabalar_soni = 0
    def __init__(self,nom,*qiymat):
        self.nom = nom
        self.talabalar = [1,2]
        Fan.talabalar_soni += 1
        
    def __repr__(self):
        return f"{self.nom} fani"
        
    def get_fan(self):
        return self.nom
    
    def get_talabalar(self):
        return list(self.talabalar[:])
    
    def get_talabalar_soni(self):
        return self.talabalar_soni
    
    def add_talaba(self,talaba):
        if isinstance(talaba,Talaba):
            self.talabalar + talaba
            return list(self.talabalar)
            

        
    def __getitem__(self,index):
        return self.talabalar[index]

            
    def __len__(self):
        return len(self.talabalar)






talaba1 = Talaba("ilgor","jamoliddinov",20,1290874,"qurilish",3)
talaba2 = Talaba("turdali","tursinaliyev",18,3456711,"energetika",1)
talaba3 = Talaba("sevinch","xasanova",22,4537751,"tibbiyot",2)
talaba4 = Talaba("aaa","ddd",22,6575832,"mm",5)

shaxs1 = Shaxs("ulugbek","xatamjonov",20,"AB6414036") 
shaxs2 = Shaxs("jahongir","isaqov",24,"AA3457724") 
shaxs3 = Shaxs("nodirjon","jorayev",20,"AB5679120")

fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Adabiyot")

#yakunlandi
