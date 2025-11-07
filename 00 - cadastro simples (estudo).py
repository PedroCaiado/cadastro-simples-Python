# Sistema de cadastro simples - para estudo (nome, idade, email)

cadastros = []

while True:
    print('\n\033[1;34m=== CADASTRO DE PESSOAS ===\033[m')

    # validação do nome (permite letras e espaços)
    while True:
        nome = input('Nome: ').strip()
        if nome.replace(' ', '').isalpha():
            break
        print('\033[1;33m⚠️  Nome inválido! Digite apenas letras (pode usar espaços).\033[m')

    # validação da idade (somente dígitos)
    while True:
        idade_txt = input('Idade: ').strip()
        if idade_txt.isdigit():
            idade = int(idade_txt)
            break
        print('\033[1;33m⚠️  Idade inválida! Digite apenas números.\033[m')

    email = input('E-mail: ').strip().lower()

    cadastros.append({'nome': nome, 'idade': idade, 'email': email})
    print('\033[1;32m✅ Cadastro realizado com sucesso!\033[m')

    continuar = input('Deseja cadastrar outra pessoa? [S/N] ').strip().upper()[:1]
    if continuar == 'N':
        break

print('\n\033[1;34m=== LISTA DE CADASTRADOS ===\033[m')
for i, reg in enumerate(cadastros, start=1):
    print('\033[1;36m{}. {} ({} anos) - {}\033[m'.format(i, reg['nome'], reg['idade'], reg['email']))

# --- Resumo final ---
qtd = len(cadastros)
if qtd > 1:
    media = sum(item['idade'] for item in cadastros) / qtd
    mais_velho = max(cadastros, key=lambda item: item['idade'])
    mais_novo  = min(cadastros, key=lambda item: item['idade'])
    print(
        '\n\033[1;35mForam cadastradas {} pessoas e a idade média entre elas é {:.1f} anos, '
        'sendo a maior idade de {}, que tem {} anos, e a menor idade de {}, que tem {} anos.\033[m'
        .format(qtd, media, mais_velho['nome'], mais_velho['idade'], mais_novo['nome'], mais_novo['idade'])
    )
elif qtd == 1:
    unico = cadastros[0]
    print('\n\033[1;35mFoi cadastrada apenas 1 pessoa: {} ({} anos).\033[m'.format(unico['nome'], unico['idade']))
else:
    print('\n\033[1;33mNenhum cadastro realizado.\033[m')

print('\n\033[1;32m👋 Fim do programa!\033[m')
