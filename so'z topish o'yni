
import random as rd

print("Siz son o'ylang va boshlang'ich va yakuniy chegaralarni kiriting, men topaman.")
boshlangich_chegara = int(input("Boshlang'ich chegara: "))
yakuniy_chegara = int(input("Yakuniy chegara: "))
taxminlar = []

while True:
    taxmin = rd.randint(boshlangich_chegara, yakuniy_chegara)
    if taxmin not in taxminlar: 
        javob = input(f"Siz {taxmin} ni o'yladingizmi? (H, Y) ")
        if javob.lower() == "h":  
            print(f"{taxminlar}shuncha urinishda men siz o'ylagan sondi topdim{taxmin}")
            break
        taxminlar.append(taxmin)
