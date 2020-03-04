valor_total = float(input("Digite o valor do produto: "))
valor_desconto = valor_total - (valor_total * 0.1)
valor_desconto -= valor_desconto*0.1
print(round(valor_desconto,2))