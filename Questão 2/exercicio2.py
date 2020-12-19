import math

# função para calcular o fatorial
def fatorial(x):
	fat = 1
	if x == 0:
		return 1
	else:
		for i in range(x, 1, -1):
			fat *= i
		return fat

# adiciona os elementos ao vetor
vet = []
for i in range(0, 10):
	if (i % 2 == 0):
		vet.append(3**i + 7*(fatorial(i)))
	else:
		vet.append(2**i + 4*math.log(i))

# procura a posição do maior elemento do vetor
maior = vet[0]
pos = 0
for i in range(1, len(vet)):
	if vet[i] > maior:
		maior = vet[i]
		pos = i
print("A posição do maior elemento é", pos)

# calcula a média dos elementos do vetor
# arredondando para duas casas decimais
soma = 0
for i in vet:
	soma += i
media = round(soma/len(vet), 2)
print("A média é", media)
