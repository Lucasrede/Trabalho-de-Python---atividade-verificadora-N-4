#Parte 2 -Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

'''
def valorPagamento(p,da):
   if (da > 0):        
     multa=p*0.03        
     juro=p*(0.001*da)        
     valorApagar=p+multa+juro
   else:       
     valorApagar=p    
     return valorApagar
total=0
while True:    
  p=float(input("Digite o valor da prestação (PARA SAIR TECLE 0 (zero)!!): "))    
  if (p==0):        
    break
    da=int(input("Digite o número de dias em atraso: "))    
    presta=valorPagamento(p,da)    
    total+=presta
    print("O valor a ser pago é: %.2f"%presta)
  print("O total de prestações pagas no dia é: %.2f"%total,"\n\n***Fim do programa***")
'''

#Parte 1 - Faça um programa com uma função chamada somaImposto( ). A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função deverá "alterar" o valor de custo para incluir o imposto sobre vendas.

'''def somaImposto(taxaImposto,custo):
  trat = float(taxaImposto/100)
  resultado=(trat*custo) + custo
  return resultado
  '''


