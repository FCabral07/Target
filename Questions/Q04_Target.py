# Define o faturamento mensal de cada estado, guardando em um dicionário
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o faturamento total
faturamento_total = sum(faturamento.values())

# Calculando e imprimindo o percentual de representação de cada estado no faturamento total
for estado, valor in faturamento.items():
    percentual = (valor / faturamento_total) * 100
    print(f'{estado}: {percentual:.2f}%')
