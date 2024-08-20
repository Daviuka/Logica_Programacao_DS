print("Olá Mundo")

nome = 'Davi'
idade = 17
peso = 80.5
altura = 1.79
instrutor = True

#FIXME:Visualizando os tipos de dados
print(type(nome))
print(type(idade))
print(type(peso))
print(type(altura))
print(type(instrutor))


# FIXME:Entrada de dados

sobrenome = input('Digite o seu sobrenome: ')

print(nome, sobrenome)
print(type(sobrenome))

#Convertendo o valor do input

idade = input('Digite sua idade: ')
idade = int(idade)
print(type(idade))

ano = int(input('Em qual ano estamos: '))
print(type(ano))

if ano > 2024:
    print("Fora do if")
    
