def adicionar_contato(nome, telefone, email, favorito=False):
    contato_para_adicionar = {"nome":nome, 'telefone':telefone, 'email':email, 'favorito':favorito}
    lista_contatos.append(contato_para_adicionar)
    print('Contato adicionado com sucesso!\n')

def ver_contatos(lista_contatos):
    print('\nContatos: \n')
    for elemento in lista_contatos:
        print('Contato %s\nNome: %s\nTelefone: %s\nEmail: %s\n' % (int(lista_contatos.index(elemento)+1),elemento['nome'],elemento['telefone'],elemento['email']))

def editar_contato(lista_contatos, indice, nome, telefone, email):
    for elemento in lista_contatos:
        if int(lista_contatos.index(elemento)+1) == int(indice):
            elemento['nome']=nome
            elemento['telefone']=telefone
            elemento['email']=email
            print('Contato atualizado!\n')

def marcar_desmarcar_favorito(lista_contatos ,escolha, indice):
    for elemento in lista_contatos:
        if int(lista_contatos.index(elemento)+1) == int(indice):
            if escolha == '1':
                elemento['favorito']=True
                print('Contato favoritado!\n')
            elif escolha == '2':
                elemento['favorito']=False
                print('Contato desfavoritado!\n')
            else:
                print('Escolha invalida')

def ver_contatos_favoritos():
    exist = False
    for elemento in lista_contatos:
        if elemento['favorito']==True:
            print('Contato %s\nNome: %s\nTelefone: %s\nEmail: %s\n' % (int(lista_contatos.index(elemento)+1),elemento['nome'],elemento['telefone'],elemento['email']))
            exist = True
        if not exist:
            print('Não existe contatos favoritados\n')


def apagar_contato(lista_contatos, indice):
    for elemento in lista_contatos:
        if int(lista_contatos.index(elemento)+1) == int(indice):
           lista_contatos.remove(elemento)
    print('Contato apagado!\n')

lista_contatos = []

while True:
    print('----------------------------')
    print('1. Acionar contato')
    print('2. Ver contatos')
    print('3. Editar contatos')
    print('4. Marcar/Desmarcar favorito')
    print('5. Ver favoritos')
    print('6. Apagar contato')
    print('0. Sair')

    option = input('\nEntre com uma opção: ')
    print('----------------------------')
   
    match option:
            case '1':
                nome = input('\nEntre com o nome: ')
                telefone = input('Entre com o telefone: ')
                email = input('Entre com o email: ')
                adicionar_contato(nome, telefone, email)
            case '2':
                ver_contatos(lista_contatos)
            case '3':
                print('Qual contato deseja editar?\n')
                ver_contatos(lista_contatos)
                indice = input('Entre com o numero do contato: ')
                nome = input('Entre com o nome do contato: ')
                telefone = input('Entre com o telefone do contato: ')
                email = input('Entre com o email do contato: ')
                
                editar_contato(lista_contatos, indice, nome, telefone, email)
            case '4':
                escolha = input('Digite 1 para colocar um contato nos favoritos ou 2 para tirar dos favoritos: \n')
                ver_contatos(lista_contatos)
                indice = input('Entre com o numero do contato: \n')
                marcar_desmarcar_favorito(lista_contatos ,escolha, indice)
            case '5':
                print('\nFavoritos: ')
                ver_contatos_favoritos()
            case '6':
                ver_contatos(lista_contatos)
                indice = input('Entre com o numero do contato que deseja deletar: \n')
                apagar_contato(lista_contatos, indice)
            case '0':
                print('Saindo...')
                break
            case _:
                print('Entre com uma opção válida.')
    