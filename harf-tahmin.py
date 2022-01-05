#Bu uygulama kelime değişkeni içerisindeki karakter dizilerini baz alarak kullanıcının girdiği karakter dizileriyle karşılaştırma yapan bir algoritmayı içermektedir.
kelime = "yazıcı"
yanit = ""
while True:
    giris = input("Tahmininizi giriniz")

    if giris == "q":
        print("Uygulamadan çıkılıyor")
        input()
        break
    if giris in kelime:
        yanit += giris
        print("Doğru tahmin {}".format(giris))
    else:
        print("Tekrar deneyiniz")
        input()

#Yanıt değişkenindeki karakter sayısı ile kelime değişkenindeki karakter sayısı eşitse çalışacak kodlar kelime değişkenindeki sonucu ekrana basacaktır.  
    if len(yanit) == len(kelime):
        print("{} kelimesindeki tüm harfleri bildiniz".format(kelime))
        input()
        break


