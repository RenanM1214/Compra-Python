nome_cliente = input("Digite o nome do cliente: ") 
numero_pedido = input("Digite o número do pedido: ") 
pedido = {} 
menu = { 
    "100": {"produto": "Coxinha Frango", "preco": 0.85}, 
    "101": {"produto": "Bolinha Queijo", "preco": 0.85}, 
    "102": {"produto": "Kibe", "preco": 0.95}, 
    "103": {"produto": "Esfirra Carne", "preco": 0.95}, 
    "104": {"produto": "Lanche Natural", "preco": 8.0}, 
    "105": {"produto": "Beirute", "preco": 15.00},
    "106": {"produto": "Refrigerante", "preco": 5.50}} 

def calcular_total(pedido): 
    total = 0 
    for item, quantidade in pedido.items(): 
        total += menu[item]["preco"] * quantidade 
    return total

while True: 
    print("\nMenu:") 
    for key, value in menu.items(): 
        print(f"{key}: {value['produto']} - R${value['preco']}")
    escolha = input("\nEscolha um produto pelo número (ou 'F' para finalizar): ") 

    if escolha.upper() == 'F': 
        print(f"Senhor {nome_cliente} seu pedido ficou no total de R${valor_total}")
        break 

    if escolha in menu: 
        quantidade = int(input(f"Digite a quantidade de {menu[escolha]['produto']} desejada: ")) 
        pedido.setdefault(escolha, 0) 
        pedido[escolha] += quantidade 
    else: print("Escolha inválida. Tente novamente.")  
    
    valor_total = calcular_total(pedido) 
    print(f"\nResumo do Pedido:") 
    print(f"Nome do Cliente: {nome_cliente}") 
    print(f"Número do Pedido: {numero_pedido}") 
    print("Itens do Pedido:") 

    for item, quantidade in pedido.items(): 
        print(f"{menu[item]['produto']} - Quantidade: {quantidade}") 
        print(f"Valor Total do Pedido: R${valor_total}")
