class Point(object):
    #define uma classe com valores de coordenadas X e Y no plano cartesiano

    def __init__(self,x,y):
    #construtor da classe com teste se os valores sao do tipo float
        try:
            if type(x) == float and type(y) == float:
                self.X = x
                self.Y = y
            else:
                print("Wrong entry")
                
        except:
            print("Error creating a point instance.")

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    
