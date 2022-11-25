import string
import random

pergunta = int(input('O que você deseja\n'
                     '1- Ver senhas\n'
                     '2- Adicionar senha\n'
                     '3- Ver uma senha espesifica\n'
                     'DIGITE AQUI: '))
if pergunta == 1:
    with open("senhas.txt", "r", encoding="utf-8") as ler_arquivo:
        senhas = ler_arquivo.read()
    print(senhas)

elif pergunta == 2:
    while True:

        # A senha sera salva no nome da variavel [nome]
        nome = str(input('Para quem a senha vai ser gerada? '))

        # Para qual site/app vai usar essa senha
        local = str(input('Nome onde onde vai usar essa senha: '))

        numero_para_string = 1
        quantidade_de_letras = 9
        for x in range(numero_para_string):
            senha = (''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in
                             range(quantidade_de_letras)))
            nova_senha = f"{nome}/{local} = {senha}"
            print(nova_senha)

        while True:
            guardar = str(input('Deseja guardar essa senha? [S/N] ')).upper()

            if guardar == 'S':
                with open("senhas.txt", "a") as adicionar_senha:
                    adicionar_senha.write(f"\n" + nova_senha)
                print('Senha guardada.')

                exit()
            elif guardar == 'N':
                opcao2 = str(input('Deseja refazer as configuraçoes? [S/N] ')).upper()
                if opcao2 == 'N':
                    exit()
                elif opcao2 == 'S':
                    print('Ok, refazendo...')
                    break
            else:
                print('ERRO! Digite (S) para sim e (N) para não.')

elif pergunta == 3:

    sennha_especifica = str(input('Qual senha voce busca? '))

    with open("senhas.txt", "r", encoding="utf-8") as ler_senha_especifica:
        senha = ler_senha_especifica.readlines()

    for linha in senha:
        if sennha_especifica in linha:
            print(linha)
        else:
            print('Essa senha ainda nao existe.')

else:
    print('Desculpe algo esta errado, tente novamente.')
