print(" <<<<<<<<<<<<<<<------------------------------------------------------------------>>>>>>>>>>>>>>>")
print("\t\t*******    Welcome to Medical Diagnosis Expert System     *******")
print(" <<<<<<<<<<<<<<<------------------------------------------------------------------>>>>>>>>>>>>>>>")
name=input("\nenter your name :\n")
print("Choose from following system:")
choose=int(input(''' 
1.body paining
2.cold
3.cough
4.fever\n'''))


def pain(tell):
    if(tell==1):
        print("\nMEDICINE : you can take following medicenes:\n\t1. Paracitamol  -->  1 rs \n\t2. Dolo  -->  2 rs \n\t3. Crocin pain relief  --> 4.13 rs")
        print("\nHome Tritment : \n\t1. use balm \n\t2. Do 'yoga'\n3.Use Bhapara Capsul\n")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2. Do Meditation")
        return thankyou()
    if(tell==2):
        print("\nMEDICINE :  you can take following medicenes:\n\t1. Buscogast plus  -->  3.3 rs \n\t2. spasmonil  -->  3 rs \n\t3. Cycloform  --> 3 rs")
        print("\nHome Tritment : \n\t1. eat simple food \n\t2. drink hot water\n")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2.Do not eat steet food")
        return thankyou()
        
    if(tell==3):
        print("\nMEDICINE :  you can take following medicenes:\n\t1. Naproxen  -->  2 rs \n\t2. Distamol  -->  4 rs \n\t3. CROCIN pain relief  --> 4.13 rs")
        print("\nHome Tritment : \n\t1. use balm or you can use any Ointment \n\t 2. drink hot water\n")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1. Take rest\n\t2. Do 'yoga'")
        return thankyou()
    
        
def cold(tell1):
    if(tell1==1):
        print("\nMEDICINES : you can take following medicenes:\n\t1. Cronic flu & cold  -->  3.8 rs \n\t2.Vicks Acction 500   --> 5.2 rs \n\t3.Codral cold & flu  -->  7.2 rs\n")
        print("\nSYRUPS :  you can take following Syrup:\n\t1. Sinarest(60 ml)  -->  81.42 rs\n\t2. Relent(60 ml) -->  92 rs ")
        print("\nHome Tritment : \n\t1.use balm \n\t2.drink hot water\n\t3. Use inhelar")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2.Don't Eat/Drink cold items")
        return thankyou()
    if(tell1==2):
        print("\nMEDICINES :  you can take following medicenes:\n\t1.Cronic flu & cold  -->  3.8 rs\n\t2.Codral cold & flu  -->  7.2 rs \n\t3.FLU 150mg  -->  12.17 rs\n")
        print("\nSYRUPS :  you can take following Syrup:\n\t1.Flucold(60 ml)   -->  46.75 rs\n\t2. Ascorali Flu(60 ml)  -->  80.50 rs")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2.Keep Hygine\n\t3.Cover Your Mouth And Nose\n\t4Eat Healthy")
        print("\nHome Tritment : \n1.Drink Kadha(Termaric,Tulsi,Ginger,etc.)\n2.use balm \n")
        return thankyou()
    if(tell1==3):
        print("\nMEDICINES :  you can take following medicenes:\n\t1. Cheston Cold  -->  4.2 rs \n\t2. Nam Cold  -->  5.5 rs \n\t3.Codral cold & flu  -->  7.2 rs\n\t4.Cofsils  -->  3 rs")
        print("\nSYRUPS :  you can take following Syrup:\n\t1. Cheston Cold(60 ml)   -->  38.72 rs\n\t2. T Cold(80 ml)  -->  200 rs ")
        print("\nHome Tritment : \n\t1.Drink Kadha(Termaric,Tulsi,Ginger,etc.) \n\t2.Use Honey\n\t3. Use inhelar")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2.Keep Hygine\n\t3.Avoid Cold things(IceCreams,Cold Drinks)\n")
        return thankyou()
    if(tell1==4):
        print("\nMEDICINES :  you can take following medicenes:\n\t1.Cheston Cold Total   -->  8 rs \n\t2. Mucinex  -->  18.7 rs \n\t3.Cofsils  -->  3 rs")
        print("\nSYRUPS :  you can take following Syrup:\n\t1.Triz Cold  -->   41.6 rs\n\t2. Robitussin   -->  1270 rs ")
        print("\nHome Tritment : \n\t1.Drink Kadha(Termaric,Tulsi,Ginger,etc.)\n\t2. Use inhelar\n\t3.Use Bhapara Capsul")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n")
        return thankyou()

def cough(tell2):
     if(tell2==1):
        print("\nSYRUPS :  you can take following Syrup:\n\t1. Zandu Cough Syrup  -->  5 rs \n\t2. Benadryl(60 ml)  -->  109.65 rs\n\t3. Robitussin(100 ml) -->  419 rs ")
        print("\nHome Tritment : \n\t1.use balm \n\t2.drink hot water\n\t3. Drink Masala Tea Chai\n\t4. Gargle with salt water")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2.Don't Eat/Drink cold items")
        return thankyou()
     if(tell2==2):
        print("\nSYRUPS :  you can take following Syrup:\n\t1. Benadryl(60 ml)  -->  109.65  rs\n\t2. Koflate-Ex -->  90.50 rs \n\t Cofsils(60ml)  -->  64 rs")
        print("\nHome Tritment : \n1.Drink Kadha(Termaric,Tulsi,Ginger,etc.)\n2.use balm \n")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2.Keep Hygine\n3.Cover Your Mouth And Nose\n4. Don't Eat/Drink cold items")
       
        return thankyou()

def fever(tell3):
    if(tell3==1):
        print("\nMEDICINES : you can take following medicenes:\n\t1. Paracitamol  -->  1 rs\n\t2. Dollo-650  -->  3.8 rs \n\t3. Eciclo-p  --> 5 rs")
        print("\nHome Tritment : \n\t1.use balm \n\t2.drink hot water\n\t3. Use inhelar")
        print("\nADVICE : firstly,take care.\n Following Things you can do : \n\t1.Take rest\n\t2.Don't Eat/Drink cold items")
        return thankyou()

def logic(choose):
    print("lets go")
    if(choose == 1):
        print("\nyour  body paining ,right")
        print("please tell me brif:")
        tell=int(input("\nwhich pain you have \n1. head ache\n2. stomach pain\n3. body pain \n"))
        return pain(tell)
    if(choose==2):
        print("you have cold ,right")
        print("please tell me brif:")
        tell1=int(input("which type of cold you have \n1. Common cold\n2. Flu\n3. Trachea cold\n4. Chest cold\n"))
        return cold(tell1)
    if(choose==3):
        print("you have cough ,right")
        print("please tell me brif:")
        tell2=int(input("which type of cough you have \n1. Dry cough\n2. Wet cough\n"))
        return cough(tell2)
    if(choose==4):
        print("you have fever ,right")
        print("please tell me brif:")
        tell3=int(input("which type of fever you have \n1. Normal fever\n"))
        return fever(tell3)
        
    
def thankyou():
    print(" <<<<<<<<<<<<<<<------------------------------------------------------------------>>>>>>>>>>>>>>>")
    print("\t\t\t*******  THANK YOU FOR VISITING TO SYSTEM  *******")
    print(" <<<<<<<<<<<<<<<------------------------------------------------------------------>>>>>>>>>>>>>>>")

logic (choose)


