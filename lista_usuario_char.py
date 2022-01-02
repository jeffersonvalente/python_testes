#!/usr/bin/env 
# -*- coding: UTF-8 -*-

usuarios = []
nome = ""

while nome != "sair":
	nome = input("Digite o nome \n")
	if nome == "sair":
		print ("Saindo do chat")
		break
	if not nome in usuarios:
		print (nome+" entrou no chat \n")
		usuarios.append(nome)
	for u in usuarios:
		print (u+" está online \n")

