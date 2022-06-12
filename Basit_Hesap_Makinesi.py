print("""
Basit Hesap Makinesi

1. Toplama İşlemi
2.Çıkarma İşlemi
3.Çarpma İşlemi
4.Bölme İşlemi
""")

a = int(input("1.Sayıyı Giriniz:"))
b = int(input("2.sayıyı Giriniz:"))

işlem = input ("işlem numarasını giriniz:")

if  (işlem == "1"):
    print("{} + {} = {}".format(a,b,a+b))

elif   (işlem == "2"):
    print("{} - {} = {}".format(a,b,a-b))

elif    (işlem == "3"):
    print("{} * {} = {}".format(a,b,a*b))

elif   (işlem == "4"):
    print("{} / {} = {}".format(a,b,a/b))

else :
    print("İşlem Geçersiz.")


