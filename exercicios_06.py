'''
Type Check
Verificação de tipo (type check) é o processo de verificar o tipo de uma variável. 
Isso pode ser útil para garantir que operações ou funções sejam aplicadas apenas a tipos de dados compatíveis, 
evitando erros em tempo de execução.

Exemplo de Type Check
Para verificar o tipo de uma variável em Python, você pode usar a função type() ou isinstance().

valor_01 = input("Digite um valor não inteiro: ")

if isinstance(valor_01, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

'''

'''
Type Conversion
Conversão de tipo (type conversion), também conhecida como casting, é o processo de converter 
o valor de uma variável de um tipo para outro. Python oferece várias funções integradas 
para realizar conversões explícitas de tipo, como int(), float(), str(), etc.

Exemplo de Type Conversion
Se você quiser somar um inteiro e um número flutuante, pode ser necessário converter o 
inteiro para flutuante ou vice-versa para garantir que a operação de soma seja realizada corretamente.


numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5
'''


# try-except
# A estrutura try-except é usada para tratamento de exceções em Python. 
# Uma exceção é um erro que ocorre durante a execução do programa e que, s
# e não tratado, interrompe o fluxo normal do programa e termina sua execução. 
# O tratamento de exceções permite que o programa lide com erros de maneira 
# elegante, permitindo que continue a execução ou falhe de forma controlada.

# try: Este bloco é o primeiro na estrutura de tratamento de exceções. Python tenta executar o código dentro deste bloco.
# except: Se uma exceção ocorrer no bloco try, a execução imediatamente salta para o 
# bloco except. Você pode especificar tipos de exceção específicos para capturar e 
# tratar apenas essas exceções. Se nenhum tipo de exceção for especificado, ele captura todas as exceções.
# Exemplo de try-except.


'''
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")
'''

# if
# O if é uma estrutura de controle de fluxo que permite ao programa executar diferentes ações 
# com base em diferentes condições. Se a condição avaliada pelo if for verdadeira (True), 
# o bloco de código indentado sob ele será executado. Se a condição for falsa (False), o bloco de código será ignorado.

# if: Avalia uma condição. Se a condição for verdadeira, executa o bloco de código associado.
# elif: Abreviação de "else if". Permite verificar múltiplas condições em sequência.
# else: Executa um bloco de código se todas as condições anteriores no if e elif forem falsas.
# Exemplo de if4

valor_01 = float(input("Digite a sua idade: "))

if valor_01 < 18:
    print("Você é de menor!")
elif valor_01 == 18:
    print("Você tem exatamente 18 anos!")
else:
    print("Você é maior de idade!")