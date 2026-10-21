import requests

valyuta = input("Valyuta: ")
valyuta = valyuta.upper()

manzil = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

javob = requests.get(manzil)
kurslar = javob.json()

topildi = False

for kurs in kurslar:
    if kurs["Ccy"] == valyuta:
        print("1", valyuta, "=", kurs["Rate"], "so'm")
        topildi = True
        break

if topildi == False:
    print("Bunday valyuta topilmadi.")