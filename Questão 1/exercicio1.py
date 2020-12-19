# vamos inicializar a variável contador com zero
cont = 0

# estrutura de repetição para testar o intervalo
# não testa o 5000000 (não é necessário)
for i in range(1, 5000000):
	# condição para um número, deve ser par e múltiplo de 49 e 37
	# caso aconteça soma um ao contador
	if ((i % 2 == 0) and (i % 49 == 0) and (i % 37 == 0)):
		cont += 1

print("Existem", cont, "números entre 1 e 5000000!")
