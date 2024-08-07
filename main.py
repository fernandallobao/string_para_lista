# #pega a string de uma veriavel e transforma em uma lista
# nome = 'Joao Corno'

# nome_completo = nome.split(' ') #nome_completo é uma lista

# for parte in nome_completo:
#     print(parte, end=' ')#end='oq vc quer no lugar da quebra de linha' elimina a quebra de linha 'oq vc quer no lugar da quebra de linha'

# print(nome_completo)

#OUTRA FORMA DE FAZER   
nome = input('Informe o nome: ')

#separa as palavras do nome
nome_completo = nome.split(' ')

#capitular as palavras do nome
for i in range(len(nome_completo)):
    nome_completo[i] = nome_completo[i].capitalize()
    
#junta o nome em uma variavel
nome_completo = ' '.join(nome_completo)

print(nome_completo)