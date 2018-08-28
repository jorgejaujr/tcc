#lasse que descreve o objeto 
import point
import matplotlib.pyplot as plt
#classe de interpolador, que contem os metodos de interpolacao linear e polinomial (metodo de Lagrange)
from interpolator import *

#conjunto de pontos iniciais
p3 = point.Point(3.0,4.0)
p2 = point.Point(2.0,3.0)
p1 = point.Point(1.0,2.0)

#vetor de pontos
conjunto = [p1,p2,p3]

#criacao de uma instancia de vetor de pontos
interp = Interpolator(conjunto)

#novo conjunto com a interpolacao linear

conjuntoLinear = interp.linearInterpolation(0.5)

#criacao artificial de novos pontos usando interpolacao polinomial
for i in range (4, 10):

    pi = point.Point(float(i),interp.lagrangeInterpolation(float(i)))
    conjunto.append(pi)

#vetores para armazenar os valores de x e f(x) de cada ponto para criar grafico
#usando o matplotlib
listaX = []
listaY = []

listaXlin = []
listaYlin = []

#insercao dos valores de x e f(x) da interpolacao polinomial nos vetores auxiliares
for elemento in range(0,len(conjunto)):
    listaX.append(conjunto[elemento].getX())
    listaY.append(conjunto[elemento].getY())
    #impressao para simples conferencia - interpolacao polinomial
    print("Polinomial: ",conjunto[elemento].getX()," ",conjunto[elemento].getY())

#insercao dos valores de x e f(x) da interpolacao linear nos vetores auxiliares
for elemento in range(0,len(conjuntoLinear)):
    listaXlin.append(conjuntoLinear[elemento].getX())
    listaYlin.append(conjuntoLinear[elemento].getY())
    #impressao para simples conferencia - interpolacao linear
    print("Linear: ",conjuntoLinear[elemento].getX()," ",conjuntoLinear[elemento].getY())

#criacao do plot de interpolacao linear
#tracejado azul
plt.plot(listaXlin,listaYlin,'b--')
#criacao do grafico usando os vetores dos valores de x e f(x)
#circulos vermelhos
plt.plot(listaX,listaY,'ro')
#criacao dos eixos
plt.axis([0,10,0,10])
#exibicao do grafico de pontos
plt.show()
    
