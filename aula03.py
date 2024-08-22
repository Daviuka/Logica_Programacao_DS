nome = 'Davi'
idade = 17

print('-----------------')
print(nome)
print(f"O nome é {nome}")
print('-----------------')
peso = input('Digite seu peso: ')
print('-----------------')
num1 = input('Digite o primeiro numero: ')
num1 = int(num1)
print('-----------------')
num2 =  int(input('Digite o segundo numero: '))
print('-----------------')

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

# FIXME:Operadoes matemáticos
print("\n")
print('-----------------')
print("Operadores matemáticos no print")
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)
print(num1 % num2)
print('-----------------')
# FIXME:Operadores comparativos
print(" ")
print('-----------------')
print("Operadores comparativos")
print(num1 > num2) # maior que
print(num1 < num2) # menor que
print(num1 == num2) # igualdade
print(num1 != num2) # diferente
print(num1 <= num2) # menor ou igual

print(num1 <= 100 and num2 <= 100 and (num1 + num2) > 100)
print('-----------------')

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
print('-----------------')
print("\n")
