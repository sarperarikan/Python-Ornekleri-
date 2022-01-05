yasaklilar = "1234567890"
metin = input("Metin girişi")
for karakter in metin:
    if karakter in yasaklilar:
        print("Sayılar girilmez")
        input()
    else:
        print(metin)
        input()        
        break
        