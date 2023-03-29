import requests

print('##################')
print('## Consulta CEP ##')
print('##################')
print()

#Função que consulta o CEP e retorna as informações em uma lista
def consulta_cep(x):
    
    #Busca as informações e retorna em json
    requisicao = requests.get(f'https://viacep.com.br/ws/{x}/json/')
    resposta = requisicao.json()

    #Variáveis que guardam as informações coletadas
    pcep = ('CEP : {}'.format(resposta['cep']))
    plogradouro = ('Logradouro: {}'.format(resposta['logradouro']))
    pbairro = ('Bairro: {}'.format(resposta['bairro']))
    plocalidade = ('Cidade: {}'.format(resposta['localidade']))
    puf = ('UF: {}'.format(resposta['uf']))

    #Variavel com a string das informações coletadas
    resultado = print(f'Endereço: {plogradouro} - {pbairro}, {plocalidade} - {puf}, {pcep}')

    return resultado

chamados = True


#Comando para manter o programa rodando
while chamados:

    #Captura a intenção do usuario
    opcao = input('Escolha o que deseja executar:\n[1] - Consulta CEP\n[2] - Sair\n ')
    
    #Direciona o usuario para a opcao desejada
    if opcao == '1':
            
            #Captura o CEP para ser consultado
            cep_input = input('Digite o CEP que deseja consultar: ')
            if len(cep_input) == 8 and cep_input.isdigit:
                consulta_cep(cep_input)
            else:
                 print('CEP Inválido')
                 continue
    #Executa a opção 2 de sair
    elif opcao == '2':
         print('Até a próxima')
         chamados = False
    #Caso o valor digitado não for nem 1 nem 2     
    else:
        print('Valores Inválidos')
        continue


    



