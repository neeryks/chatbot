from ipaddress import collapse_addresses
from pydoc import splitdoc
import pandas as pd


## MAking Models For Chatbot #
def regis():
    emai = input("Enter Email : ")
    passw = input("Enter Password : ")
    nam = input("Enter Full Name : ")
    new = {'email':[emai],'password':[passw],'name':[nam]}
    df = pd.DataFrame(new)
    df1 = pd.read_csv("cred.txt")
    f = pd.concat([df1,df],ignore_index=True)
    f.to_csv('cred.txt')
    
def cbot():
    print("Hi I am Cbot. Please Enter your Email Id to login or type 'Guest' to continue as it is : ")
    b = input().upper()
    if b == "GUEST":
        print('Hello I am Cbot How Can i Help You ?')
    
    else:
        cdata = pd.read_csv("cred.txt")
        count = 0
        for data in cdata['email']:
            count = count + 1
            while 6>5:
                if b == data.upper():
                    passchk = input("Enter Password : ")
                    if passchk == cdata['password'][count-1]:
                        print("Login Sucessful")
                    else:
                        print("Wrong password , Please Renter")
                    print("Hi {}. How Can I Help You ?".format(cdata['name'][count-1]))
                    break

                else:
                    print("No User Found, Register Now !")
                    regis()
                    break



cbot()








            