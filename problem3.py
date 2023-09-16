cümle_girisi=input("Cümle girişi tanımlayınız:")
buyuk_harf=[]
kucuk_harf=[]
sayı=[]

for i in cümle_girisi:
    if i ==" ":
        continue
    elif i.islower():
        kucuk_harf.append(i)
    elif i.isupper():
        buyuk_harf.append(i)
    else:
        sayı.append(i)
sum=buyuk_harf + kucuk_harf + sayı
print("".join(sum))
        