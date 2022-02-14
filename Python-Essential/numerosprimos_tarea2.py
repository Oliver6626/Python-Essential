# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:43:43 2022

@author: Ol!ver
"""

def isprime(num):
    
    for n in range(2, num):
        if num % n == 0:
            #print("No es primo")
            return False
    else:
     return True


for i in range (2,20):
    if isprime(i):
         
        print(i,end=" ")       
        
num1=5
print(isprime(num1))
print (num1)
