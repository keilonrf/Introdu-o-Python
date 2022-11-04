"""
Programa divide
Requisito: Este progrma pega dois números inteiros do teclado e calcula
a sua razão, colocando o resultado na tela.
Autor: Keilon Reckers Ferreira
Data: 26/10/2022
Versão: 0.0.1
"""

# Entrada

print("Este programa informa a razão de dois números inteiros do teclado.")

numero1 = int(input("\nDigite o primeiro numero: "))
numero2 = int(input("\nDigite o segundo numero: "))

# Processamento

razão = int(numero1 / numero2)


# Saída

print(f"A razão dos numeros {numero1} e {numero2} é igual a {razão}.")
