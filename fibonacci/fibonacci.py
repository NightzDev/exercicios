try:
    # O input será feito para receber o numero para saber se ele faz parte da sequência de fibonacci
    num = int(input("Digite um número: "))
    
    # Define os dois primeiros termos da sequência de Fibonacci
    a, b = 0, 1

    # Repete o loop até que o valor de b seja igual ou maior que o número digitado
    while b < num:
        # Atualiza os valores de a e b para os próximos termos da sequência
        a, b = b, a + b
    
    # Verifica se o numero pertence à sequência de Fibonacci
    if b == num:
        print(num, "pertence à sequência de Fibonacci.")
    else:
        print(num, "não pertence à sequência de Fibonacci.")
except ValueError: #Tratamento de erro, caso o usuário digite errado e não dar um erro complexo para um usuário comum
    print("O valor é inválido")