# Faturamento mensal por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do total de faturamento
totalFaturamento = sum(faturamento.values())

# Cálculo do percentual de representação de cada estado
percentuais = {estado: (valor / totalFaturamento) * 100 for estado, valor in faturamento.items()}

# Exibição dos resultados
print("Percentual de representação de cada estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
