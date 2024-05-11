print('='*8, 'PONTO DE VENDA', '='*8)
valor = float(input('Digite o preço da compra: R$'))
frm_d_pgmt = int(input('''Escolha a forma de pagamento
                   [ 1 ] À vísta (dinheiro ou PIX)
                   [ 2 ] À vista (cartão)
                   [ 3 ] Parcelado (até 2x) no cartão
                   [ 4 ] 3x ou mais (cartão)
                   Digite a forma de pagamento: '''))
if frm_d_pgmt == 1:
    desc = (valor*(10/100))
    j = 0
    parc = 0
    nparc = 0
elif frm_d_pgmt == 2:
    desc = (valor*(5/100))
    j = 0
    parc = 0
    nparc = 0
elif frm_d_pgmt == 3:
    desc = 0
    j = 0
    parc = 0
    nparc = 0
elif frm_d_pgmt == 4:
    nparc = int(input('Em quantas vezes quer parcelar? '))
    desc = 0
    j = (valor*(20/100))
    parc = (valor+j)/nparc
else:
    valor = 0
    print('Opção invalida tente novamente!')
valorCmDesc = valor - desc + j
print('++++ RESUMO DA COMPRA ++++'
            f'\n VALOR DO PRODUTO: R${valor}'
            f'\n DESCONTO: R${desc:.2f}'
      f'\n JUROS: {j:.2f}'
      f'\n VALOR DAS PARCELAS: R${parc} ({nparc}x)'
            f'\n VALOR A PAGAR: R${valorCmDesc:.2f}')
