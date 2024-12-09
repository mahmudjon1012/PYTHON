talaba_jadvali=["dushanba:matematika va fizika",
                "seshanba:tarix,ingiliz tili",
                "chorshanba:jismoniy tarbiya,huquq,odobnoma",
                "payshanba:atrofimizdagi olam,fizika,geometiriya",
                "juma:algebra,geometiriya,fizika",
                "shanba:o'z ustizda ishlaydigon kuniz",
                "yakshanb: dam olish kuni"]
ustoz_jadvali=["dushanba: dars 5 sinifga va 9 sinifga",
               "seshanba:dars 4 va 6 siniflarga",
               "chorshanba:ota onalar majlisi",
               "payshanba:o'qtuvchilar majlisi"
               "juma:10 va 11 siniflarga dars ",
               "shanba: dam olish kuni",
               "yakshanba:uydagi ishlarni qilish"]
days=["dushanba",'seshanba','chorshanba','payshanba','juma','shanba','yakshanba']
who=input("""siz "teacher" yoki "student? """)  
name=input('ismiz nima? ').capitalize()
day=input(" hafta kunini kirgazin?")
if day in days:
    day_index=days.index(day)
    if who=='student':
        print(f"Salom\t   {name} sizning   {day}lik jadvalingiz:")
        print(talaba_jadvali[day_index])
    elif who=='teacher':
        print(f"salom{name}sizning{day}lik jadvalingiz:")
        print(ustoz_jadvali[day_index])
