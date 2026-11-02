# Enunciado:
# Crie um programa que peça a idade de uma pessoa e pergunte
# se ela está acompanhada por um responsável.
# Permita a entrada se a pessoa tiver 18 anos ou mais
# ou se estiver acompanhada por um responsável.
# Caso contrário, informe que a entrada não é permitida.

idade = int(input("Qual sua idade?: "))
acompanhado = input("Está acompanhado por um responsável? (sim/nao): ")

if acompanhado != "sim" and acompanhado != "nao":
    print("Resposta inválida! Digite sim ou nao.")
elif idade >= 18 or acompanhado == "sim":
    print("Entrada Permitida")
else:
    print("Entrada não Permitida")

# a primeira condição usa != "sim" and acompanhado != "nao", que significa "diferente de"
# Ela pergunta: a resposta é diferente de "sim" e diferente de "nao"? Se for, o programa mostra que a resposta é inválida. 