


import random
import string
from math import*
import sys
import os


def randomString():
    return''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)])

def PasswordWriting():
        
        password_file = open("Passwords.txt","r+")
        Platform = input("Enter The Platform:")
        password_generated= randomString()
        count = password_file.readlines()
        num_count = len(count)
        num_count = num_count
        num_count = ceil(num_count) 
        num_count = str (num_count)
           

        password_file.writelines(["\n"+num_count+"| " + Platform ," => "+password_generated])
       
        print("////////////////////////////////////////////")
        print("//////""Your password will be:"+password_generated+"///////")
        print("///////////////////////////////////////////")
        password_file.close() 
       


def Main (PasswordWriting):
    Run =True
    while Run == True:
        Run = input("Do want to enter password yes or no :")
        if Run == "yes":
            Run = True
            if os.path.exists('Passwords.txt') != True:
                Createfile =open("Passwords.txt","w+")
                Createfile.close()
                PasswordWriting()
                
            else:
                PasswordWriting()

        else:
            Run =False
            sys.exit()  
        
    
       
         
            
Main(PasswordWriting) 
        
    
   