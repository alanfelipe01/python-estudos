# Enunciado:
# Crie um programa que peça uma nota ao usuário.
# Verifique se a nota está entre 0 e 10, incluindo os dois valores.
# Mostre uma mensagem informando se a nota é válida ou inválida.

nota = float(input("Digite a nota: "))

if nota >= 0 and nota <= 10:
    print("Nota Válida!")
else:
    print("Nota Inválida!")
