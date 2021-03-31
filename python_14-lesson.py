"""
Created  22:31:17 30/03/2021

Dasturlash asoslari

Muallif: Xatamjonov Ulugbek 

#14-dars: Funksiya  bilan tanishuv

Amaliyot https://python.sariq.dev  web sahifasi asosida

"""
#1
# Otam(onam , ukam ...) degan lug'at yarating va lug'atga kamida 3 ta ma'lumot kiriting . Lug'atdagi ma'lumotlarni konsulga atn ko'rinishida chiqaring.  
otam= {"ism":"ilxomjon", "tyil":1977 , "viloyat":"namangan" }
ism= otam["ism"]
tyil= otam["tyil"] 
vil= otam["viloyat"] 
print(f"Otamning ismi {ism.title()} , {tyil}-yilda {vil.title()} viloyatida tug'ilgan.")

onam= {"ism":"nasiba", "tyil":1979, "viloyat":"namangan"}
ism= onam["ism"]
tyil= onam["tyil"]
vil= onam["viloyat"]
print(f"Onamning ismi {ism.title()} , {tyil}-yilda  {vil.title()} viloyatida tug'ilgan ")

#2
# Oila azolaringizning sevimli tamolari lug'atini tuzing . Lug'atda kamida ism-taom juftligi bo'lsin. Kamida 3 kishing sevimli taomini konsulga chiqaring.
taomlar= {"otam":"osh","onam":"mastava","ukam":"shashlik", "men":"manti", "singlim":"dimlama"}
taom= taomlar["otam"]
print(f"Otamning sevimli taomi {taom.title()}.")

taom= taomlar["onam"]
print(f"Onamning sevimli taomi {taom.title()}.")

taom= taomlar["ukam"]
print(f"Ukamning sevimli taomi {taom.title()}.")

#3
# Python izohli lug'atini tuzing : Lug'atga shu kungacha o'rgangan 10 ta so'zni(atamani) ni kiriting va ularning qisqacchatarjimasini yozing .
python_lugati ={
"print":"konsulga yozilgan dasturni chiqarib berdi.",
"if":"agar deb tarchima qilinadi va birinchi shartni bajaradi",
"else":"yoki deb tarchima qilinadi va qolgan shartni bajaradi",
"elif":"ikinchi va boshqa shartlarni bajaradi",
".title":"Bu metod berilgan so'zni birinchi harfini konsulga katta qilib berib chiqaradi.",
".upper":"Bu metod berilgan so'zni konsulga bacha harflarini katta qilib berib chiqaradi.",
}
print(python_lugati["print"])

#4
# Foydalanuvchidan biror so'z kiritishini so'rang va kiritilgan so'zni yuqoridagi lug'atdan chiqarib bering . Agar so'z lug'atda mavjud bo'lmasa , "Bunday so'z lug'atda mavjud emas" degan xabarni chiqaring.
eng_uz = {
"apple":"olma",
"pear":"nok",
"peanapple":"ananas",
"fig":"anjir",
"stawberry":"qulupnay",
"greip":"uzum"
}

soz = input("Biror meva nomini kiriting: ").lower()
if eng_uz != soz :
    print(eng_uz.get(soz, "Bunday so'z mavjud emas."))
else :
    print(eng_uz.title())
    

# yakunlandi

