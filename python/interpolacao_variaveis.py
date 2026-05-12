nome = 'Marco'
idade = 23
profissao = 'Analista de Dados'
linguagem = 'Python'
pessoa = {'nome': nome, 'idade': idade, 'profissao': profissao, 'linguagem': linguagem}

print('Olá, me chamo %s, tenho %d anos, trabalho como %s e estou aprendendo %s.' % (nome, idade, profissao, linguagem))

print('Olá, me chamo {}, tenho {} anos, trabalho como {} e estou aprendendo {}.'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {0}, tenho {1} anos, trabalho como {2} e estou aprendendo {3}.'.format(nome, idade, profissao, linguagem))

print('Olá, me chamo {nome}, tenho {idade} anos, trabalho como {profissao} e estou aprendendo {linguagem}.'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print('Olá, me chamo {nome}, tenho {idade} anos, trabalho como {profissao} e estou aprendendo {linguagem}.'.format(**pessoa))

print(f'Olá, me chamo {nome}, tenho {idade} anos, trabalho como {profissao} e estou aprendendo {linguagem}.')

PI = 3.14159
print(f'O valor de PI é aproximadamente {PI:.2f}.')

