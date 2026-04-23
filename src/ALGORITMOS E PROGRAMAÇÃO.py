# ============================================================
# SISTEMA DE CONTROLE DE ESTOQUE - ARTIGOS ESPORTIVOS
# ============================================================

# --- CONSTANTES POR CATEGORIA (mínimo e máximo em estoque) ---
CATEGORIA_1 = 'Calcados'
ESTOQUE_MIN_CALCADOS = 5
ESTOQUE_MAX_CALCADOS = 100

CATEGORIA_2 = 'Roupas'
ESTOQUE_MIN_ROUPAS = 10
ESTOQUE_MAX_ROUPAS = 200

CATEGORIA_3 = 'Equipamentos'
ESTOQUE_MIN_EQUIPAMENTOS = 3
ESTOQUE_MAX_EQUIPAMENTOS = 50

# --- DADOS INICIAIS ---
# Produtos armazenados como lista de listas: [codigo, nome, categoria, quantidade, preco]
produtos = []

# Usuários armazenados como lista de listas: [codigo, nome, senha]
usuarios = [[1, 'admin', 123]]

usuario_logado = ''

# ============================================================
# LOGIN
# ============================================================
MAX_TENTATIVAS = 3
contador_tentativas = 0
logado = False

print('=' * 44)
print('     SISTEMA DE CONTROLE DE ESTOQUE')
print('=' * 44)

while not logado and contador_tentativas < MAX_TENTATIVAS:
    login_usuario = input('Login: ')
    senha_usuario = int(input('Senha: '))
    contador_tentativas += 1

    for u in usuarios:
        if u[1] == login_usuario and u[2] == senha_usuario:
            logado = True
            usuario_logado = u[1]
            break

    if not logado:
        tentativas_restantes = MAX_TENTATIVAS - contador_tentativas
        if tentativas_restantes > 0:
            print(f'Login ou senha incorretos! {tentativas_restantes} tentativa(s) restante(s).')
        else:
            print('Número máximo de tentativas atingido. Encerrando sistema.')

