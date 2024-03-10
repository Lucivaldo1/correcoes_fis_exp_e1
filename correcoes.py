import numpy as np

from scipy import stats

import os

#teoria do desvio maximo
class Estatistica: 

    def teoria_Desvio_Maximo_Soma(mediaA, desvioA, mediaB, desvioB):
    
        soma = mediaA + mediaB

        desvio = desvioA + desvioB

        return f'{soma} \pm {desvio}'

    def teoria_Desvio_Maximo_Subtracao(mediaA, desvioA, mediaB, desvioB):
    
        subtracao = mediaA - mediaB

        desvio = desvioA + desvioB

        return f'{subtracao} \pm {desvio}'

    def teoria_Desvio_Maximo_Produto(mediaA, desvioA, mediaB, desvioB):
        
        produto = mediaA * mediaB

        desvio = produto * (np.abs(desvioA/mediaA) + np.abs(desvioB/mediaB))

        return f'{produto} \ pm {desvio}'

    def teoria_Desvio_Maximo_Divisao(mediaA, desvioA, mediaB, desvioB):

        divisao = mediaA / mediaB

        desvio = divisao * (np.abs(desvioA/mediaA) + np.abs(desvioB/mediaB))

        return f'{divisao} \pm {desvio}'

    #teoria do desvio padrao
        
    def teoria_Desvio_Padrao_Soma(mediaA, desvioA, mediaB, desvioB):

        soma = mediaA + mediaB

        desvio = np.sqrt((desvioA**2) + (desvioB**2))

        return f'{soma}, \pm {desvio}'
        

    def teoria_Desvio_Padrao_Subtracao(mediaA, desvioA, mediaB, desvioB):

        subtracao = mediaA - mediaB

        desvio = np.sqrt((desvioA**2) + (desvioB**2))

        return f'{subtracao}, \pm {desvio}'

    def teoria_Desvio_Padrao_Produto(mediaA, desvioA, mediaB, desvioB):

        produto = mediaA * mediaB

        desvio = produto * np.sqrt( (desvioA/mediaA)**2 + (desvioB/mediaB)**2 )

        return f'{produto} \pm {desvio}'

    def teoria_Desvio_Padrao_Divisao(mediaA, desvioA, mediaB, desvioB):

        divisao = mediaA / mediaB

        desvio = divisao * np.sqrt( (desvioA/mediaA)**2 + (desvioB/mediaB)**2 )

        return f'{divisao} \pm {desvio}'
    #estatística geral

    def desvioPadraoDaMedia(dados):
    
        desvio = stats.tstd(dados)/ (np.sqrt(len(dados)))

        return desvio


#Atividades

def atividade1():

    '''
    --------- Gabarito da primeira atividade ---------
    1]
        a) 2
        b) 3
        c) 5 
        d) 3 
        e) 3 (o último zero da medida é devido à notação explícita, critério da meia unidade- não é algarismo significativo)
    2]
        A = 23,17 (3+1 = 4 alg. sig.)
        B = 12,21
        C = -7,51
        D = 0,238
    3]
        a) 24,14 (3+1 = 4 alg. sig.)
        b) 4,169
    4]
        a) A = 8,15912*10^2  e B = 3,453*10^2 (a forma implícita implica na representação da leitura na ordem das unidades)
        b) A = (8,159120 \pm 0,000005) * 10^2 e B = (3,4530 \pm 0,0005) * 10^2
        c) 5
    5]
        A = 5,22 * 10^5
        B = 28,10 * 10^3
        C = 13 * 10^2
        D = 426,68 * 10^4
        E = - 0,3

    '''

    q1 = int(input('Digite o número de erros da primeira questão: '))

    q2 = int(input('Digite o número de erros da segunda questão: '))

    q3 = int(input('Digite o número de erros da terceira questão: '))

    q4 = int(input('Digite o número de erros da quarta questão: '))

    q5 = int(input('Digite o número de erros da quinta questão: '))

    return 10 - (q1*0.4 + q2*0.5 + q3*1 + q4*(2/3) + q5*0.4)

def atividade2():

    '''
    --------- Gabarito da segunda atividade ---------
    1]
        Vv = 31.3949 \pm 0.0014
        Vi = 31.3949 \pm 0.0010

    2]
        Vv = 49.952 \pm 0.014
        Vi = 49.95 \pm 0.09
    3]
        Vv = 11.309 \pm 0.005
        Vi = 11.309 \pm 0.013
    4]
        Vv = 13.220 \pm 0.013
        Vi = 13.220 \pm 0.029 
    5]
        35.11 \pm 0.20

    '''
    q1 = int(input('Digite o número de erros da primeira questão: '))

    q2 = int(input('Digite o número de erros da segunda questão: '))

    q3 = int(input('Digite o número de erros da terceira questão: '))

    q4 = int(input('Digite o número de erros da quarta questão: '))

    q5 = int(input('Digite o número de erros da quinta questão: '))

    return 10 - (q1*0.5 + q2*0.5 + q3*0.5 + q4*0.5 + q5*1)

