
frase = str(input('escreva uma frase: ')).strip().upper()
# eliminamos os espaços antes e depois com o strip,
# colocamos tudo para maiusculo com upper.
palavras = frase.split() #gerou uma lista
tjunto = ''.join(palavras) # juntou tudo para eliminar os espaços da lista
inverso = ''
#inverso = [::-1] \ sem o uso do for
for letra in range(len(tjunto) -1, -1, -1): # criei ela invertida
    inverso += tjunto[letra]
print(tjunto, inverso)
if inverso == tjunto: # coloquei em condições
    print('temos um palindromo!')
else:
    print('sua frase não é um palindromo!')
