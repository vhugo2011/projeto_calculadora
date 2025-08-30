permanecer_no_loop = '1'
while permanecer_no_loop == '1' :
    print("\nSelecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    
    escolha = input("Digite sua escolha (1/2): ")

    if escolha in ['1', '2']:
        try:
            num1 = float(input("Digite um número: "))
            num2 = float(input("Digite outro número: "))
        except ValueError:
            print("Número inválido!")
            continue

        if escolha == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")

        elif escolha == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")

    else:
        print("Opção inválida. Tente novamente.")
    
    permanecer_no_loop = input("Digite 1 para uma nova operação, e qualquer outra tecla para sair:\n")