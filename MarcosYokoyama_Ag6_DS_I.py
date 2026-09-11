# Entrada de dados: valor total da compra
valor_compra = float(input("Informe a valor total da compra: "))

# Condicional para definir o desconto conforme as faixas de valor
if valor_compra < 200:
    valor_desconto = valor_compra * 0.05
elif valor_compra >=200 and valor_compra <300:
    valor_desconto = valor_compra * 0.10
else:
    valor_desconto = valor_compra * 0.15

# Cálculo do valor total a ser pago com desconto
valor_final = valor_compra - valor_desconto
# Saída de dados: exibição dos resultados formatados
print(f"O valor de desconto foi de: R$ {valor_desconto:.2f}")
print(f"O valor a ser pago é: R$ {valor_final:.2f}")   
