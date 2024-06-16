#criar um menu
#parte visual==============================================================================
def codigo():
    print('='*40)

    print('\033[1;49;34m{:^40}\033[m'.format('MENU PRINCIPAL'))

    print('='*40)

    print('\033[33m {} - \033[m\033[34m {} \033[m'.format('1', 'Ver pessoas cadastradas'))

    print('\033[33m {} - \033[m\033[34m {} \033[m'.format('2', 'Cadastrar novas pessoas'))

    print('\033[33m {} - \033[m\033[34m {} \033[m'.format('3', 'Sair do sistema'))

    print('='*40)

    #===========================================================================================


    #backend====================================================================================


    lista_clientes = []
    opcao_cliente = input('Sua opção: ') 
    
    if opcao_cliente == '1':
            print('='*40)
            if lista_clientes == []:
                print('\033[3;31m Não existe nehum usuário cadastrado. \033[m')
            else:
                for x in lista_clientes:
                    print(x)
                    
            print('='*40)

    elif opcao_cliente == '2':
            
            while nome != '':
                nome = input('\033[1;34m {} \033[m'.format('Nome: '))

                def erro_acesso1():
                    


                    if nome == '':
                        
                        acesso1 = input('\033[3m Deseja ver os clientes salvos? \033[m \n {:^20}? {:^20}?'.format('Sim', 'Não'))
                        if acesso1 == 'Sim':
                            codigo()
                                    
                        elif acesso1 == 'Não':
                            print('\033[3;41m Obrigado por usar nossos serviços! \033[m')
                        else:
                            print('\033[3;31m Operação inválida \033[m')
                            
                            erro_acesso1()
                           
                    
                erro_acesso1()      
              
    elif opcao_cliente == '3':
            print('\033[3;41m Obrigado por usar nossos serviços! \033[m') 
    
    # ====================================================================================
# Temos um erro com o lista_clientes.append(nome) tenta resolver hoje
codigo()