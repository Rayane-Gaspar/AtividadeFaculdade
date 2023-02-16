print('Bem vindo a sorveteria da Rayane Cristina Gaspar')
print('-------------------------------------------CARDÁPIO--------------------------------------------')
print('| Código |      Descrição       | Tamanho P (500ML) | Tamanho M (1000 ml) | Tamanho G (2000ml)|')
print('|  TR   | Sabores Tradicionais |       R$6.00      |       R$10.00       |      R$18.00       |')
print('|  ES   |  Sabores Especiais   |       R$7.00      |       R$12.00       |      R$21.00       |')
print('|  PR   |   Sabores Premium    |       R#8.00      |       R$14.00       |      R$24.00       |')
print('|_____________________________________________________________________________________________|')

acumulador = 0
while True:
    sabores = input('qual sabor deseja? TR (tradicional), ES (especial), ou PR (premium)\n >>')
    if sabores != 'TR' and sabores != 'ES' and sabores != 'PR' and sabores:
        print('!!Sabor InvalidO!! Digite novamente uma opção válida:')
        continue
    tamanhos = input('Qual o tamanho desejado? (P/M/G)\n>>')
    if tamanhos != 'P' and tamanhos != 'M' and tamanhos != 'G' and tamanhos:
        print('!!Tamanho Invalido!! Digite novamente uma opção válida:')
        continue
    if sabores == 'TR' and tamanhos == 'P':
        print('Voce escolheu sorvete Tradicional tamanho P.')
        acumulador = acumulador + 6
    elif sabores == 'TR' and tamanhos == 'M':
        print('Voce escolheu sorvete Tradicional tamanho M.')
        acumulador = acumulador + 10
    elif sabores == 'TR' and tamanhos == 'G':
        print('Voce escolheu sorvete Tradicional tamanho G.')
        acumulador = acumulador + 18
    elif sabores == 'ES' and tamanhos == 'P':
        print('Voce escolheu sorvete Especial tamanho P.')
        acumulador = acumulador + 7
    elif sabores == 'ES' and tamanhos == 'M':
        print('Voce escolheu sorvete Especial tamanho M.')
        acumulador = acumulador + 12
    elif sabores == 'ES' and tamanhos == 'G':
        print('Voce escolheu sorvete Especial tamanho G.')
        acumulador = acumulador + 21
    elif sabores == 'PR' and tamanhos == 'P':
        print('Voce escolheu sorvete Premium tamanho P.')
        acumulador = acumulador + 8
    elif sabores == 'PR' and tamanhos == 'M':
        print('Voce escolheu sorvete Premium tamanho M.')
        acumulador = acumulador + 14
    elif sabores == 'PR' and tamanhos == 'G':
        print('Voce escolheu sorvete Premium tamanho G.')
        acumulador = acumulador + 24
    pedido = input('Deseja fazer mais algum pedido? S(Sim)/ N(Nao)')
    if pedido == 'Sim' or pedido == 'SIM' or pedido == 'sim' or pedido == 's' or pedido == 'S':
        continue

    else:
        print('Agradecemos o pedido. Seu total foi R${:.2f}'.format(acumulador))
        break
