# Enunciado:
# Crie uma calculadora que peça dois números ao usuário.
# Peça também a operação desejada: +, -, * ou /.
# Realize a operação escolhida e mostre o resultado.
# Se a operação for inválida, informe ao usuário.
# Se ele tentar dividir por zero, informe que não é possível.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação desejada (+ , -, *, /): ")

if operacao == "+":
    print(f"A soma dos números é {n1 + n2}")
elif operacao == "-":
    print(f"A subtração dos números é {n1 - n2}")
elif operacao == "*":
    print(f"A multiplicação dos números é {n1 * n2}")
elif operacao == "/":
    if n2 == 0:
        print("Não é possivel dividir por zero")
    else:
        print(f"A divisão dos números é {n1 / n2}")
else:
    print("Operação Inválida!")
