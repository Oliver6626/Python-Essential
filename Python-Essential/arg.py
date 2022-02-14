# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:02:33 2022

@author: Ol!ver
"""

def suma (*args):
    print("\n tipo de datos del argumento",
      type(args))
    
    sum= 0
    for n in args:
        sum+=n
    print('suma:',sum)
    
    suma(3)
    suma(3,5)
    suma(4,5,6,7)
    suma(4,5,6,7,8)