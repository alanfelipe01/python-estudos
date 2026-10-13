"""
O objetivo é criar um programa em Python que leia um número inteiro e mostre:
- Antecessor: o número que vem antes.
- Sucessor: o número que vem depois.
"""

numero = int(input("Digite um numero: "))
antecessor = numero -1 
sucessor = numero + 1

print(f"O Antecessor de {numero} é: {antecessor}")

print(f"O Sucessor de {numero} é: {sucessor}")
