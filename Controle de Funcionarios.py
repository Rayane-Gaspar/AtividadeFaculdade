# ----------Início das Variáveis Globais: ----------

lista_funcionario = []
codigo_funcionario = 0

# ----------Fim das Variáveis Globais: ----------

# ----------Início da função CADASTRAR funcionário: ----------

def cadastrar_funcionario(codigo_entrada):                                     # Função que irá cadastrar os funcionários e armazena-los na lista definida.
    print('~~'*25)
    print('Bem vindo ao menu CADASTRO de funcionários \n')
    print('Código do Funcionário: {}'.format(codigo_entrada))
    nome_funcionario = input('Digite o NOME completo do funcionário a ser cadastrado: \n' +
                             '>>')
    setor_funcionario = input('Digite o SETOR no qual o funcionário trabalhará: \n'+
                              '>>')
    salario_funcionario = float(input('Digite o SALÁRIO do funcionário: (R$) \n' +
                                      '>>'))
    print('~~'*25)
    dicionario_funcionario = {'codigo': codigo_entrada,
                              'nome': nome_funcionario,
                              'setor': setor_funcionario,
                              'salario': salario_funcionario}
    lista_funcionario.append(dicionario_funcionario.copy())                  # Onde irá ficar salvo os funcionários cadastrados.

 # ----------Fim da função CADASTRAR funcionário. ----------

def consultar_funcionario():                                                 #Função para realizar a consulta dos funcionários cadastrados.

    print('~~'*25)
    while True:
        opcao_consultar = input( '\n Escolha a opção desejada: \n'+
                                ' 1 - consultar todos os funcionarios \n'+
                                ' 2 - consultar funcionarios por id \n'+
                                ' 3 - consultar funcionario(s) por setor \n'+
                                ' 4 - retornar \n'+
                                '>>')
        print('~~' * 25)
        if opcao_consultar == '1':
          print('Você escolheu a opção consultar todos os funcionarios')
          for funcionario in lista_funcionario:                             # Variavel funcionário vai varrer toda a lista de funcionários
            print('-'*20)
            for key, value in funcionario.items():                          # Irá varrer todos os conjuntos chave e valor do dicionario funcionário
              print('{}: {} '.format(key, value))
            print('-'*20)
        elif opcao_consultar == '2':
          print('Você escolheu a opção consultar funcionarios por ID')
          valor_desejado = int(input('Entre com o ID desejado: '))
          for funcionario in lista_funcionario:
            if funcionario['codigo'] == valor_desejado:                      # Verificar se valor do campo código desse dicionario é igual o valor desejado pela consulta
              print('-'*20)
              for key, value in funcionario.items():                         # Irá varrer todos os conjuntos chave e valor do dicionario funcionário
                print('{}: {} '.format(key, value))
              print('-'*20)
        elif opcao_consultar == '3':
           print('Você escolheu a opção consultar funcionario(s) por SETOR')
           valor_desejado = input('Entre com o SETOR desejado: ')
           for funcionario in lista_funcionario:
            if funcionario['setor'] == valor_desejado:
              print('-'*20)
              for key, value in funcionario.items():
                print('{}: {} '.format(key, value))
              print('-'*20)
        elif opcao_consultar == '4':                                           # Opção para voltar ao menu inicial
            return
        else:
            print('Opção Invalida! Tente novamente.')
            continue                                                           # Volta para o início do laço
    print('~~'*25)

    # ----------Fim da função CONSULTAR funcionários. ----------

    # ----------Inicio da função REMOVER funcionários. ----------

def remover_funcionario():
    print('~~'*25)
    print('Você optou por REMOVER um funcionário')
    opcao_remover = int(input('Digite o código de cadastro do funcionário que deseja remover. \n'+
                                  '>>'))
    print('~~' * 25)
    for funcionario in lista_funcionario:
        if funcionario['codigo'] == opcao_remover:
            lista_funcionario.remove(funcionario)
            print('Cadastro de funcionário removido')
    print('~~'*25)

# ----------Fim da função REMOVER funcionários. ----------

# ----------Inicio do Programa Principal: ----------

print('~~'*35)
print('   Bem vindo ao controle de funcionários de Rayane Cristina Gaspar')          #Programa principal que aparecerá para o usuário interagir
print('~~' * 35)

while True:
    cadastro_principal = input(' \n Escolha a opção desejada: \n' +                    #Laço de repetição para o programa principal rodas até que seja encerrado pelo usuario.
                               ' 1: Cadastrar um novo funcionário. \n' +
                               ' 2: Consultar um funcionário \n' +
                               ' 3: Remover um funcionário \n' +
                               ' 4: Sair/Encerrar \n' +
                               '>>')
    if cadastro_principal == '1':
        codigo_funcionario = codigo_funcionario + 1
        cadastrar_funcionario(codigo_funcionario)
    elif cadastro_principal == '2':
        consultar_funcionario()
    elif cadastro_principal == '3':
        remover_funcionario()
    elif cadastro_principal == '4':
        break

    # ----------Fim do Programa Principal: ----------

