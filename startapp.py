from pydoc import splitdoc
import pandas as pd


## MAking Models For Chatbot ##
dico = ['hello','bye']
def cbot():
    print("Hi I am Cbot. How Can i help You")
    b = input()
    #splitlist = list(b.split(" ")
    for d in dico:
        splitlist = list(b.split(" "))
        for sp in splitlist:
            if d == sp:
                print("Ok let me check that for you!")

cbot()







            