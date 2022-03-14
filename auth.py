import pandas as pd

class cred():
    
    def __init__(self,email,password,name):
        self.email = email
        self.password = password
        self.name = name
        self.saved_df = pd.read_csv("cred.txt")
    
    def register(reg):
        auth_df=pd.DataFrame(columns=['Email','Password','Name'])  
        pd.concat([reg.saved_df,auth_df.append({'Email':email,'Password':password,'Name':name})],ignore_index=True).to_csv("cred.txt",index=False)
        cred.login()

    def login(log):
        index = -1
        for checkemail in log.saved_df['Email']:
            index += 1
            if log.email == checkemail:
                if password == log.saved_df['Password'][index]:
                    app.cbot(email,name)
                else:
                    keypress = input("Wrong Email or Password, Type 'L' to Login Again or 'R' to Register").upper()
                    if keypress == "L":
                        cred.login()
                    elif keypress == "R":
                        cred.register()
            else:
                keypress_note = input("Email Address Not Found, type 'L' to login or 'R' to Register").upper()
                if keypress_note == 'L':
                    cred.login()
                elif keypress_note =='R':
                    cred.register()




email = input("Enter Email: ")
password = input("Enter Password: ")
name = input("Enter Name: ")

cred(email,password,name).register()





            