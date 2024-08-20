# Tipos de concatenação
# Concatenação com sinal = 
num1 = int(input("Digite um numero inteiro: "))

# não é possivel concatenar numero inteiro usando esse modelo, a menos que 
# converta o numero inteiro em uma string
print('Ola, '+ str(num1) + '. Seja muito bem-vindo!')
print(type(num1))

# Concatenação com a (,)
print('O numero digitado é:',num1)

# Concatenação com f string (f)
print(f'O numero digitado é: {num1} usando a concatenação "f"')

div = num1 /3
# Usando format para formatação numérica
# limitando a quantidade de casas decimais
print(f'O resultado da divisoa é: {div:.2f}')

