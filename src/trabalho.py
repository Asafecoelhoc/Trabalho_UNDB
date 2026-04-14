senha = 123
login = 'admin'
contador_tentativas = usarios_cadastrados = 0
login_usuario = str(input('Login: '))
senha_usuario = int(input('Senha: '))
produtos = usuarios = []
while senha_usuario != senha and login_usuario != login:
    print('Login ou senha incorretos. Tente novamente.')
    login_usuario = str(input('Login: '))
    senha_usuario = int(input('Senha: '))
    contador_tentativas += 1
    usarios_cadastrados += 1 
print('Cadastro bem-sucedido!')
print('Escolha uma opção:')
print('''    [1] Cadastrar Produto
    [2] Editar Produto
    [3] Excluir Produto
    [4] Cadastrar Usuário
    [5] Sair''')
opcao_escolhida = int(input('Opção escolhida: '))
print('-' * 34)

if opcao_escolhida == 1:
    print('Opção escolhida: Cadastrar Produto')
    produto_codigo = int(input('Código do produto: '))
    produto_nome = str(input('Nome do produto: '))
    produtos.append(produto_nome)
    produto_categoria = str(input('Categoria do produto: '))
    produto_quantidade = int(input('Quantidade do produto: '))
    produto_preco = float(input('Preço do produto: R$ '))        
elif opcao_escolhida == 2:
    print('Opção escolhida: Editar Produto')
    produto_codigo = int(input('Código do produto: '))
    produto_nome = str(input('Nome do produto: '))
    produto_categoria = str(input('Categoria do produto: '))
    produto_quantidade = int(input('Quantidade do produto: '))
    produto_preco = float(input('Preço do produto: R$ '))
elif opcao_escolhida == 3:
    print('Opção escolhida: Excluir Produto')
    print(f'Produtos cadastrados: {produtos}')
    excluir = str(input('Digite o nome do produto que deseja excluir: '))
    produtos.remove(excluir)
    print(f'Produto {excluir} excluído com sucesso!')
elif opcao_escolhida == 4:
    print('Opção escolhida: Cadastrar Usuário')
    login_novousuario = str(input('Login: '))
    senha_novousuario = int(input('Senha: '))
    codigo_usuario = int(input('Código: '))
    contador_tentativas += 1
    usarios_cadastrados += 1 
    print('Cadastro bem-sucedido!')
elif opcao_escolhida == 5:
    print('Opção escolhida: Sair')
    print('Saindo do programa...')