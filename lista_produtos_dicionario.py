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

print ("seu carrinho possui",len(carrinho),"itens")
total = 0
for c in carrinho:
	total += c["valor"]
print ("O valor total é de:", total)
