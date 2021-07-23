'''
print("")   ifoda yoki matinni konsulga chiqarish uchum ishatiladi
/n          matinni qatorlarga ajratish uchun ishlatilad

f" "        yordamida matnlarni birlashtirish mumkin
/t          uzun tire qoldiradi
.lstrip     matning chap qismidagi bo'shliqni olib tashlaydi
.rstrip     matning o'ng qismidagi bo'shliqni olib tashlaydi  
.strip      matning ikkala qismidagi bo'shliqni olib tashlaydi'  

input()     foydalanuvchidan malumot olish un ishlatiladi
int()       malumotni butun son ko'rinishida uzatadi 
float()     malumtni o'nli son ko'rinishida uzatadi 
str()       malumtni matn ko'rinishida uzatadi
.upper()    hamma hariflarni katta qilib beradi
.title()    birinchi harifni katta qilib beradi
.lower()    hamma hariflarni kichkina qilib beradi
.capitalise()                  matinfagi hamma sozlarning birinchi harifini katta qilib beradi

.append(qiymat)                ro'yhatning ohiriga  element qo'shadi
.insert(index,qiymat)          ro'yhatning istalgan joyiga element qo'shadi
del o'zgaruvchi_nomi[index]    ro'yhatdan elementni o'chiradi
.remuve(qiymat)                ro'yhatdan elementni qiymati bo'yicha o'chiradi 
.pop(indeks)                   ro'yhatdan biror elementni sug'urub oladi

.sort()                  "ro'yhatni alifbo bo'yicha taxlaydi (a b c..)"
.sort(reverse=True)       ro'yhatni alifbo bo'yicha teskarisiga taxlaydi(z x v ... b a )
.sorted( )                asl ro'yhatni o'zgartirmasdan (ro'yhatni bir martalik alifbo bo'yicha) taxlaydi.
.reverse()                ro'yhatni boshi va oxirini o'zgartirib taxlaydi (abc-cba)


abs()           absalyut qiymatni ko'rsatadi. M: abs(-5) = 5
pow()           darajaga ko'tarish
round()         yaxlidlaydi 

#from  math 
floor()         yahlidlaydi: pastki chiziq bo'yicha
ceil()          yahlidlaydi: pastki yuqori bo'yicha
sqrt()          ildizdan chiqaradi

len()                     royhatdagi elementlar sonnini aniqlaydi 
range()                   malum bir oraliqdagi sonlar ketma ketligini yaratish uchun. list() yordamida esa bu oraliqni esa ro'yhat ko'rinishiga keltiramiz.(list(range(0,10))) bo'lsa o dan 9 gacha sonlar chiqadi .
list()                    ro'yhat yaratadi
range()                   da list(range(0,10,2)) bo'lsa juft sonlarni erish mumkin .(0,2,4,8) 
min()                     ro'yhatdagi eng kichik sonni topish uchun
max()                     ro'yhatdagi eng katta sonni topish uchun .
sum()                     ro'yhatdagi sonlarning yig'indisini topish uchun 
ro'yhat_nomi[0:3]         bunda ro'yhatdagi 0 dan 2 gacha (2 ham) sonlarni qirqib oladi

2-ro'yhat_nomi=1-ro'yhat_nomi[:]       bunda 1 dan 2 ro'yhatga nusxa olinadi 
ro'yhat_nomi() - yani tuples           bunda o'zgarmas ro'yhat tuziladi

for ### in ####                        bunda ro'yhat ichidagi har bir elementni alohida aohida konsulga chiqaradi

if           shart yozish uchun 
else         shart bajrilmasa 
elif         shart yozish un
==           tengmi ?
!=           teng bo"lmasa
and          va operatori
or           yoki operatori
boolean      malumotlar turi.True yoki False / 1 yoki 0 orqali belgilash mn 
in          operatori orqali "ichidami" ni tekshirish mn
not in      "ichida" emasmi ni tekshirish mn 
  
lug'at_nomi = {'kalit_so'z':'qiymat'}            bu soda lug'at'
del lug'at_nomi = {'kalit_so'z':'qiymat'}        lug'atni o'chiradi 
.get           metodi yordamida 
.items()       lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin
.keys()        lug'atdagi kalit so'zlarni ko'rish uchun
.values()      lug'atdagi qiymatlarni chiqarish uchun 
set(lugat(ro'yhat,tupl...) nomi)     lugatdagi(...) kop bolib qolgan qiymatlardan faqat bittadan olib ch iqaradi

while        toki -gacha 
break        while ni to'xtatish un
continue    to'gri kelgan shartni tashlab o'tib ketadi
abadiy tsiklni to'xtatish un 'CTRL+C' ni bosish kerak

def              funksia yaratuvchi
print(funksia_nomi.__doc__)  funksia vazifasini konsulga chiqaradi
return           funksiadan qiymat qaytarish uchun 
None            standart qiymat (mavjud emas)
*args           istalgancha qiymat qabul qiluvchi argument
**kwargs        argumantga istalgancha qiymatni lug'at ko'rinishida qabul qiladi
import          metodni chaqiruvchi 
import x from y            x obyektni y dan chaqir
import "abc" as "a""       bu abc ni a nomiga pzgartivchi  

set()          obyektning hususiyatlarini o'zgartiradi'
get()          xususiatlarni qaytaradigan metod
pass           bo'sh obyekt bn to'ldiradi
isinstance(obyekt,class)    obyektni shu classga tegishli ekanini tekshiradi

Dunder         ikki pastgi chiziq ning qisqartmasi
__init__       classning hususiatlarini belgilaydi
__dict__       obyrktning hususiatlarini lygat qilib qaytaradi 
__str__        ma'lumot berish un 
__repr__       ma'lumot berish un
__getitem__    obyekt ichidagi elementni qaytaradi
__setitem__    obyrktga yangi element qo'shadi
__call__       obyektni chaqirish un ishlatiladi


x.__lt__(self,y)  x<y
x.__le__(self,y)  x<=y
x.__gt__(self,y)  x>y
x.__ge__(self,y)  x>=y
x.__eq__(self,y)  x==y
x.__ne__(self,y)  x!=y

x.__add__(self,y)   x+y   qo'shish
x.__sub__(self,y)   x-y   ayrish
x.__mul__(self,y)   x*y   ko'paytirish
x.__pow__(self,y)   x**y  darjaga ko'tarish
x.__div__(self,y)   x\y   bo'lish

.readlines()                file ichidagi har bir qatorni alohida o'qiydi'
.rstrip()                   qator ohiridagi "\n" belgisini oib tashlaydi
# import pickle             bu modul faylga narsa yozish un ishlatiladi
pickle.dump(obyekt,file)    yangi faylga o'zgaruvchi ni saqlash un

y = 32
y_json = json.dumps(dump-faylga yuklash un)(y)                    python formatidan jsonga o'tkazish un
o'zgaruvchi = json.loads(load-fayga yuklash un)(y_json)          json formatidan python ga  o'tkazish un
(y,indent=x)                              x ta joy tashlash chap tomondan
pprint          json fayllar bn ishda matnni konsulga chiroyli qilib chiqarish un ishlatiladi

try-except      istisno obyektlarni tutib olish uchun


### 38-darsdan standart kutub hona manzilini saqlab qo'yish #####

' ihanteregex.io '     andozalar syti
' PyPi.org '           python tashqi kutubhonasi











'''




