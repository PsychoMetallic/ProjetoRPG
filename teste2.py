nomes = []

while True:
    opcao = int(input('''\nvocê deseja: 1- adicionar um nome | 2- sair
>> '''))
    
    if opcao == 1:
        nome = input('''\nnome?
>> ''')
    
        nomes.append(nome)
        
    else:
        break

    

print(nomes)