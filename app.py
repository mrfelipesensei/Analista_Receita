#Dicionários vazios para armazenar despesas e receitas
despesas = []
receitas = []

#Função para adicionar uma despesa
def adicionar_despesa(valor, categoria):
    despesas.append({'valor': valor, 'categoria': categoria})

#Função para adicionar uma receita
def adicionar_receita(valor, fonte):
    receitas.append({'valor': valor, 'fonte': fonte})

#Função para calcular o saldo total
def calcular_saldo():
    total_despesas = sum(despesa['valor'] for despesa in despesas)
    total_receitas = sum(receita['valor'] for receita in receitas)
    return total_receitas - total_despesas

#Função para analisar as categorias de despesas
def analisar_despesas():
    from collections import defaultdict
    categorias = defaultdict(float)
    for despesa in despesas:
        categorias[despesa['categoria']] += despesa['valor']
    return dict(categorias)

#Exemplo de uso
adicionar_receita(1500, 'Salário')
adicionar_despesa(350, 'Dívida Itaú')
adicionar_despesa(200, 'Cartão Crédito')

saldo = calcular_saldo()
analise = analisar_despesas()

print('Análise de Despesas por Categoria:')
for categoria, valor in analise.items():
    print(f'{categoria}: R${valor}')
