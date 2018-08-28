from point import *

class Interpolator(object):
    #construtor da classe sempre recebe uma lista
    def __init__(self,entryList):
        try:
            self.aList = entryList
        except:
            print("Error creating object")
            
    #definindo metodo de interpolacao linear
    #Neste metodo o interpolador usa a lista passada e gera os pontos interpolados dado o passo
    def linearInterpolation(self,step):
    
        #criando lista paralela para acrescentar pontos
        outputList = []
        for element in range(0,len(self.aList)):
            outputList.append(self.aList[element])

        #pegando cada elemento e inserindo na lista de saida
        for i in range(0,len(self.aList)-1):
            
                
                #pegando dois elementos subsequentes da lista
                element1=self.aList[i]
                element2=self.aList[i+1]
                
                #calculo do denominador X1-X0
                denominator = element2.getX()-element1.getX()
                
                #calculo numerador X-X0
                numerator = (element1.getX()+step)-element1.getX()

                #calcula razao entre numerador e denominador
                ratio = numerator/denominator
                
                #calculando o valor Ydesejad0 = Y0*(1- (X-X0)/(X1-X0))+Y1*((X-X0)/(X1-X0)) 
                intermediateElementY = element1.getY()*(1-ratio)+element2.getY()*ratio

                #cria um objeto do tipo Ponto
                interpolatedPoint = Point(element1.getX()+step,intermediateElementY)

                #insere o objeto entre os pontos
                outputList.append(interpolatedPoint)
        return outputList
            
        
    #definicao do metodo de interpolacao polinomial pelo metodo de lagrange
    #Neste metodo o interpolador retorna o valor do f(x) interpolado
    def lagrangeInterpolation(self,xdado):
        #inicializando o valor de y interpolado
        yinterpolated = 0
        #calculo do y
        for i in range(0,len(self.aList)):
            #pega o valor de f(x) da curva de cada ponto, menos o que quero calcular
            termo = self.aList[i].getY()
            
            #calculo do coeficiente de lagrange para cada ponto
            for j in range(0,len(self.aList)):
                
                if i!=j:
                    #multiplico o valor de f(x) pelo coeficiente de Lagrange do ponto
                    termo = termo*(xdado-self.aList[j].getX()) / (self.aList[i].getX() - self.aList[j].getX())
                #ignoro os pontos com i e j iguais
                elif i==0:
                    pass
            #somo o valor dos produtos de f(x) com os coeficientes de Lagrange para gerar o f(x) desejado
            yinterpolated+=termo
        #retorno o valor de f(x)
        return yinterpolated
    
