nome = 'Davi'
idade = 17

print(nome)
print(f"O nome é {nome}")

peso = input('Digite seu peso: ')

num1 = input('Digite o primeiro numero: ')
num1 = int(num1)

num2 =  int(input('Digite o segundo numero: '))

#Códigos de cálculo entre as variáveis num1 e num2
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
divi = num1 / num2
divi_inteiro = num1 // num2
expo = num1 ** num2
modulo = num1 % num2

#Atribuição
num1 += 1
#num1 -= 1
#num1 *= 1
#num1 /= 1
#num1 //= 1
#num1 **= 1
#num1 %= 1

print("\n")
print('-----------------')
print(f"O nome é {nome}")
print(f'O seu peso é: {peso}')
print('-----------------')
print(f'O resultado da soma foi: {soma}')
print(f'O resultado da subtração foi: {sub}')
print(f'O resultado da multiplicação foi: {mult}')
print(f'O resultado da divisão foi: {divi:.2f}')
print(f'O resultado da divisão inteiro foi: {divi_inteiro}')
print(f'O resultado da exponenciação foi: {expo}')
print(f'O resultado do modulo foi: {modulo}')
print('-----------------')
print(f'O numero digitado + 1 é: {num1}')