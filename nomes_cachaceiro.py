#variaveis de saida
nome = ""
sobrenome = ""

mes = 1
dia =1

#usando if
if mes ==1:
	nome = "betinho"
elif mes == 2:
	nome = "Xexeu"
elif mes == 3:
	nome = "Ze"

if dia == 1:
	sobrenome = "Furico"
elif dia == 2:
	sobrenome = "da Viola"
elif dia == 3:
	sobrenome =  "rosca solta"

#Usando listas
lista_nomes = ["betinho", "xexeu", "ze"]
lista_sobrenomes = ["Furico", "da viola", "rosca solta"]

nome = lista_nomes[mes - 1]
sobrenome = lista_sobrenomes[dia - 1]

#usando dicionario
dicionario_nomes = {1: "betinho", 2: "xexeu", 3: "ze"}
dicionario_sobrenomes = {1: "Furicop", 2: "da Viola", 3: "rosca solca"}
nome = dicionario_nomes[mes]
sobrenome = dicionario_sobrenomes[dia]

#usando funçoes
def gerador_if(mes,dia):
#	global nome
#	global sobrenome
	nome =""
	sobrenome=""
	if mes ==1:
	        nome = "betinho"
	elif mes == 2:
	        nome = "Xexeu"
	elif mes == 3:
	        nome = "Ze"

	if dia == 1:
	        sobrenome = "Furico"
	elif dia == 2:
	        sobrenome = "da Viola"
	elif dia == 3:
	        sobrenome =  "rosca solta"
	return nome, sobrenome

#type(gerador_if(1,1))
#tuple

#usando zip


# Resultado

nome, sobrenome= gerador_if(mes,dia)
print("Seu nome de cachaceiro eh {} {}".format(nome, sobrenome))
