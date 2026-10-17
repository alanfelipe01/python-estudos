"""
O objetivo é criar um programa em Python que leia um número inteiro e mostre:
- Antecessor: o número que vem antes.
- Sucessor: o número que vem depois.
"""

numero = int(input("DIGITE UM NUMERO: "))
antecessor = numero - 1
sucessor = numero + 1

print(f"O antecessor de {numero} é {antecessor}, e o sucessor é {sucessor}.")
