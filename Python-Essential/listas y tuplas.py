# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 19:05:39 2022

@author: Ol!ver
"""
lista1=["Python", 58,True,25.8]
print(type(lista1))
print(len(lista1))
print(lista1)
print(lista1[0])
print(lista1[1])
tupla1=("Python", 58,True,25.8)
print(tupla1)
print(tupla1[0])
print(tupla1[1])
print(tupla1[2])
print(tupla1[3])
print(tupla1[-1])
print(tupla1[-2])
print(tupla1[-3])

lista1[0]= "Hola Python desde cero"# las listas son mutables
#tupla1[0]= "Hola Python desde cero"# las tuplas son inmutables

del lista1[3]
del tupla1[3]