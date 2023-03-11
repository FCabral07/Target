import json

# Lê o arquivo json com os dados do faturamento diário
with open("./assets/dados.json") as file:
    dados = json.load(file)

# Filtra os dias do mês em que houve faturamento
dias_faturamento = [dado['valor'] for dado in dados if dado is not None]

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(dias_faturamento)
maior_faturamento = max(dias_faturamento)

# Calcula a média mensal de faturamento
media_mensal = sum(dias_faturamento) / len(dias_faturamento)

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_media = sum(1 for valor in dias_faturamento if valor > media_mensal)

# Exibe os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias acima da media: {dias_acima_media}")