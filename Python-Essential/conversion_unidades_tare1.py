# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:44:33 2022

@author: Ol!ver
"""
l=float(input("ingrese valor en L/100KM "))
km=float(input("ingrese valor en MPG "))

def l100kmtompg(l):
    l1=(378541.1784)/(l*1609.344)
    print("El resultado es ",l1," MPG")
    
def mpgtol100km(km):
    
    km1=(378541.1784)/(km*1609.344)
    print("El resultado es ",km1," L/100KM")
    
resultado1=l100kmtompg(l)
resultado2=mpgtol100km(km)

    