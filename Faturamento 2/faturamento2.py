# Faturamento dentro do exercício
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Soma de todos os valores do faturamento
total_faturamento = sum(faturamento.values())

# Loop dos items do faturamento
for estado, valor in faturamento.items():
    # O calculo é feito pelo numero do valor (de cada estado) divido pelo faturamento total feito acima e depois divido por 100
    percentual = (valor / total_faturamento) * 100
    # E aqui terá o percentual imprimido
    print(f"{estado}: {percentual:.2f}%")
