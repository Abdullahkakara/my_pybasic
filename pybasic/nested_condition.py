
# name = "Abdullah"
# phone = "01628962214"
# email = "mamunabdullah"
# if(len(name)==0 or len(phone)==0 or len(email)==0): #name=0;phone=1} name or phone
#     print("failed")
# else:
#     if(len(name)<5 or len(name)>8):
#         print("The number must be minimum 5 and 8")
#     elif(len(phone)!=11): 
#         print("The phone number size must be equal to 11")
#     elif(len(email)>=7):
#         print("The email name character must be 7 or above digit ")
#     else:
#         print("success")

name = "abdullah"
phone = "01628962214"
email ="mamun"
if(len(name))==0 or len(phone)==0 or len(email)==0:
    print("failed")
else:
    if(len(name)<5 or len(name)>8):
        print("The number must be minimum 5 and 8")
    elif(len(phone)!=11):
        print("The phone number must be 11 digit")
    elif(len(email)>7):
        print("The email name character must be 7 digit")
    else:
        print("success")




