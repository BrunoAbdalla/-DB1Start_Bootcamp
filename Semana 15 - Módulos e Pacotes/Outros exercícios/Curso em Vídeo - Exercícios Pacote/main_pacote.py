#Programa principal dos exercícios de Pacote

#Importando o módulo moeda criado
from UtilidadesCeV import Moeda
from UtilidadesCeV import Dado

p = Dado.LerDinheiro('Digite um valor: R$')
Moeda.resumo(p)
