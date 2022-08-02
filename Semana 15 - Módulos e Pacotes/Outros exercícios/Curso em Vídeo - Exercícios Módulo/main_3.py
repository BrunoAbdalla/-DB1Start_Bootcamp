#Programa principal do exercício 3 - Com a formatação de dentro do módulo e as funções de cálculos terem a opção de se formatarem sozinhas

#Importando o módulo moeda criado
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade do preço {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro do preço {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'O preço {moeda.moeda(p)} aumentado em 10% é {moeda.aumentar(p, 10, True)} ')
print(f'O preço {moeda.moeda(p)} reduzido em 13% é {moeda.reduzir(p, 13, True)}')