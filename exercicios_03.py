# Strings (str)

# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

'''
valor_01 = str(input("Digite seu nome: "))

resultado_final = print(valor_01.upper())
'''

# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

'''
valor_01 = str(input("Digite seu nome: "))

resultado_final = print(valor_01.lower())
'''

# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

'''
valor_01 = str(input("Digite seu nome: "))

resultado_final = print(valor_01.strip().lower())
'''

# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

'''
valor_01 = str(input("Digite a data de nascimento: "))

dia, mes, ano = valor_01.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
'''


# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.


valor_01 = str(input("Digite seu nome: "))

valor_02 = str(input("Digite seu sobre nome: "))

resultado_final = print(valor_01 + " " + valor_02)