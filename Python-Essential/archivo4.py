# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:51:23 2022

@author: Ol!ver
"""

file=open("devices.txt","a")


newitem=" "
while True :
    newitem=input("ingrese dato: ")
    if newitem == "salir":
        print("Todo bien")
        break
    file.write(newitem + "\n")
print(file)
file.close()