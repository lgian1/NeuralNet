class Layer:
    def __init__(self,length):
        #self.nodes = [Node() for i in range(length)]
        self.length = length
        self.I = np.zeros(length)
        self.O = np.zeros(length)
        self.b = np.zeros(length)
        self.weights = []
        self.dElayers = []
        self.Delta = []
        return
    
class NeuralNet():
    def __init__(self,X,Y,sizeH=[2]):
        self.layers = [Layer(len(X[0]))] + [Layer(i) for i in sizeH] + [Layer(len(Y[0]))]
        self.length = len(self.layers)
        for i in range(self.length-1):
            self.layers[i].weights = [[rd.random() for j in range(self.layers[i+1].length)] for k in range(self.layers[i].length)] #MATRICE DI ADIACENZE RIGHE = LAYER 0, CLN = LAYER 1
        return 
    
    def feedfw(self,x):
        self.layers[0].O = x
        for i in range(self.length-1):
            for j in range(self.layers[i+1].length):
                self.layers[i+1].I[j] = np.dot(self.layers[i].O,np.transpose(self.layers[i].weights)[j]) + self.layers[i+1].b[j]
                self.layers[i+1].O[j] = sigmoid(self.layers[i+1].I[j])
                
    def totError(self,x,y):
        self.feedfw(x)class Layer:
    def __init__(self,length):
        #self.nodes = [Node() for i in range(length)]
        self.length = length
        self.I = np.zeros(length)
        self.O = np.zeros(length)
        self.b = np.zeros(length)
        self.weights = []
        self.dElayers = []
        self.Delta = []
        return
    
class NeuralNet():
    def __init__(self,X,Y,sizeH=[2]):
        self.layers = [Layer(len(X[0]))] + [Layer(i) for i in sizeH] + [Layer(len(Y[0]))]
        self.length = len(self.layers)
        for i in range(self.length-1):
            self.layers[i].weights = [[rd.random() for j in range(self.layers[i+1].length)] for k in range(self.layers[i].length)] #MATRICE DI ADIACENZE RIGHE = LAYER 0, CLN = LAYER 1
        return 
    
    def feedfw(self,x):
        self.layers[0].O = x
        for i in range(self.length-1):
            for j in range(self.layers[i+1].length):
                self.layers[i+1].I[j] = np.dot(self.layers[i].O,np.transpose(self.layers[i].weights)[j]) + self.layers[i+1].b[j]
                self.layers[i+1].O[j] = sigmoid(self.layers[i+1].I[j])
                
    def totError(self,x,y):
        self.feedfw(x)
        Error = sum(np.square(np.subtract(y,self.layers[-1].O)))/(self.layers[-1].length*2)
        print(Error)
        
    def backpropagation(self,x,y,lr):
        self.feedfw(x)
        self.layers[-1].Delta = [ (self.layers[-1].O[i]*(1- self.layers[-1].O[i])*(self.layers[-1].O[i]-y[i])) for i in range (self.layers[-1].length)]
        #self.layers[-1].Delta = np.dot(np.dot(self.layers[-1].O,np.subtract(1,self.layers[-1].O)),np.subtract(self.layers[-1].O,y))  np.multiply
        for i in reversed(range (1,self.length)):
            for n in range( self.layers[i+1]):
                self.layers[i].weights[n] = np.subtract(self.layers[i].weights[n],lr*self.layers[i-1].O[n]*self.layers[i].Delta)
            self.layers[i-1].Delta= [(self.layers[i-1].O[k]*(1-self.layers[i-1].O[k])*np.dot(self.layers[i].Delta,self.layers[i].weights[k])) for k in range( self.layers[i-1].length)]
            
    
    def debug(self):
        for layer in self.layers:
            print(layer.O)
            print(layer.weights,"\n")

        Error = sum(np.square(np.subtract(y,self.layers[-1].O)))/(self.layers[-1].length*2)
        print(Error)
        
    def backpropagation(self,x,y,lr):
        self.feedfw(x)
        self.layers[-1].Delta = [ (self.layers[-1].O[i]*(1- self.layers[-1].O[i])*(self.layers[-1].O[i]-y[i])) for i in range (self.layers[-1].length)]
        #self.layers[-1].Delta = np.dot(np.dot(self.layers[-1].O,np.subtract(1,self.layers[-1].O)),np.subtract(self.layers[-1].O,y))  np.multiply
        for i in reversed(range (1,self.length)):
            for n in range( self.layers[i+1]):
                self.layers[i].weights[n] = np.subtract(self.layers[i].weights[n],lr*self.layers[i-1].O[n]*self.layers[i].Delta)
            self.layers[i-1].Delta= [(self.layers[i-1].O[k]*(1-self.layers[i-1].O[k])*np.dot(self.layers[i].Delta,self.layers[i].weights[k])) for k in range( self.layers[i-1].length)]
            
    
    def debug(self):
        for layer in self.layers:
            print(layer.O)
            print(layer.weights,"\n")
