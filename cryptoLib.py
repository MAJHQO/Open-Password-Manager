import hashlib as hash,string,flet
from random import randint

def createMPassword(self):

    passLen=randint(10,25)

    mPassword=""

    lettersPassword_arr=list(string.ascii_letters)
    numberPassword_arr=list(string.digits)
    symbolPassword_arr=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    for i in range(1,passLen+1):

        if (i%2==0):

            mPassword+=lettersPassword_arr[randint(0, len(lettersPassword_arr))]
        

        elif (i%2==1):

            if(i%3==1):

                mPassword+=numberPassword_arr[randint(0,len(numberPassword_arr))]

            else:

                mPassword+=symbolPassword_arr[randint(0,len(symbolPassword_arr))]

    