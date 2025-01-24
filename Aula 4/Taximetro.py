"""
Criar um novo arquivo chamado taximetro.py;
Receber a quantidade de km rodados pelo táxi;
Receber o preço por km do táxi;
Receber a taxa fixa do táxi;
Exibir o preço total da corrida.
"""
quantidade_km_rodado = float(input())
preco_por_km = float(input())
taxa_fixa = float(input())
preco_total = (quantidade_km_rodado * preco_por_km) + taxa_fixa

print(preco_total)