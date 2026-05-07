def validar_int(msg_int):
    while True:
        try:
            return int(input(msg_int))
        except ValueError:
            print('Digite apenas números!\n')


def preco_final(msg_preco, msg_desconto):
    while True:
        try:
            preco = float(input(msg_preco))
            desconto = float(input(msg_desconto))
            if preco < desconto:
                print('Desconto não pode ser maior que preço!\n')
                continue
            else:
                return preco - desconto
        except ValueError:
            print('Digite apenas números!\n')

# Programa principal
categorias = {
    1: 'supermercado',
    2: 'refeições fora',
    3: 'higiene pessoal',
    4: 'produtos de limpeza'
}

print('--- CATEGORIAS ---')
for chave, valor in categorias.items():
    print(f'{chave} {valor}')

print('\nQuando selecionar categoria, digite o número correspondente.')

produtos = []
while True:
    produto = {}

    produto['categoria'] = validar_int('Qual a categoria do produto? ')

    if produto['categoria'] not in categorias:
        print('Categoria inválida!\n')
        continue

    produto['nome'] = input('Qual o nome do produto? ').lower()
    produto['preço final'] = preco_final('Qual o preço do produto? ', 'Qual o desconto do produto? ')

    produtos.append(produto)

    continuar = input('\nQuer continuar? [s/n] ').strip().lower()
    if continuar == 'n':
        break
    else:
        print('-' * 50)
        print('\n--- CATEGORIAS ---')
        for chave, valor in categorias.items():
            print(f'{chave} {valor}')

        print()

somatorio = {}
for produto in produtos:
    nome_categoria = categorias[produto['categoria']]

    if nome_categoria not in somatorio:
        somatorio[nome_categoria] = 0

    somatorio[nome_categoria] += produto['preço final']

for categoria, valor in somatorio.items():
    print(f'{categoria}: {valor:.2f}')
