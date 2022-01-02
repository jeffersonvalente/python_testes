#!/usr/bin/env 
# -*- coding: UTF-8 -*-

def calcular (*args):
	if len(args) == 1:
		print ("A área do quadrado é:",(args[0]*args[0]))
	elif len(args) == 2:
		print ("A área do retângulo é:",(args[0]*args[1]))
	elif len(args) == 3:
		print ("A área do paralelepipedo é:",(args[0]*args[1]*args[2]))

calcular(2)
calcular(4,2)
calcular(1,2,3)
