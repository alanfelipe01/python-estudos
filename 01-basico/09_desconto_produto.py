#Enunciado
#Peça o preço de um produto.
#Peça o percentual de desconto.
#Calcule o valor do desconto.
#Mostre o valor do desconto e o preço final.

preco_produto = float(input("Digite o preço do produto: "))
percentual = float(input("Qual o percentual de desconto?: "))

desconto = preco_produto * percentual / 100
preco_final = preco_produto - desconto

print(f"Voce teve um desconto de: R${desconto:.2f}")
print(f"O preço final do produto é: R${preco_final:.2f}")

# :2f serve para mostrar os valores com duas casas decimais, que é como
# costumamos fazer com dinheiro, colocando dentro das chaves da f-string
