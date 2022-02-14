# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 19:20:40 2022

@author: Ol!ver
"""

acl=int(input("Ingrese el numero"))

if acl>=1 and acl <=99:
    print("La ACL es estandar")
elif acl>=100 and acl <=199:
    print("La ACL es extendida")
else:
    print("El dato ingresado no es de un ACL")
    