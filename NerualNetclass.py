class Layer:
    def __init__(self,length):
        #self.nodes = [Node() for i in range(length)]
        self.length = length
        self.I = np.zeros(length)
        self.O = np.zeros(length)
        self.b = np.zeros(length)
        self.weights = []
        self.deltas = []
        return
    
class NeuralNet():
    def __init__(self,X,Y,sizeH=[2]):
        self.X = X
        self.Y = Y
        self.layers = [Layer(len(X[0]))] + [Layer(i) for i in sizeH] + [Layer(len(Y[0]))]
        self.length = len(self.layers)
        for i in range(self.length-1):
            self.layers[i].weights = [[rd.random() for j in range(self.layers[i+1].length)] for k in range(self.layers[i].length)] #MATRICE DI ADIACENZE RIGHE = LAYER 0, CLN = LAYER 1
            print()
            
    def feedfw(self,x):
        self.layers[0].O = x
        for i in range(self.length-1):
            for j in range(self.layers[i+1].length):
                self.layers[i+1].I[j] = np.dot(self.layers[i].O,np.transpose(self.layers[i].weights)[j]) + self.layers[i+1].b[j]
                self.layers[i+1].O[j] = sigmoid(self.layers[i+1].I[j])
        return self.layers[-1].O
    
    def totErrorInput(self,x,y):
        self.feedfw(x)
        Error = sum(np.square(np.subtract(y,self.layers[-1].O)))/(self.layers[-1].length*2)
        #print(Error)
        return Error
        
    def backpropagation(self,x,y,lr):
        self.feedfw(x)
        self.layers[-1].deltas = np.multiply(np.subtract(self.layers[-1].O,y),[Dsigmoid(out) for out in self.layers[-1].O])
        self.layers[-2].weights = [np.subtract(self.layers[-2].weights[j],np.multiply(lr,np.multiply(self.layers[-1].deltas,self.layers[-2].O[j]))) for j in range(self.layers[-2].length)]
        self.layers[-1].b = np.subtract(self.layers[-1].b, np.multiply(lr,self.layers[-1].deltas))
        for i in reversed(range(1,self.length-1)):
            self.layers[i].deltas = [np.dot(self.layers[i+1].deltas,self.layers[i].weights[j])*Dsigmoid(self.layers[i].O[j]) for j in range(self.layers[i].length)]
            self.layers[i-1].weights = [np.subtract(self.layers[i-1].weights[j],np.multiply(lr,np.multiply(self.layers[i].deltas,self.layers[i-1].O))) for j in range(self.layers[i-1].length)]
            self.layers[i].b = np.subtract(self.layers[i].b,np.multiply(lr,self.layers[i].deltas))
            
    def train(self,lr):
        for epoch in range(1000):
            totError = 0
            for i in range(len(self.X)):
                self.backpropagation(self.X[i],self.Y[i],lr)
                totError += self.totErrorInput(self.X[i],self.Y[i])
            if totError < 0.2:
                return
                
    def debug(self):
        for layer in self.layers:
            print(layer.O)
            print(layer.weights,"\n")
