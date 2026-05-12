nome = 'MarCO'
print(nome.lower())
print(nome.upper()) 
print(nome.capitalize())
print(nome.title())
print(nome.swapcase())

texto = "   Olá, mundo!   "
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())   

menu = 'Python'
print("----" + menu + "----")
print(menu.center(20, '-'))

for letra in menu:
    print(letra, end='-')

print('-'.join(menu))

