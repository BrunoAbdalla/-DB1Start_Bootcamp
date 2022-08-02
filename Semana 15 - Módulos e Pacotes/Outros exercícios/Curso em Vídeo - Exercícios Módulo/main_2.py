#Programa principal do exercício 2 - Com a formatação de dentro do módulo

#Importando o módulo moeda criado
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade do preço {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro do preço {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O preço {moeda.moeda(p)} aumentado em 10% é {moeda.moeda(moeda.aumentar(p, 10))} ')
print(f'O preço {moeda.moeda(p)} reduzido em 13% é {moeda.moeda(moeda.reduzir(p, 13))}')