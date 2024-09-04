import json
import os

def calcular_faturamento():
    mydir = os.getcwd()

    with open(mydir + '\\Testes_Target\\dados.json', 'r') as file:
        arquivo = json.load(file)
    
    valores = [item['valor'] for item in arquivo if item['valor'] > 0]

    menor_valor = min(valores)
    maior_valor = max(valores)

    media_mensal = sum(valores) / len(valores)

    dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

    print(f"Menor valor de faturamento: {menor_valor:.2f}")
    print(f"Maior valor de faturamento: {maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

calcular_faturamento()
