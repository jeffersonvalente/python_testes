#!/usr/bin/env 
# -*- coding: UTF-8 -*-

#mostrando itens da lista
lista = [
	"linux","devops","python"
]

for i in lista:
	print (i)

#mostrando posições
lista2 = [
        "linux", "devops","python"
]

for num,item in enumerate(lista):
	print ("%s está na posição %s"%(item,num))
