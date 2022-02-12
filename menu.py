import random #importando a biblioteca pro voucher

dados = {'voucher':[random.randint(100,400)], 'nome':[], 'email':[], 'telefone':[], 'curso':[]} #dicionário com listas

while True: #loop pra pessoa escolher de novo caso ela queira continuar
    print('         MENU        ')
    print('1 - Nova inscrição\n2 - Visualizar inscrição\n0 - Encerrar') #opções de escolha
    opcao = int(input('Qual a opção desejada?'))
    if (opcao == 1):
        print('Opção escolhida: {}' .format(opcao))
        nome = input('Digite seu nome: ') #variáveis que devem ser digitadas pelo usário
        email = input('Digite seu email: ')
        telefone = int(input('Digite seu telefone: '))
        curso = input('Digite seu curso: ')
    elif (opcao == 2):
        print('Opcao escolhida: {}' .format(opcao))
        print('******* Lista de inscritos *******')
        dados['nome'].append(nome) #adicionando os dados nas listas
        dados['email'].append(email)
        dados['telefone'].append(telefone)
        dados['curso'].append(curso)
        print(dados) #escrecer o dicionário agora com as listas completadas
    elif (opcao == 0): #caso a pessoa queira encerrar a sessão
        print('Fechando o programa...')
        break
    else:
        print('Opção inválida!') #caso a pessoa digite qualquer outra coisa






