import random
bilgi = """
Bil bakalım aklımdaki sayı ne?
"""
hak = 3
tutulan_sayi = random.randint(1,4)
while   True :
    giris = int(input("Tahmininizi giriniz."))
    if giris == tutulan_sayi:
        print("Tebrikler sayıyı bildiniz")
        hak += 1
        input()
    else:
        print(bilgi)
        hak -= 1
        print("Kalan hakkınız: {}".format(hak))

    if hak == 0:
        print("Haklarınız bitti, oyunu kaybettiniz")
        input()        
        break
        
