import pandas as pd

kitoblar={
    'badiy':['ikki eshik orasi',"o'tgan kunlar",'mehrobdan chayon'],
    'ilmiy':['ensklopediya','mashinalar olami','supper va oddiy mashina farqi'],
    "qo'llanmalar":["lug'atlar","yo'riqnoma",'xaritalar']
}
df=pd.DataFrame(kitoblar)
print(f'{df} \n  shu kitoblar bor')
kerakli_kitob=input('qaysi kitob kerak? ').lower()
if df.loc[0,'badiy']==kerakli_kitob or df.loc[1,'badiy']==kerakli_kitob or df.loc[2,'badiy']==kerakli_kitob:#indeks orqali chaqirish 
    print('bu kitob bor')
    dalniy=['isim','pasport','manzil']
    isim=input("to'lliq ismingizni kirgazing? ").lower().strip()
    pasport=input('pasport seriya raqamlarizni kirgazing? ').lower().strip()
    manzil=input('yashash joyizni kirgazing? ').lower().strip()
    
    dalniy1=[isim,pasport,manzil]
    if ""in dalniy1:
        print('malumot toliq emas!')
    elif not "" in dalniy1:
        print('malumotlar toliq.')
        mudat='7 kunda'
        qaytarish=input('kitobni qancha voqitda qaytarasiz? ')
        if qaytarish==mudat:
            print('kitobni olishiz mumkun')
        else:
            print('berilmaydi kitob uzoq mudatga!')
elif kerakli_kitob in df['badiy'].values or kerakli_kitob in df['ilmiy'].values or kerakli_kitob in df[ "qo'llanmalar"].values:#ustun orqali
    print('bor bu kitob')
    dalniy=['isim','pasport','manzil']
    isim=input("to'lliq ismingizni kirgazing? ").lower().strip()
    pasport=input('pasport seriya raqamlarizni kirgazing? ').lower().strip()
    manzil=input('yashash joyizni kirgazing? ').lower().strip()
    
    dalniy1=[isim,pasport,manzil]
    if ""in dalniy1:
        print('malumot toliq emas!')
    elif not ""in dalniy1:
        print('malumotlar toliq.')
        mudat='7 kunda'
        qaytarish=input('kitobni qancha voqtda  qaytarasiz? ')
        if qaytarish==mudat:
            print('kitobni olishiz mumkun')
        else:
            print('kitob berilmaydi uzoq mudatga')
        
else:
    print('xato') 