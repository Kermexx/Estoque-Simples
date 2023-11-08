estoque = {}


def adicionar_produto():
    produto_novo = input("Qual produto será adicionado? ")
    if produto_novo:
        quantidade = int(input(f"Qual a quantidade de '{produto_novo}'? "))
        estoque[produto_novo] = estoque.get(produto_novo, 0) + quantidade
        print(f"{quantidade} unidades de '{produto_novo}' adicionadas ao estoque.")
    else:
        print("Nome do produto não pode estar vazio.")


def atualizar_produto():
    produto_alterado = input("Que produto terá a quantidade alterada? ")
    if produto_alterado in estoque:
        nova_quantidade = int(input(f"Fale a nova quantidade de '{produto_alterado}': "))
        estoque[produto_alterado] = nova_quantidade
        print(f"A quantidade de '{produto_alterado}' foi atualizada para {nova_quantidade}.")
    else:
        print(f"'{produto_alterado}' não está no estoque.")


def vender_produto():
    produto_vendido = input("Qual o produto que foi vendido? ")
    if produto_vendido in estoque:
        quantidade_disponivel = estoque[produto_vendido]
        quantidade_vendida = int(input(f"Quantos '{produto_vendido}' foram vendidos? "))
        if quantidade_vendida <= quantidade_disponivel:
            estoque[produto_vendido] -= quantidade_vendida
            print(f"{quantidade_vendida} unidades de '{produto_vendido}' foram vendidas.")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print(f"'{produto_vendido}' não está no estoque.")


def visualizar_estoque():
    print("Estoque atual:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")


while True:
    print("\nEscolha uma opção:")
    print("1- Adicionar um produto ao estoque")
    print("2- Atualizar a quantidade de um produto no estoque")
    print("3- Vender um produto")
    print("4- Visualizar o estoque atual")
    print("5- Sair do programa")
    escolha = input()

    if escolha == '1':
        adicionar_produto()
    elif escolha == '2':
        atualizar_produto()
    elif escolha == '3':
        vender_produto()
    elif escolha == '4':
        visualizar_estoque()
    elif escolha == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Escolha uma opção de 1 a 5.")
