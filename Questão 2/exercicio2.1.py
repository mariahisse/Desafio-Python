import numpy as np

# essa é uma resolução simplificada utilizando a biblioteca numpy 

# vetor com os valores
vet = np.array([(3**i + 7*np.math.factorial(i)) if (i % 2 == 0) else (2**i + 4*np.math.log(i)) for i in range(0,10)])

# procura a posição do elemento de maior valor
print("A posição do maior elemento é", np.where(vet == max(vet))[0][0])

# calcula a média dos valores do vetor
# arredondando para duas casas decimais
print("A média é", round(np.mean(vet),2))