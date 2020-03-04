nome = input()
salario = float(input())
vendas = float(input())
comissao = (vendas * 0.05)
salario_final = salario + comissao
print("{} deve receber R${:.2f}".format(nome,salario_final))