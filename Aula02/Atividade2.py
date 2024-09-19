numero = float(input('Informe o número: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'{antecessor} {numero} {sucessor}')

dobro = 2 * numero
triplo = 3 * numero
quadrado = numero ** 2

print(f'Seu número é {numero}, o dobro dele corresponde a {dobro}, o triplo a {triplo} e seu quadrado vale {quadrado}')

nota_teste = float(input('Informe a nota do teste: '))
nota_prova = float(input('Informe a nota da prova: '))

media = (nota_teste + nota_prova) / 2

print(f'A média das suas avaliações é igual a {media}')