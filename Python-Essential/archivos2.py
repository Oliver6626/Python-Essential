# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:38:03 2022

@author: Ol!ver
"""

file=open("devices.txt","r")
for item in file:
    item=item.strip("\n")#elimina uno o varios caracteres
    print(item)
file.close()
