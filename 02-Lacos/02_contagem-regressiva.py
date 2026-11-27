# Enunciado:
# Leia um número inteiro positivo e use um laço while para mostrar
# a contagem regressiva desse número até zero, incluindo o zero.
#
# Exemplo: se o usuário digitar 5, mostre 5, 4, 3, 2, 1 e 0.
#
# Raciocínio:

numero = int(input("Digite um numero:"))

while numero >= 0:
    print(numero)
    numero = numero - 1
