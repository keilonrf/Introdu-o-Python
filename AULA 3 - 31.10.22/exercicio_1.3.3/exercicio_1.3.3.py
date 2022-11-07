"""
Exercício 1.3.3
Requisito: Leia cinco numeros e imprima na tela o quadrado de cada um deles.
Autor: Keilon Reckers Ferreira
Data: 31/10/2022
Versão: 0.0.1
"""

# Entrada, processamento e saída

i = 0
while i < 5:
    numero = float(input("\n Digite o número: "))
    print(f"\nO quadrado deste número é {numero**2}.")
    i += 1