# ============================================================
# MENU PRINCIPAL
# ============================================================
if logado:
    print(f'\nBem-vindo, {usuario_logado}!')
    opcao_escolhida = 0

    while opcao_escolhida != 5:

        # --- Cálculo do estoque total e por categoria ---
        total_quantidade = 0
        total_valor = 0.0
        qtd_calcados = 0
        qtd_roupas = 0
        qtd_equipamentos = 0

        for p in produtos:
            total_quantidade += p[3]
            total_valor += p[3] * p[4]
            if p[2] == CATEGORIA_1:
                qtd_calcados += p[3]
            elif p[2] == CATEGORIA_2:
                qtd_roupas += p[3]
            elif p[2] == CATEGORIA_3:
                qtd_equipamentos += p[3]

        # --- Cálculo das porcentagens ---
        if total_quantidade > 0:
            pct_calcados = qtd_calcados / total_quantidade * 100
            pct_roupas = qtd_roupas / total_quantidade * 100
            pct_equipamentos = qtd_equipamentos / total_quantidade * 100
        else:
            pct_calcados = pct_roupas = pct_equipamentos = 0.0

        # --- Exibição do painel de status ---
        print('\n' + '=' * 44)
        print(f'  Usuário logado: {usuario_logado}')
        print(f'  Total em estoque: {total_quantidade} un. | R$ {total_valor:.2f}')
        print('  Estoque por categoria:')
        print(f'    {CATEGORIA_1:<14}: {qtd_calcados:>3} un. ({pct_calcados:>5.1f}%) | Min:{ESTOQUE_MIN_CALCADOS} Max:{ESTOQUE_MAX_CALCADOS}')
        print(f'    {CATEGORIA_2:<14}: {qtd_roupas:>3} un. ({pct_roupas:>5.1f}%) | Min:{ESTOQUE_MIN_ROUPAS} Max:{ESTOQUE_MAX_ROUPAS}')
        print(f'    {CATEGORIA_3:<14}: {qtd_equipamentos:>3} un. ({pct_equipamentos:>5.1f}%) | Min:{ESTOQUE_MIN_EQUIPAMENTOS} Max:{ESTOQUE_MAX_EQUIPAMENTOS}')
        print('=' * 44)

        print('\n  [1] Cadastrar Produto')
        print('  [2] Editar Produto')
        print('  [3] Excluir Produto')
        print('  [4] Cadastrar Usuário')
        print('  [5] Sair')
        opcao_escolhida = int(input('Opção: '))
        print('-' * 44)

        # --------------------------------------------------
        # OPÇÃO 1 - CADASTRAR PRODUTO
        # --------------------------------------------------
        if opcao_escolhida == 1:
            print('>>> Cadastrar Produto')
            produto_codigo = int(input('Código: '))

            codigo_existe = False
            for p in produtos:
                if p[0] == produto_codigo:
                    codigo_existe = True
                    break

            if codigo_existe:
                print('Erro: código já cadastrado!')
            else:
                produto_nome = input('Nome: ')
                print(f'Categorias disponíveis: {CATEGORIA_1} | {CATEGORIA_2} | {CATEGORIA_3}')
                produto_categoria = input('Categoria: ')

                categoria_valida = False
                if produto_categoria == CATEGORIA_1 or produto_categoria == CATEGORIA_2 or produto_categoria == CATEGORIA_3:
                    categoria_valida = True

                if not categoria_valida:
                    print('Categoria inválida!')
                else:
                    produto_quantidade = int(input('Quantidade: '))
                    produto_preco = float(input('Preço: R$ '))
                    produtos.append([produto_codigo, produto_nome, produto_categoria, produto_quantidade, produto_preco])
                    print(f'Produto "{produto_nome}" cadastrado com sucesso!')

        # --------------------------------------------------
        # OPÇÃO 2 - EDITAR PRODUTO
        # --------------------------------------------------
        elif opcao_escolhida == 2:
            print('>>> Editar Produto')
            if len(produtos) == 0:
                print('Nenhum produto cadastrado.')
            else:
                print('Produtos cadastrados:')
                for p in produtos:
                    print(f'  [{p[0]}] {p[1]} | {p[2]} | {p[3]} un. | R$ {p[4]:.2f}')

                produto_codigo = int(input('Código do produto a editar: '))
                encontrado = False
                indice = 0

                for i in range(len(produtos)):
                    if produtos[i][0] == produto_codigo:
                        encontrado = True
                        indice = i
                        break

                if not encontrado:
                    print('Produto não encontrado!')
                else:
                    print(f'Editando: {produtos[indice][1]} (deixe em branco para manter)')
                    novo_nome = input(f'Novo nome [{produtos[indice][1]}]: ')
                    print(f'Categorias: {CATEGORIA_1} | {CATEGORIA_2} | {CATEGORIA_3}')
                    nova_categoria = input(f'Nova categoria [{produtos[indice][2]}]: ')
                    nova_quantidade = input(f'Nova quantidade [{produtos[indice][3]}]: ')
                    novo_preco = input(f'Novo preço [{produtos[indice][4]:.2f}]: R$ ')

                    if novo_nome != '':
                        produtos[indice][1] = novo_nome
                    if nova_categoria == CATEGORIA_1 or nova_categoria == CATEGORIA_2 or nova_categoria == CATEGORIA_3:
                        produtos[indice][2] = nova_categoria
                    if nova_quantidade != '':
                        produtos[indice][3] = int(nova_quantidade)
                    if novo_preco != '':
                        produtos[indice][4] = float(novo_preco)

                    print('Produto editado com sucesso!')

        # --------------------------------------------------
        # OPÇÃO 3 - EXCLUIR PRODUTO
        # --------------------------------------------------
        elif opcao_escolhida == 3:
            print('>>> Excluir Produto')
            if len(produtos) == 0:
                print('Nenhum produto cadastrado.')
            else:
                print('Produtos cadastrados:')
                for p in produtos:
                    print(f'  [{p[0]}] {p[1]} | {p[2]} | {p[3]} un. | R$ {p[4]:.2f}')

                produto_codigo = int(input('Código do produto a excluir: '))
                encontrado = False
                indice = 0

                for i in range(len(produtos)):
                    if produtos[i][0] == produto_codigo:
                        encontrado = True
                        indice = i
                        break

                if not encontrado:
                    print('Produto não encontrado!')
                else:
                    print(f'Produto "{produtos[indice][1]}" excluído com sucesso!')
                    produtos.pop(indice)

        # --------------------------------------------------
        # OPÇÃO 4 - CADASTRAR USUÁRIO
        # --------------------------------------------------
        elif opcao_escolhida == 4:
            print('>>> Cadastrar Usuário')
            novo_codigo = int(input('Código: '))

            codigo_existe = False
            for u in usuarios:
                if u[0] == novo_codigo:
                    codigo_existe = True
                    break

            if codigo_existe:
                print('Erro: código já cadastrado!')
            else:
                novo_nome = input('Nome: ')
                nova_senha = int(input('Senha: '))
                usuarios.append([novo_codigo, novo_nome, nova_senha])
                print(f'Usuário "{novo_nome}" cadastrado com sucesso!')

        # --------------------------------------------------
        # OPÇÃO 5 - SAIR
        # --------------------------------------------------
        elif opcao_escolhida == 5:
            print('Saindo do sistema. Até logo!')

        else:
            print('Opção inválida! Tente novamente.')