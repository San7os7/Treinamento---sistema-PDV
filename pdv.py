def caixa():
    produtos = []
    total = 0

    while True:
        nome = input("\nDigite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço unitário: "))

        subtotal = quantidade * preco
        produtos.append((nome, quantidade, preco, subtotal))
        total += subtotal

        continuar = input("Deseja adicionar mais produtos? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nResumo da compra:")
    for p in produtos:
        print(f"{p[1]}x {p[0]} - R$ {p[2]:.2f} cada - Subtotal: R$ {p[3]:.2f}")

    print(f"\nSubtotal: R$ {total:.2f}")
    desconto = float(input("Digite o desconto (%): "))
    total_com_desconto = total - (total * desconto / 100)

    print(f"Total com desconto: R$ {total_com_desconto:.2f}")

    valor_pago = float(input("\nDigite o valor pago: "))
    troco = valor_pago - total_com_desconto

    print(f"Troco: R$ {troco:.2f}")

# Executar o programa
caixa()
