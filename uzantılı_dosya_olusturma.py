import time
print("""
***********************
Dosya Oluþturma Programý
***********************
1.Ýlk önce dosya ismi giriniz
2.Dosya uzantýsýný girin
3.Sonra oluþturulacak yeri seçin
Örneðin:
masaüstü    D:        belgeler

""")


isim=input("Oluþturulacak Dosyanýn ismini girin =")
uzanti=input("Dosya uzantýsý  =")
yol=(input("Nereye Oluþtululsun ="))

isimuzanti=isim+"."+uzanti
try:
    if yol=="masaüstü":
        print("Dosya oluþturuluyor..")
        time.sleep(2)
        print("Dosya oluþturuldu..")
        file =open("C:/Users/Omer/Desktop/"+isimuzanti,"a")


    elif yol=="D:":
        print("Dosya oluþturuluyor..")
        time.sleep(2)
        print("Dosya oluþturuldu..")
        file = open("D:/" + isimuzanti, "a")

    elif yol=="belgeler":
        print("Dosya oluþturuluyor..")
        time.sleep(2)
        print("Dosya oluþturuldu..")
        file = open("C:/Users/Omer/Documents/"+isimuzanti,"a")


    else:
        print("""       Hata aldýnýz !
        Bu hatanýn  sebepleri aþaðýdakilerden dolayý olabilir.
        1.Kodu copy paste yaptýysanýz file = open kýsmýný kendi Pc nize göre konumlandýrýn
        2.Girdiðiniz dosya adý veya uzantýsý hatalýdýr Örn(dosyaisminde ' ? 'iþareti olmaz.)""")
except:
    print("""Hata aldýnýz except;
          Bunu sebepleri aþaðýdakilerden dolayý olabilir.
          1.Kodu copy paste yaptýysanýz file = open kýsmýný kendi Pc nize göre konumlandýrýn
          2.Girdiðiniz dosya adý veya uzantýsý hatalýdýr Örn(dosyaisminde ' ? 'iþareti olmaz.)""")