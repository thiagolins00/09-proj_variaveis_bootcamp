'''
Type Check
Verificação de tipo (type check) é o processo de verificar o tipo de uma variável. 
Isso pode ser útil para garantir que operações ou funções sejam aplicadas apenas a tipos de dados compatíveis, 
evitando erros em tempo de execução.

Exemplo de Type Check
Para verificar o tipo de uma variável em Python, você pode usar a função type() ou isinstance().
'''

valor_01 = input("Digite um valor não inteiro: ")

if isinstance(valor_01, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")