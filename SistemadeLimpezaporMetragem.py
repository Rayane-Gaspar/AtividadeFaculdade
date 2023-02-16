
# ------------------------------ Inicio Quadros com Informações: ------------------------------

def linha ():
    print('-' * 190)

linha()
print('|    METRAGEM(m²)      |       VALOR (R$)        | |             TIPO DE LIMPEZA                      |  MULTIPLICADOR   | |         ADICIONAIS                   |       VALOR (R$)         |')
linha()
print('| 30 <= metragem < 300 |    60 + 0.3 * metragem  | | 1.BASICA-Limpeza  semanal ou quinzenal           |      1.00        | | 0 - Não desejpo mais nada/ Encerrar  |        (R$)  0.00        |')
linha()
print('|300 <= metragem < 700 |   120 + 0.5 * metragem  | | 2.COMPLETA-Limp. de sujeira antiga/não rotineira |      1.30        | | 1 - Passar 10 peças de roupas        |        (R$) 10.00        |')
linha()
print('|    Outros Valores    |    Não são aceitos      | |                  -------------                   |                  | | 2 -Limpar 1 forno/microo0ondas       |        (R$) 12.00        |')
linha()
print('|                        --------                | |                  -------------                   |                  | | 2 -Limpar 1 geladeira/freezer        |        (R$) 20.00        |')
linha()

# ------------------------------ Inicio Quadros com Informações: ------------------------------

# ------------------------------ Inicio das Funções: ------------------------------

def metragem():
    print('---------------Menu 1 de 3 -  Metragem da limpeza  - ----------------- ')                  # Esta função irá calcular o valor da limpeza com base na metragem do local
    while True:
        try:
            metragem1 = int(input('Digite a metragem do local a ser limpo: \n' +
                                 '>> '))
            if (metragem1 >= 30) and (metragem1 < 300):                                               # Por definição, a metragem não deve ser menor que 29 m² nem maior que 701  m²
                print('Será necessário UMA funcionaria para a limpeza')                               #Analisa também se serão necessarias UMA ou DUAS funcionarias para limpar o local. Já pré estabelecido
                calculo = 60 + metragem1 * 0.3
                return calculo

            elif (metragem1 >= 300) and (metragem1 < 700):
                print('Serão necessárias DUAS funcionárias para a limpeza.')
                calculo = 120 + metragem1 * 0.5
                return calculo
            else:
                print("Opção Invalida. Digite novamente.")
                continue
        except ValueError:  # Caso o usuario digite algum valor nao numerico; Como decimais ou strings
            print('Valor não aceito. Digite números inteiros!')

def tipo_limpeza ():                                                                                    # Esta função irá calcular os valores com base no tipo de limpeza escolhida pelo usuário
    print('---------------Menu 2 de 3 -  Tipo de limpeza  - -----------------')
    while True:
        try:
            limpeza=int(input('Qual o tipo de limpeza desejada? \n' +
                              '1 = limpeza básica:indicada para limpeza semanal e/ou quinzenal \n' +
                              '2 = limpeza completa:indicada para sujeiras antigas e/ ou não rotineiras \n' +
                              '>>'))
            if limpeza == 1:
                multiplicador = 1.0
                return multiplicador
            elif limpeza == 2:
                multiplicador = 1.3
                return multiplicador
            else:
                print('Valor inválido! Digite novamente')
        except ValueError:
            print('Valor Invalido. Tente novamente!')
def adicionais():                                                                                         # Esta função irá calcular se terão adicionais e quais o cliente esscolherá
    print('---------------Menu 3 de 3 - Adicionais de limpeza - ------------- ')
    acumulador = 0
    while True:
        adicionais = (input('Deseja mais algum adicional? \n' +
                            '0 - Não desejo mais nada.             - R$0.00 \n' +
                            '1 - Passar 10 peças de roupa          - RS10.00 \n' +
                            '2 - Limpeza de um forno/micro-ondas   - R$12.00 \n' +
                            '3 - Limpeza de 1 geladeira/freezer    - R$20.00 \n' +
                            '>>'))
        if (adicionais == '0'):
            return acumulador
        elif (adicionais == '1'):
            acumulador = acumulador + 10
            continue
        elif (adicionais == '2'):
            acumulador = acumulador + 12
            continue
        elif (adicionais == '3'):
            acumulador = acumulador + 20
            continue
        else:
            print('OPÇÃO NÃO ACEITA. Digite novamente: 0/1/2/3')

# ----------------------- Fim das Funções -----------------------


# ----------------------- Inicio do Programa principal: ------------------------
print('~~'*35)
print('      Bem vindo ao programa de limpeza Rayane Cristina Gaspar')
print('~~'*35)
print(' ')
metragem = metragem()
tipo = tipo_limpeza()
valor_parcial = metragem * tipo
adicionais = adicionais()
total = valor_parcial + adicionais
print('O total a ser pago é R$ {:.2f},sendo metragem R$ {:>2f}, tipo de limpeza R$ {:.2f}, adicionais {:.2f}'.format (total, metragem, tipo, adicionais))

