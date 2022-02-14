# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:11:54 2022

@author: Ol!ver
"""

try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir para cero")
    
except ValueError:
    print("Debes ingresar un valor entero")
    
except:
    print("Hubo un error!")
    
print("Fin..")