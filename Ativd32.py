valor_total_venda = float(input("Digite o valor total da venda: "))
desconto = valor_total_venda * 0.10
total_pagar = valor_total_venda - desconto
valor_parcela = total_pagar / 3
comissao_vista = total_pagar * 0.05
comissao_parcelada = valor_total_venda * 0.05
print("Total a pagar com desconto de 10%:", total_pagar)
print("Valor de cada parcela:", valor_parcela)
print("Comissão do vendedor (à vista):", comissao_vista)
print("Comissão do vendedor (parcelada):", comissao_parcelada)