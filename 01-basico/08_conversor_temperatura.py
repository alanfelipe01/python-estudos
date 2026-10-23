# Enunciado:
# Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
# Use a fórmula: Fahrenheit = Celsius * 9 / 5 + 32.
# Ao final, mostre a temperatura convertida com duas casas decimais.

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
