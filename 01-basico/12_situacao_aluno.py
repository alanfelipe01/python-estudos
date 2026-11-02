# Enunciado:
# Peça três notas e calcule a média do aluno.
# Se a média for menor que 5, informe que ele está reprovado.
# Se for de 5 até menos de 7, informe que está em recuperação.
# Se for igual ou maior que 7, informe que está aprovado.

av1 = float(input("Digite a nota da Avaliação 1: "))
av2 = float(input("Digite a nota da Avaliação 2: "))
av3 = float(input("Digite a nota da Avaliação 3: "))

media = (av1 + av2 + av3) / 3

print(f"Sua média é: {media}")

if media < 5:
    print("Você foi reprovado")
elif media < 7:
    print("Você está de recuperação")
else:
    print("Você foi aprovado")
