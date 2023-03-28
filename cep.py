import requests

print('##################')
print('## Consulta CEP ##')
print('##################')
print()

chamados = True

while chamados:
    cep_input = input('Digite o CEP para a consulta: ')
    if len(cep_input) == 8 and cep_input.isdigit:
        requisicao = requests.get(f'https://viacep.com.br/ws/{cep_input}/json/')
        endereco = requisicao.json()
        pcep = ('CEP : {}'.format(endereco['cep']))
        plogradouro = ('Logradouro: {}'.format(endereco['logradouro']))
        pbairro = ('Bairro: {}'.format(endereco['bairro']))
        plocalidade = ('Cidade: {}'.format(endereco['localidade']))
        puf = ('UF: {}'.format(endereco['uf']))
        print(f'{plogradouro} - {pbairro}, {plocalidade} - {puf}, {pcep}')
    else:
        print('CEP Inválido')
        chamados = False





    



