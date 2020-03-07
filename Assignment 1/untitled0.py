# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:45:29 2020

@author: ahmed saeed
"""
import string
stream = list(string.ascii_lowercase)

#####################################
# Shift cipher
#####################################
def shift(Type):
    key = int(input("Enter the Key : "))
    if(Type == 'encrypt'):
        file1 = open("input.txt","r") 
        msg = file1.read()
        file1.close()  
        file2 = open("output.txt","w")
        for i in range(len(msg)):
            file2.write(stream[(stream.index(msg[i])+ key)%26])
        file2.close() 
    elif(Type == 'decrypt'):
        file2 = open("output.txt","r")
        y =file2.read()
        file2.close()
        i=0
        trueMsg=[]
        for i in range(len(y)):
            trueMsg.append( stream[(stream.index(y[i]) - key)%26])
        trueMsg = ''.join(trueMsg) # convert msg to string
        print("\nThe True Msg is : " + trueMsg)
#####################################

#####################################
# affine cipher
#####################################
def affine(Type):
    key1 = int(input("Enter the Key1 : "))
    key2 = int(input("Enter the Key2 : "))
    if(Type == 'encrypt'):
        file1 = open("input.txt","r") 
        msg = file1.read()
        file1.close()  
        file2 = open("output.txt","w")
        for i in range(len(msg)):
            file2.write(stream[((stream.index(msg[i]) * key1 )+ key2)%26])
        file2.close() 
    elif(Type == 'decrypt'):
        file2 = open("output.txt","r")
        y =file2.read()
        file2.close()
        i=0
        trueMsg=[]  
        for i in range(len(y)):
            trueMsg.append( stream[((stream.index(y[i]) * pow(key1, 24 , 26)) - key2)%26] )
        trueMsg = ''.join(trueMsg) # convert msg to string
        print("\nThe True Msg is : " + trueMsg)
#####################################

def main():
    TypeOfChiper = input("Enter The Chiper Type : ")
    if TypeOfChiper == 'shift': 
        Flag = input("decrypt or encrypt : ")
        if Flag == 'encrypt' :
            shift('encrypt')
        elif Flag == 'decrypt':
            shift('decrypt')
    elif TypeOfChiper == 'affine': 
        Flag = input("decrypt or encrypt : ")
        if Flag == 'encrypt' :
            affine('encrypt')
        elif Flag == 'decrypt':
            affine('decrypt')
      
if __name__== "__main__":
  main()