import json

# Carrega o json do faturamento diário
with open('faturamento.json') as file:
    faturamento = json.load(file)['faturamento_diario']

# Calcula o menor e o maior valor de faturamento ocorrido em um dia do mês
valores_faturamento = [valor for valor in faturamento.values() if valor != 0]
menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)

# Calcula a média mensal considerando apenas os dias em que houve faturamento
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Calcula o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

# Resultados que foram pedidos
print("=" * 20)
print(f"Menor valor de faturamento: R${menor_valor}")
print(f"Maior valor de faturamento: R${maior_valor}")
print("=" * 20)
print(f"Média mensal de faturamento: R${media_mensal:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
print("=" * 20)