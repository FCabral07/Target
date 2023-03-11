# Defino a função que irá calcular se é ou não
def fibonacci(numero_fibonacci):
    # Casos iniciais
    if numero_fibonacci == 0:
        return 0
    elif numero_fibonacci == 1:
        return 1
    # Casos após o 1
    else:
        k, j = 0, 1
        while j < numero_fibonacci:
            k, j = j, k + j
        if j == numero_fibonacci:
            return numero_fibonacci
        else:
            return None

# Recebe a entrada do usuário
numero = int(input("Informe um número: "))

# Atribui a entrada para a função fibonacci e a aloca para a variável resultado
resultado = fibonacci(numero)

# Saída dos dados mostrando se pertence ou não à sequência de fibonacci
if resultado == None:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
