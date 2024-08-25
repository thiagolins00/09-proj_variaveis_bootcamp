'''
Exemplo de TypeError
Um exemplo clássico é tentar utilizar a função len() com um inteiro, o que resulta em TypeError, 
pois len() espera um objeto iterável, como uma string, lista, ou tupla, não um inteiro.


try:
    valor_01 = float(input("Digite o valor 01: "))
    valor_02 = float(input("Digite o valor 02: "))
    
    resultado = valor_01 + valor_02
    print(f"O resultado da soma é: {resultado}")
except ValueError as e:
    print("Erro: Por favor, digite apenas números.")
    valor_02 = float(input("Digite o valor 02: "))
except TypeError as e:
    print(f"Erro de tipo: {e}") 
'''

while True:  # Inicia um loop infinito
    try:
        valor_01 = float(input("Digite o valor 01: "))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Erro: Por favor, digite apenas números.")

while True:  # Inicia um loop infinito
    try:
        valor_02 = float(input("Digite o valor 02: "))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Erro: Por favor, digite apenas números.")

resultado = valor_01 + valor_02
print(f"O resultado da soma é: {float(resultado)}")
print(f"Obrigadooooo!!!")