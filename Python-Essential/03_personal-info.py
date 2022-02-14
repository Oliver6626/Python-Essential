# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 20:46:44 2022

@author: Ol!ver
"""
espacio=" "
nombre=input("Ingrese su Nombre")
apellido=input("Ingrese su Apellido")
ubicacion=input("Ingrese su Ubicación")
edad=int(input("Ingrese su Edad"))


print("Hola!",nombre,espacio,apellido,espacio,
      "Te encuentras en",espacio,ubicacion,espacio,
      "y tienes",espacio,edad,espacio,"años")

if edad>=1 and edad<= 18:
    print("eres Menor de Edad")
elif edad>=18 and edad<=30:
    print("eres Adulto Joven")
elif edad>=30 and edad<=55:
    print("eres Adulto")
else:
    print("eres Tercera Edad")