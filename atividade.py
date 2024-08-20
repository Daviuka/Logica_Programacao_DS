##concatenação com sinal (+)
#concatenação com a vírgula
nome = input("Digite o seu nome: ")
print("Olá, "+ nome +". Seja bem-vindo!")
email = input("Digite o seu endereço de e-mail: ")
telefone = input("Digite o seu número de telefone: ")

gasto_gasolina = 64 * 20 / 14
gasto_alcool = 64 * 20 / 12
mediakm = 64 * 5 * 4

gasto_alcool = int(gasto_alcool)
gasto_gasolina = int(gasto_gasolina)

print("\n")
print("===============")
print("Nome de usuário: ",nome)
print("Endereço de Email: ",email)
print("Número de telefone: ",telefone)
print("---------------")
print("Seu gasto mensal no álcool é de: ",gasto_alcool,"litros.")
print("Seu gasto mensal na gasolina é de: ",gasto_gasolina,"litros.")
print("A média de quilômetros rodados mensalmente é: ",mediakm,"quilômetros")
print("===============")
print("\n")

'''
    Desenvolva um sistema que receba o cadastro do nome de usuario e as 
    suas informações basicas, como, email e telefone, em seguida, calcule
    o gasto de combustivel mensal, considerando que o carro que ele usa tem
    capacidade total de 55 litros. Na gasolina ele tem autonomia de 14km/l, já
    no alcool a autonomia é de 12km/l. Considere que de casa ao trabalho são 32km
    e ele precisa ir e voltar do trabalho de segunda a sexta. 
        
    Qual será o gasto mensal (reais/litro) que o usuario terá no alcool e na gasolina? 
    Qual á média de kilometros rodados mensalmente?
'''