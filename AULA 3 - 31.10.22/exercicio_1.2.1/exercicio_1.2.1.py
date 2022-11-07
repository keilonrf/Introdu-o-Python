"""
Exercício 1.2.1
Requisito: leia um numero e imprima na tela o seu dobro se ele for menor do que
10. Se o numero for de 10 ate 20, imprima a sua metade. Em qualquer outro caso,
imprima na tela que o numero n˜ao e valido.
Autor: Keilon Reckers Ferreira
Data: 31/10/2022
Versão: 0.0.1
"""

# Etrada

numero = float(input("\nDigite um numero: "))

            
# Processamento


if numero < 5:
    dobro = numero * 2
    frase = f"\nO dobro do numero {numero} é {dobro} e é menor que 10."

elif numero > 10:
    metade = numero / 2
    frase = f"\nO numero {numero} fica entre 10 e 20 e a sua metade é igual a {metade}."

else:
    frase = f"\nO numero {numero} não é valido."
               

#Saída

print(frase)
