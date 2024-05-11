# VAR
print('='*8, 'EMPRESTIMO BANCÁRIO', '='*8);
valorCasa = int(input('Qual o valor do imóvel a ser financiado: '))
salario = int(input('Qual o salario do solicitante: '))
anos = int(input('Em quantos anos deseja pagar: '))
parc = valorCasa / (anos*12)

#Code
print(f'O valor da parcela em {anos} é igual a {parc}')
if parc >= (salario*(30/100)):
    print('Não é possível financiar o imóvel para este cliente nestas condições!')
elif parc <= (salario*(30/100)):
    print('O cliente pode financiar o imóvel!')