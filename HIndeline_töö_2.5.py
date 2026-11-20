try:
    print("1 - Arvu kontroll")
    print("2 - Kehamassiindeks")
    print("3 - Ostu allahindlus")
    programm=int(input("Vali programm: "))
    if programm==1:
        try:
            print("Arvu kontroll") #' -> "
            arv=int(input("Sisesta täisarv => ")) ##lisasin int()
            if arv>0: #lisasin :
                print("Arv on positiivne")
            elif arv==0: # = -> ==
                print("Arv on null")
            else:
                print("Arv on negatiivne") #lisasin tab
            if arv%2==0:
                print("Arv on paarisarv")
            else:
                print("Arv on paaritu")
            if arv%3==0: 
                print("Arv jagub 3-ga")
            else:
                print("arv ei jaguv 3-ga")
            print("Kehamassiindeks")
        except ValueError:
            print("sisestage täisarv")
    elif programm==2:
        try:
            mass=float(input("Sisesta kaal (kg) => "))
            pikkus=float(input("Sisesta pikkus (m) => ")) #lisasin )
            if pikkus<0 or mass<0:
                print("see ei sobib")
            else:
                kmi=mass/pikkus*2
                print("KMI:", round(kmi,1))
                if kmi<18.5:
                    print("Alakaal")
                elif kmi>=18.5:
                    print("Normaalkaal")
                elif kmi>=25: 
                    print("Ülekaal")
                elif kmi>=30: #lisasin :
                    print("Rasvumine")
                print()
                print("Ostu allahindlus")
        except ValueError:
            print("sisestage arv")
        except ZeroDivisionError:
            print("nulliga jagada ei saa")

    elif programm==3:
        try:
            summa=float(input("Sisesta ostusumma => "))
            if summa<=0: #"=<" -> ">="
                print("Vigane summa")
            elif summa>500:
                print("Allahindlus 10%, maksta:", round(summa*0.9,2)) #kohade vahetus 5% ridast 10%ridasse 
            elif summa>100 and summa<=500:
                print("Allahindlus 5%, maksta:", round(summa*0.95,2))
            else: #lisasin :
                print("Allahindlust pole, maksta:", summa) #lisasin )
        except ValueError:
            print("sisestage õige summa")
    else:
        print("Vigane valik,  valida 1,2 või 3")
except ValueError:
    print("palun sisesta arv, valida 1,2 või 3") ##lisasin try: ja except:


