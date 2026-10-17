# Enunciado:
# Peça ao usuário dois números diferentes de zero.
# Mostre o resultado das seguintes operações entre eles:
# adição (+), subtração (-), multiplicação (*), divisão (/),
# divisão inteira (//), resto da divisão (%) e potência (**).

numero1 = int(input("DIGITE O PRIMEIRO NUMERO: "))
numero2 = int(input("DIGITE O SEGUNDO NUMERO: "))

if numero2 == 0:
    print("O segundo numero não pode ser zero")
else:

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2
    divinteira = numero1 // numero2
    restodadiv = numero1 % numero2
    potencia = numero1 ** numero2

    print(f"A soma dos numeros é: {soma}") 
    print(f"A subtração dos numeros é: {subtracao}")
    print(f"A multiplicação dos numeros é: {multiplicacao}")
    print(f"A divisão dos numeros é: {divisao}")
    print(f"A divisão inteira é {divinteira}")
    print(f"O resto da divisão é {restodadiv}")
    print(f"A potência dos numeros é: {potencia}")
