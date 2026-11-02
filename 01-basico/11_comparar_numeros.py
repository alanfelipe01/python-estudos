# Enunciado:
# Peça dois números ao usuário.
# Informe se o primeiro número é maior, menor ou igual ao segundo.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}.")
elif n1 == n2:
    print(f"{n1} é igual a {n2}.")
else:
    print(f"{n1} é menor que {n2}.")