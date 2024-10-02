import json

# Exemplo de dados de faturamento em formato JSON
faturamentoJson = """
{
    "faturamento": [
        {"dia": 1, "valor": 100},
        {"dia": 2, "valor": 200},
        {"dia": 3, "valor": 0},
        {"dia": 4, "valor": 150},
        {"dia": 5, "valor": 300},
        {"dia": 6, "valor": 0},
        {"dia": 7, "valor": 400},
        {"dia": 8, "valor": 250},
        {"dia": 9, "valor": 0},
        {"dia": 10, "valor": 350}
    ]
}
"""

data = json.loads(faturamentoJson)

# Extraindo valores de faturamento
faturamentos = [d['valor'] for d in data['faturamento'] if d['valor'] > 0]

# Cálculo do menor e maior faturamento
menorFaturamento = min(faturamentos) if faturamentos else 0
maiorFaturamento = max(faturamentos) if faturamentos else 0

# Cálculo da média mensal
mediaFaturamento = sum(faturamentos) / len(faturamentos) if faturamentos else 0

# Contando dias com faturamento acima da média
diasAcimaDaMedia = sum(1 for valor in faturamentos if valor > mediaFaturamento)

# Resultados
print(f"Menor faturamento: R${menorFaturamento:.2f}")
print(f"Maior faturamento: R${maiorFaturamento:.2f}")
print(f"Número de dias acima da média: {diasAcimaDaMedia}")
