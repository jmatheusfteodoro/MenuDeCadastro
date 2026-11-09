def menu(num):
    while True:
        n = input(num)

        try:
            valor = int(n)
        except ValueError:
            print('\033[1;31mErro!!! Digite um valor inteiro válido.\033[m')
            continue

        if 1 <= valor <= 3:
            return valor
        else:
            print('\033[1;31mErro!!! Essa opção não existe no sistema.\033[m')