#!/usr/bin/env 
# -*- coding: UTF-8 -*-

n= int(input("Qual o termo? "))
ultimo_numero = 1
penultimo_numero = 1

if (n==1) or (n==2):
	print ("1")
else:
	for count in range(2,n):
		termo = ultimo_numero + penultimo_numero
		penultimo_numero = ultimo_numero
		ultimo_numero = termo
		count += 1
	print ("O termo é: %s" %(termo))
