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

while True:
    print('----Análise de Receita----')
    print('Digite 1 para Adicionar Receita')
    print('Digite 2 para Adicionar Despesa')
    print('Digite 3 para Analisar a Receita')
    print('Digite 4 para Sair')
    
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        quantidade = int(input("Quantas Receitas você deseja registrar? "))

        for i in range(quantidade):
            valor = float(input(f'Digite o Valor da Receita {i+1}: '))
            fonte = input(f'Digite a Fonte da Receita {i+1}: ')
            adicionar_receita(valor, fonte)
    elif opcao == 2:
        quantidade = int(input("Quantas Despesas você irá registrar? "))

        for i in range(quantidade):
            valor = float(input(f'Digite o Valor da Despesa {i+1}: '))
            categoria = input(f'Digite a Categoria da Despesa {i+1}:')
            adicionar_despesa(valor, categoria)
    elif opcao == 3:
        total_receitas, total_despesas, saldo = calcular_saldo()
        analise = analisar_despesas()
        print(f'Total de Receitas: R${total_receitas}')
        print(f'Total de Despesas: R${total_despesas}')
        print(f'Saldo Total: R$ {saldo}')
        print('Análise de Despesas por Categoria:')
        for categoria, valor in analise.items():
            print(f'{categoria}: R${valor}')
    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print('Opção Inválida.Tente novamente')
