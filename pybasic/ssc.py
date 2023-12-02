
Bangla1 = 45
Bangla2 = 90
English1 = 85
English2 = 98
Highermath = 71
Biology = 82
Physics = 38
Chemistry = 28

if(Bangla1<0 or Bangla2<0 or 100<Bangla1 or 100<Bangla2):
    print("Error")
else:
    Bangla = Bangla1 + Bangla2
if(Bangla>=160 and Bangla<=200):
    Bangla = 5
    print("Bangla A+")
elif(Bangla>=140 and Bangla<159):
    Bangla = 4
    print("Bangla A")
elif(Bangla>=120 and Bangla<139):
    Bangla = 3.5
    print("Bangla A-")
elif(Bangla>100 and Bangla<119):
    Bangla = 3
    print("Bangla B")
elif(Bangla>80 and Bangla<99):
    Bangla = 2
    print("Bangla C")
elif(Bangla>66 and Bangla<79):
    Bangla = 1
    print("Bangla D")
elif(Bangla<66 and Bangla>0):
    Bangla = 0
    print("Bangla Fail")   


if(English1<0 or English2<0 or 100<English1 or 100<English2):
    print("Error")
else:
    English = English1 + English2 
    if(English>=180 and English<=200):
        English = 5
        print("Englsih A+")
    elif(English>=140 and English<=179):
        English = 4 
        print("English A")
    elif(English>=100 and English<=139):
        English = 3
        print("English A-")
    elif(English>=80 and English<=99):
        English = 2 
        print("English B")
    elif(English>=66 and English<=79):
        English = 1
        print("Englsih C")
    elif(English>=0 and English<66):
        English = 0
        print("Englsih Fail")


if(Highermath<0 or 100<Highermath):
    print("Error")
else:
    Highermath = Highermath + Highermath

if(Highermath>=80 and Highermath<=100):
    Highermath = 5
    print("Highermath A+")
elif(Highermath>=70 and Highermath<=79):
    Highermath = 4
    print("Highermath A")
elif(Highermath>=60 and Highermath<=69):
    Highermath = 3
    print("Highermath A-")
elif(Highermath>=50 and Highermath<=59):
    Highermath = 2
    print("Highermath B")
elif(Highermath>=40 and Highermath<=49):
    Highermath = 1
    print("Highermath C")
elif(Highermath>=33 and Highermath<=39):
    Highermath = 1
    print("Highermath D")
elif(Highermath>=0 and Highermath<=32):
    Highermath = 0
    print("Highermath Fail")


if(Biology<0 or 100<Biology):
    print("Error")
elif(Biology>=80 and Biology<=100):
    Biology = 5
    print("Biology A+")
elif(Biology>=70 and Biology<79):
    Biology = 4
    print("Biology A")
elif(Biology>=60 and Biology<=69):
    Biology = 3
    print("Biology A-")
elif(Biology>=50 and Biology<=59):
    Biology = 2
    print("Biology B")
elif(Biology>=40 and Biology<=49):
    Biology = 1
    print("Biology C")
elif(Biology>=33 and Biology<=39):
    Biology = 1
    print("Biology D")
elif(Biology<=32 and Biology>=0):
    Biology = 0
    print("Biology Fail")


if(Physics<0 or 100<Physics):
    print("Error")
elif(Physics>=80 and Physics<=100):
    Physics = 5
    print("Physics A+")
elif(Physics>=70 and Physics<=79):
    Physics = 4 
    print("Physics A")
elif(Physics>=60 and Physics<=69):
    Physics = 3 
    print("Physics A-")
elif(Physics>=50 and Physics<=59):
    Physics = 2 
    print("Physics B")
elif(Physics>=40 and Physics<=49):
    Physics = 1
    print("Physics C")
elif(Physics>=33 and Physics<=39):
    Physics = 1
    print("Physics D")
elif(Physics>=0 and Physics<=32):
    Physics = 0
    print("Physics Fail")

    
if(Chemistry<0 or 100<Chemistry):
    print(Error)
elif(Chemistry>=80 and Chemistry<=100):
    Chemistry = 5 
    print("Chemistry A+")
elif(Chemistry>=70 and Chemistry<=79):
    Chemistry = 4 
    print("Chemistry A")
elif(Chemistry>=60 and Chemistry<=69):
    Chemistry = 3 
    print("Chemistry A-")
elif(Chemistry>=50 and Chemistry<=59):
    Chemistry = 2
    print("Chemistry B")
elif(Chemistry>=40 and Chemistry<=49):
    Chemistry = 1
    print("Chemistry C")
elif(Chemistry>=33 and Chemistry<=39):
    Chemistry = 1 
    print("Chemistry D")
elif(Chemistry>=0 and Chemistry<=32):
    Chemistry = 0
    print("Chemistry Fail")
