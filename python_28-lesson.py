"""
Created  22:23:24   19/05/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#28-dars: Class lar

Amaliyot https://python.sariq.dev  web sahifasi asosida.

"""

# 1
# Web sahifangiz uchun foydalanuvchi class ini tuzing.

class User:
    def __init__(self,name,username,gmail,number):
        self.name = name
        self.username = username 
        self.gmail = gmail
        self.number = number
        
    def get_name(self):
        """ Foydalanuvchi ismini qaytaruvchi metod """
        return self.name
    
    def get_uname(self):
        """ Foydalanuvchi usernameni qaytaruvchi metod """
        return self.username
    
    def get_gmail(self):
        """ Foydalanuvchi gmailini qaytaruvchi metod """
        return self.gmail
    
    def get_number(self):
        """ Foydalanuvchi raqamini qaytaruvchi metod """
        return self.nubmer
    
    def get_info(self):
        """ Foydalanuvchi haqida ummumiy malumot qaytaruvchi metod """
        return (f"Foydalanuvchi: '{self.username}', ismi: '{self.name}', emaili: '{self.gmail}'', tel. raqami: '{self.number}'")


user1 = User("Ulugbek","ulugbek17","xatamjonovulugbek17@gmail.com",993257417)
user2 = User("Ali","olimovb","alimov@gmail.com",914567866)
user3 = User("Usmon","usmonaziz","usmon1223@gmail.com",990997237)
user4 = User("Bekzod","beki","turbekzod001@gmail.com",973498230)

# yakunlandi




















