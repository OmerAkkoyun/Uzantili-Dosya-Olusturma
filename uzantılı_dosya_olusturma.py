import time
print("""
***********************
Dosya Olu�turma Program�
***********************
1.�lk �nce dosya ismi giriniz
2.Dosya uzant�s�n� girin
3.Sonra olu�turulacak yeri se�in
�rne�in:
masa�st�    D:        belgeler

""")


isim=input("Olu�turulacak Dosyan�n ismini girin =")
uzanti=input("Dosya uzant�s�  =")
yol=(input("Nereye Olu�tululsun ="))

isimuzanti=isim+"."+uzanti
try:
    if yol=="masa�st�":
        print("Dosya olu�turuluyor..")
        time.sleep(2)
        print("Dosya olu�turuldu..")
        file =open("C:/Users/Omer/Desktop/"+isimuzanti,"a")


    elif yol=="D:":
        print("Dosya olu�turuluyor..")
        time.sleep(2)
        print("Dosya olu�turuldu..")
        file = open("D:/" + isimuzanti, "a")

    elif yol=="belgeler":
        print("Dosya olu�turuluyor..")
        time.sleep(2)
        print("Dosya olu�turuldu..")
        file = open("C:/Users/Omer/Documents/"+isimuzanti,"a")


    else:
        print("""       Hata ald�n�z !
        Bu hatan�n  sebepleri a�a��dakilerden dolay� olabilir.
        1.Kodu copy paste yapt�ysan�z file = open k�sm�n� kendi Pc nize g�re konumland�r�n
        2.Girdi�iniz dosya ad� veya uzant�s� hatal�d�r �rn(dosyaisminde ' ? 'i�areti olmaz.)""")
except:
    print("""Hata ald�n�z except;
          Bunu sebepleri a�a��dakilerden dolay� olabilir.
          1.Kodu copy paste yapt�ysan�z file = open k�sm�n� kendi Pc nize g�re konumland�r�n
          2.Girdi�iniz dosya ad� veya uzant�s� hatal�d�r �rn(dosyaisminde ' ? 'i�areti olmaz.)""")