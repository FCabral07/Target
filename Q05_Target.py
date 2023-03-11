# Recebendo a entrada do usuário
texto = input('Digite a palavra que você gostaria de inverter: ')

# Definindo onde será guardada a string invertida
texto_invertido = ''

# Criando um loop que começa do último caractere da string, vai até o primeiro, voltando 1 casa
for i in range(len(texto)-1, -1, -1):
    # Adicionando a string invertida a variável que irá salvá-la
    texto_invertido += texto[i]

# Imprimindo a string invertida
print(f"A string invertida é: {texto_invertido}")
