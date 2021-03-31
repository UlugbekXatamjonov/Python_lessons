# Xatamjonov Ulugbek 
# 2021-01-13 / 19:11
# Dasturlash asoslari
# 8-dars Ro'yhat ustida amallar
# Amaliyot

#1
# O'zingizga ma'lum davlatlarning ro'yhatini tuzing va uni konsulga chiqaring 
davlatlar=("Daniya" ,"Angilya","Malayzia","Shvetsia","Rossia" ) 
print(davlatlar)

#2
# Ro'yhatning uzunligini konsulga chiqaring
print(len(davlatlar))

#3
# sorted() funksiasi yordamida ro'yhatni tartiblangan holatda konsulga chiqaring
print(sorted(davlatlar)) 

#4
# sorted() yordamida ro'yhatni teskari ko'rinishda konsulga chiqaring
print(sorted(davlatlar , reverse=True))

#5
# 120 dan 1200 gacha bo'lgan juft sonlar ro'yhatini tuzing
sonlar=list(range(120,1200))
print(sonlar)

#6
# Ro'yhatdagi sonlar yig'indisini toping va uni konsulga chiqaring
print(sum(sonlar))

#7
# Ro'yhatdagi eng katta va eng kichik son o'rtasidagi ayrmani hisoblang va konsulga chiqaring
print(max(sonlar) + min(sonlar)) 

#8
# Ro'yhatdagi elementlar sonini konsulga chiqaring
print(len(sonlar))

#9
# Ro'yhatning boshidan , o'rtasidan , oxiridan 20 ta elementni konsulga chiqaring

print(sonlar[:20])
print(sonlar[20:40])
print(sonlar[1050:1080])

#10
# taomlar degan ro'yhat yarating va ichiga 5 ta taomni kiriting
taomlar=("Osh","shashlik","manti","sho'rva","bog'irsoq")
print(taomlar)

#11
# nonushta degan yangi ro'yhatga taomlardan nusha olig
nonushta=()
nonushta=taomlar[:]
print(nonushta)

#12
# yangi ro'yhatda faqat nonushtada yeyiladigan taomlar qoldiring va yangi 2 ta taom qo'shing

nonushta.remove("Osh")
print(nonushta)

# yakunlandi





