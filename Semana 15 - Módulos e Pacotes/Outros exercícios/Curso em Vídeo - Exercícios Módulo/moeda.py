#Definindo o módulo de onde serão importadas as funções pelos programas principais "main"
#Funções pedidas: aumentar(), diminuir(), dobro() e metade() | moeda() | resumo()

def metade(n=0, format=False):
    metade = n/2
    if not format:
        return metade
    else:
        return moeda(metade)

def dobro(n=0, format=False):
    dobro = n*2
    if not format:
        return dobro
    else:
        return moeda(dobro)

def aumentar(n =0, p=0, format=False):
    aumento = n + (n * (p/100))
    if not format:
        return aumento
    else:
        return moeda(aumento)

def reduzir(n=0, p=0, format=False):
    diminuido = n - (n * (p/100))
    if not format:
        return diminuido
    else:
        return moeda(diminuido)

def moeda(n=0, moeda='R$'):
    return f'{moeda} {n:.2f}'.replace('.',',')

def resumo(n=0, aumento=10, reducao=5):
    print('-' * 34)
    print('RESUMO DO VALOR'.center(34))
    print('-' * 34)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumento}% maior é: \t\t{aumentar(n,aumento,True)}')
    print(f'{reducao}% de desconto é: \t{reduzir(n,reducao,True)}')
    print('-' * 34)