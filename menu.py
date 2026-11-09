from time import sleep
from Python_CursoEmVideo.menuCadastro import Erro,Enunciados


arquivo=open('arquivo.txt','w')
while True:
    print('\033[0;0m')
    print('-'*50)
    print('Menu Principal'.center(50))
    print('-'*50)
    print('\033[1;32m1 \033[;1m-\033[1;34mVer pessoas cadastradas\n'
          '\033[1;32m2 \033[;1m-\033[1;34mCadastrar nova pessoa\n'
          '\033[1;32m3 \033[;1m-\033[1;34mSair do programa\n')
    print('\033[0;0m')
    print('-'*50)
    a=Erro.menu('\033[1;32mSua opção: ')
    if a == 1:
        Enunciados.cabecalho(a)
        sleep(1)

        with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())

        sleep(2)
    elif a == 2:
        Enunciados.cabecalho(a)
        sit = True
        while sit:
            nome = input('Nome: ')
            idade = input('Idade: ')

            with open('arquivo.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'Nome:{nome.ljust(25)}'f'Idade:{idade} anos\n'.rjust(10))

            while True:
                i = input('Deseja continuar? [S/N] ').upper().strip()

                if i in ('S', 'N'):
                    if i == 'N':
                        sit = False
                    break
                else:
                    print('\033[1;31mErro!!! Opção inválida.\033[m')

    else:
        break
print('\033[0;0m')
print('Volte sempre!')