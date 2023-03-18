"""
## SORU 1
PYTHON'DA VERI TIPLERI:
1. Sayisal Veri Tipleri : Int, float ve complex olmak üzere 3'e ayrilir. Int -> tam sayilari (10), float -> ondalik sayillari (10.5), 
   complex -> karmasik sayilari temsil eder.
2. String Veri Tipi : Cift tirnak ("") isareti ile gösterilen metinsel ifadeleri temsil eder.
3. List (Liste) Veri Tipi : Birlesik veri tipidir. Liste icindeki ogeler, koseli parantez ([]) icinde virguller ile ayrilmis sekilde bulunnur.
4. Tuple Veri Tİpi : Liseteye benzer bir veri turudur fakat farkli olarak odeler parantez (()) icine alinir ve oge sayisi degistirelemez.
5. Dictionary Veri Tipi : Veri depolamak icin kullanilir.
6. Küme Veri Tipi :  Veri koleksiyonu depolamak icin kullanilir. Siralanmamis, degistirelemez ve dizinlenmemis bir koleksiyondur.
7. Boolean Veri Tipi : True ,False ciktisi veren sartli bir ifadedir.
"""

"""
## SORU 2
Siteye girdigimizde kurs isimlerini goruyoruz. 2023 Yazilim Gelistirici Yetistirme Kampi bir stirng veri tipine ,
tamaladigimiz kurslarin yuzdesi ise sayisal veri tiplerine ornektir.
"""
## SORU 3
# ORNEK 1
email = "email@outlook.com"
password = "password"

if email == "email@outlook.com":
    if password == "password":          
        print("Giris Yaptiniz")
elif email == "email@outlook.com":
    if password != "password":
        print("Email adresiniz veya sifreniz hatali. Tekrar Deneyiniz.")
# ORNEK 2
bitirVeDevamEt = True 

if bitirVeDevamEt:
    print("Ders tamamlandi. Bir sonraki derse gecebilirsiniz.")
else:
    print("Dersi tamalamadan bir sonraki derse gecemezsiniz.")