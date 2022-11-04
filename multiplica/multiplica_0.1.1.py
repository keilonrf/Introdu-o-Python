"""
Programa soma
Requisito: Este progrma pega dois números digitados pelo usuario e calcula
o seu produto, colocando o resultado na tela.
Autor: Keilon Reckers Ferreira
Data: 26/10/2022
Versão: 0.1.2
Inclusão de funcionalidade: informar ao usuário para que serve o programa.
"""

# Entrada

print("Este programa informa o produto de dois números informados pelo usuário.")

numero1 = int(input("\nDigite o primeiro numero: "))
numero2 = int(input("\nDigite o segundo numero: "))

# Processamento

produto = numero1 * numero2


# Saída

print(f"O produto dos numeros {numero1} e {numero2} é igual a {produto}.")
