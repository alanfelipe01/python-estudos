#Enunciado
#1.Peça um número inteiro ao usuário.
#2.Verifique se o número é par ou ímpar.
#3.Mostre o resultado na tela.

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print(f"O numero {numero} é par")
else:
    print(f"O numero {numero} é impar")

# Explicação:
# O operador % mostra o resto de uma divisão.
# Quando dividimos um número par por 2, o resto é 0.
# Quando dividimos um número ímpar por 2, o resto é diferente de 0.
#
# O if verifica se o resto da divisão do número por 2 é igual a 0.
# Se for verdadeiro, o programa informa que o número é par.
# Caso contrário, o else informa que o número é ímpar.
# == 0 pergunta se esse resto é igual a zero.