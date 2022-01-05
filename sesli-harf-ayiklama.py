while True:
    yanit = input("Yanıtınızı girin")
    soru = "sarper"
    for s in yanit:
        if s in soru:
            print(s)
        elif s not in soru:
            print("\a")
             
            
    if yanit  == "q":
        print("Uygulamadan çıkılıyor")
        input()
        break
    input()