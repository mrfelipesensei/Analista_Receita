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
    return total_receitas, total_despesas, total_receitas - total_despesas

#Função para analisar as categorias de despesas
def analisar_despesas():
    from collections import defaultdict
    categorias = defaultdict(float)
    for despesa in despesas:
        categorias[despesa['categoria']] += despesa['valor']
    return dict(categorias)

#Exemplo de uso
fonte = input("Insira a fonte da Receita: ")
valor = float(input("Insira o valor da Receita: "))
adicionar_receita(valor, fonte)

adicionar_despesa(350, 'Dívida Itaú')
adicionar_despesa(200, 'Cartão Crédito')

total_receitas, total_despesas, saldo = calcular_saldo()
analise = analisar_despesas()

print(f'Total de Receitas: R${total_receitas}')
print(f'Total de Despesas: R${total_despesas}')
print(f'Saldo Total: R$ {saldo}')

print('Análise de Despesas por Categoria:')
for categoria, valor in analise.items():
    print(f'{categoria}: R${valor}')
