#!/usr/bin/env
#-*- coding: UTF-8 -*-

produtos = []

def cadastrarProduto(produto):
	global produtos
	produtos.append(produto)

def listarProdutos():
	global produtos
	for p in produtos:
		print (p)

produto = ""
while produto != "sair":
	produto = input("digite o nome do produto: ")
	cadastrarProduto(produto)
	print ("produtos cadastrados com sucesso")
	listarProdutos()
