#Programa principal do exercício 1

#Importando o módulo moeda criado
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade do preço {p} é {moeda.metade(p)}')
print(f'O dobro do preço {p} é {moeda.dobro(p)}')
print(f'O preço {p} aumentado em 10% é {moeda.aumentar(p, 10)} ')
print(f'O preço {p} reduzido em 13% é {moeda.reduzir(p, 13)}')