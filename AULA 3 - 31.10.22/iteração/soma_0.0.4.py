"""
Programa soma
Requisito: Ler 4 números reais digitados pelo usuário, calcular a sua soma e
colocar o resultado na tela.
Autor: Keilon Reckers Ferreira
Data: 31/10/2022
Versão: 0.0.4
"""

# Entrada e processamento

i = 0 #contador
soma = 0

while i < 4: #laço de repetição (loop)
     numero = float(input("\nDigite a parcela: "))
     soma = soma + numero #acumulador
     i = i + 1

# Saída

print(f"A soma dos numeros digitados é igual a {soma}.")
