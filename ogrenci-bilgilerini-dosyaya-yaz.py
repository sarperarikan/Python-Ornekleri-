#Aşağıdaki uygulama ile öğrenci not bilgileri bir txt dosyasında saklanmaktadır.
dosya = open("ogrenci_bilgileri.txt","a+")
#Open komutuyla dosya oluşturuyor ve a+ yazma kipiyle öğrenci bilgilerini teker teker ve aynı dosya içerisinde yazmamızı sağlamış oluyoruz. Buradaki a+ aynı dosya içine yazma kipi olarak çalışılmasını sağlıyor.
while True:
    giris = input("Uygulamayı başlatmak için enter tuşuna çıkmak için q tuşuna basınız")
    # Yukarıdaki if yapısıyla döngüyü kırmak için koşul tanımlıyoruz ve burada break ifadesiyle döngüyü kırıyoruz.
    if giris == "q":
        print("Uygulamadan çıkmak için enter tuşuna basın")
        input()
        break
        dosya.close()

    ogrenci_ad_soyad = input("Öğrenci adını ve soyadını giriniz")
    ara_sinav = int(input("Ara sınav notunu giriniz"))
    donem_sonu_sinav = int(input("Dönem sonu sınav notunu giriniz"))
    print("{} adlı öğrencinin ara sınav notu: {} dönem sonu sınav notu : {}".format(ogrenci_ad_soyad,ara_sinav,donem_sonu_sinav),file=dosya,end="\n",flush=dosya)
    #Yukarıdaki print içerisinde file parametresini kullanarak ekrana değilde üstte tanımladığımız dosya içerisine çıktı alıyoruz. Bununla birlikte end parametresiyle birlikte eklediğimiz \n ifadesiyle bir alt satıra geçilmesini sağlıyoruz.
    print("Öğrenci bilgileri kaydedildi")
    