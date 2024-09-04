def fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1

    while a < n:
        a, b = b, a + b

    return a == n
while True:
    numero = input('Digite um número que deseja saber se ele pertece a sequência de fibonacci: ')

    if numero.isnumeric():
        numero = int(numero)

        if fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")

    else:
        print('Digite um número inteiro')

    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break
        