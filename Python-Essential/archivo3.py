# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:39:32 2022

@author: Ol!ver
"""

lista=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip("\n")#elimina uno o varios caracteres
    lista.append(item)
    print(item)
file.close()
print(lista)