# Números de Ponto Flutuante (float)

# 06 - Escreva um programa que receba dois números flutuantes e realize sua adição.

'''
valor_01 = float(input("Valor 01: "))
valor_02 = float(input("Valor 02: "))

resultado_final = print("Resultado: ", valor_01 + valor_02)
'''

# 07 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

'''
valor_01 = float(input("Valor 01: "))
valor_02 = float(input("Valor 02: "))

media = (valor_01 + valor_02) / 2

resultado_final = print("Resultado: ", media)
'''

# 08 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).




# 09 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.

'''
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solicita a temperatura em Celsius ao usuário
celsius = float(input("Digite a temperatura em Celsius: "))

# Converte para Fahrenheit
fahrenheit = celsius_para_fahrenheit(celsius)

# Exibe o resultado
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
'''

# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.


import math

# Função para calcular a área do círculo
def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

# Solicita o raio ao usuário
raio = float(input("Digite o raio do círculo: "))

# Calcula a área
area = calcular_area_circulo(raio)

# Exibe o resultado
print(f"A área do círculo com raio {raio} é: {area:.2f}")

