#!/usr/bin/env 
# -*- coding: UTF-8 -*-

carrinho = []

produto1 = {"nome":"tenis","valor":21.31}
produto2 = {"nome":"meia","valor":31.32}
produto3 = {"nome":"camiseta","valor":22.31}
produto4 = {"nome":"bermuda","valor":41.31}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)

def totalCarrinho(carrinho):
	return sum(produto["valor"] for produto in carrinho)

def cupomDesconto(cupom=""):
	if cupom == "gratis":
		return 0.70
	else:
		return 1

print ("o total da sua compra é de: ", (totalCarrinho(carrinho)*cupomDesconto()))
print ("usando o cupom gratis seu valor será de: ", totalCarrinho(carrinho)*cupomDesconto("gratis"),"30% menos")
