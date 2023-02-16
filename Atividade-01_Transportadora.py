print('RU:1714974','Aluna:Rayane Cristina Gaspar')
print('Bem vindo a loja Rayane C Gaspar!')
prod=input('Digite o produto desejado:')                     #Recebe o produto que o cliente deseja adquirir na loja.
preco=float(input('Digite o preço do produto:'))             #Recebe o preço que o produto custa.
quant=int(input('Digite a quantidade de produto desejado:')) #Recebe a quantidade de itens que o cliente deseja adquirir.
total=int(preco*quant)                                       #Recebe o total da compra sem o acréscimo do valor do frete pré-definido por tabela.
print('O valor total do seu pedido sem calcular o frete é R$:', total)
if quant <11:                                                # Neste bloco de condicionais irá ser estabelecido o valor pago pelo frete de acordo com a quantidade comprada.
    frete=((preco*quant)+30)
elif quant  >11 and quant <101:
    frete=((preco*quant)+60)
elif quant >101 and quant <1001:
    frete=((preco*quant)+120)
else:
    quant >1001
    frete=((preco*quant)+240)
print('O valor da sua compra com frete é R$', frete)
print('Agradecemos a preferência!')                          #Agradecimento para finalizar o programa de forma gentil.