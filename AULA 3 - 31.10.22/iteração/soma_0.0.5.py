"""
Programa soma
Requisito: Ler um conjunto números reais digitados pelo usuário, calcular a sua
soma e colocar o resultado na tela.
Autor: Keilon Reckers Ferreira
Data: 31/10/2022
Versão: 0.0.5
"""

# Entrada e processamento

soma = 0

while True:
     numero = float(input("\nDigite a parcela ou digite X para interromper: "))
     if numero == "X":
          break
     som = soma + float(numero)

# Saída

print(f"A soma dos numeros digitados é igual a {soma}.")
