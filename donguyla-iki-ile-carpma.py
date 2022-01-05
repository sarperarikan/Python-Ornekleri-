#Bu programcıkta kullanıcıdan alınan veri her biri iki ile çarpılıp işlem yaptırılıyor ve sıfır girilirse işlemden çıkılıyor.
while True:
    sayi = int(input("Sayıları girin"))
    sayilar = sayi * 2
    if sayilar  == 0:
        print("Uygulamadan çıktınız")
        input()
        break
        
    print(str(sayi)+" "+"sayısının ikiyle çarpımı{}".format(sayilar))
    input()

        
