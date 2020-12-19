i = 1
dic = {}

# loop para ler a nota de cada aluno
while (i <= 5):
	# testa se a nota é realmente um número
	# caso não seja, será pedido novamente que entre com a nota
	try:
		print("Aluno", i)

		# converte a nota para float
		nota = float(input("Digite a nota: "))

		print("------------------------")

		# adiciona a nota ao dicionário
		# poderia pedir também para digitar o nome do aluno e essa seria a chave do dicionário
		dic['Aluno ' + str(i)] = nota

		i += 1
	except:
		print("Valor inválido!\n")

# mostra a maior nota e qual foi o aluno
print("A maior nota é do", max(dic, key=dic.get), "que tirou", dic[max(dic, key=dic.get)])

