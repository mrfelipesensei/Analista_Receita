#Dicionários vazios para armazenar despesas e receitas
despesas = []
receitas = []

#Função para adicionar uma despesa
def adicionar_despesa(valor, categoria):
    despesas.append({'valor': valor, 'categoria': categoria})

#Função para adicionar uma receita
def adicionar_receita(valor, fonte):
    receitas.append({'valor': valor, 'fonte': fonte})

