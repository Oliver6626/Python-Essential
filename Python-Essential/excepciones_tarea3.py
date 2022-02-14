# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:23:13 2022

@author: Ol!ver
"""

def readint(prompt,min,max):
    try:
        v=int(input("Ingrese "))
        print("el numero es ",v)
       
        if(v>=max or v<=min ):  
            raise Exception("El valor minimo no debe ser menor que -10 y no debe ser mayor que 10")
       
    except ValueError:
        print("Debes ingresar un valor entero")
        
   
                
   
        
v=readint("ingrese numero de -10 a 10: ",-10,10)