#Experimentos

def atividade3():
    '''
    --------- Gabarito da terceira atividade ---------

    questões p/ casa:

    0]

    t.d.p.: 1587.2 \pm 116.46252616185174

    t.d.m.: 6.845528455284553 \pm 0.5859607376561571

    t.d.m.: 0.503655E+02 \pm 0,756
    
    1]
        a) t.d.p = 0.32469E+02 \pm 0.10757E+01
            t.d.m = 0.32469E+02 \pm 0.15145E+01

        b) t.d.p = 0.444825E+02 \pm 0.161053E+01
            t.d.m = 0.444825E+02 \pm 0.272424E+01
    2]
        a)  t.d.p.: S = 0.36700E+02 \pm 0.25099E+01
            t.d.m.: S = 0.36700E+02 \pm 0.34000E+01
        
        b) t.d.p.: D = 0.1087E+03 \pm 0.94831E+01
           t.d.m.: D = 0.1087E+03 \pm 0.1150E+02
    3]
        t.d.p.: S = 0.1384E+02 \pm 0.1675E+01
        t.d.m.: S = 0.1384E+02 \pm 0.2132E+01
    4]
        t.d.m.: V = 7.9 \pm 0.8

    5]
        I = (61281 + 0,6 * 10^3) gcm^2

    '''
    q0 = int(input('Digite o número de erros da questão zero: '))

    q1 = int(input('Digite o número de erros da primeira questão: '))

    q2 = int(input('Digite o número de erros da segunda questão: '))

    q3 = int(input('Digite o número de erros da terceira questão: '))

    q4 = int(input('Digite o número de erros da quarta questão: '))

    q5 = int(input('Digite o número de erros da quinta questão: '))

    return 10 - (q0*0.55 + q1*((5/3)/2) + q2*((5/3)/2) + q3*((5/3)/2) + q4*(5/3) + q5*(5/3))
   
def medidas_De_Tempo():
    g = 9.81

    tabela_IA = [10.5, 11, 15, 12.5, 13.5, 16, 15.5]

    tabela_IIA = [11.07, 11.02, 11.18, 11.30, 11.12, 11.16]

    tempos = []

    for distancia in tabela_IA:
      tempos.append(np.sqrt(((distancia/100)*2)/g))
    
    print(f'A média do tempo de reação é: {np.mean(tempos)}')

    print(f'A média do tempo do pêndulo é: {np.mean(tabela_IIA)} e o desvio padrão da média é: {Estatistica.desvioPadraoDaMedia(tabela_IIA)}')

def medidas_De_Comprimento():
    
    tabelaI = [4.3]
     #C L H
    tabelaI_desvios = [0.05]

    #cálculo do perimetro e da area da maior face do movel
    tabelaII =[57.04,31.33, 46.91] #C L H
    
    tabelaII_desvios = [0.04, 0.04, 0.04]
    #perimetro soma 2 * (C + H)

    tabelaIII = [23.57, 23.34, 23.06, 23.15, 23.51, 22.98]


    print('Perímetro: ')

    print(Estatistica.teoria_Desvio_Padrao_Soma(2*tabelaII[0], 2*tabelaII_desvios[0], 2*tabelaII[2], 2*tabelaII_desvios[2]))
    
    print('Área da face maior: ')

    print(Estatistica.teoria_Desvio_Padrao_Produto(tabelaII[0], tabelaII_desvios[0], tabelaII[2], tabelaII_desvios[2]))
    #area = C * H 

    print('Tratamendo estatístico do diâmetro')

    print(f'{np.mean(tabelaIII)} \pm {Estatistica.desvioPadraoDaMedia(tabelaIII)}')

    print('Determinação da unidade U')

    print(Estatistica.teoria_Desvio_Padrao_Divisao(tabelaII[0],Estatistica.desvioPadraoDaMedia(tabelaIII), tabelaI[0], tabelaI_desvios[0]))

def main():

    continuar = 'y'
    while continuar == 'y' or continuar == 'Y':

        print(atividade2())
        continuar = input('continuar?(y/n): ')
        os.system('cls')
    
    
   
if __name__ == '__main__':
    main()