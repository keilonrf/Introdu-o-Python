"""
Programa maior que 5
Requisito: Leia um numero digitado pelo usuario e diga se ele e maior do que 5.
Autor: Keilon Reckers Ferreira
Data: 31/10/2022
Versão 0.0.1
"""

# Entrada

numero = float(input("\nDigite um numero real: "))
                     

# Processamento 

if numero > 5:
    frase = f"\nO numero {numero} e maior que 5."
                     
elif numero == 5:
    frase = f"\nO numero {numero} e igual a 5."

else:
    frase = f"\nO numero {numero} e menor que 5."

"""válido para mais de duas condições, para uma condição apenas if e para duas
condições usa-se if e else"""
    



# Saída

print(frase)
