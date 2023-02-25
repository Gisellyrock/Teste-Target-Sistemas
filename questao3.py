import json

# Lê o arquivo JSON com o faturamento diário
with open('faturamento_diario.json') as f:
    faturamento_diario = json.load(f)

# Calcula o menor e o maior valor de faturamento diário
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Calcula a média mensal de faturamento, ignorando os dias sem faturamento
dias_com_faturamento = [f for f in faturamento_diario if f > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Conta o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento_diario if f > media_mensal)

# Imprime os resultados na tela
print("Menor faturamento diário:", menor_faturamento)
print("Maior faturamento diário:", maior_faturamento)
print("Número de dias acima da média mensal:", dias_acima_da_media)

