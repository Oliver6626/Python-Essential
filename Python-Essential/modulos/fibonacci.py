# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:40:11 2022

@author: Ol!ver
"""

def fibo (n):
        a,b =0,1
        while a<=n:
            print(a, end=' ')
            """ c=a+b
            a=b
            b=c """
            
            a,b = b, a+b

#fibo(8)