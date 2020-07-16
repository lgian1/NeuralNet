import math as mt, numpy as np, matplotlib.pyplot as plt, random as rd


def sigmoid(x):
    return 1/(1+mt.exp(-x))


def Dsigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))


class Layer:
    def __init__(self, lenght):
        # self.nodes = [Node() for i in range(lenght)]
        self.lenght = lenght
        self.I = np.zeros(lenght)
        self.O = np.zeros(lenght)
        self.b = np.zeros(lenght)
        self.weights = []
        self.dElayers = []
        return


class NeuralNet():
    def __init__(self, X, Y, sizeH=[2]):
        self.layers = [Layer(len(X[0]))] + [Layer(i) for i in sizeH] + [Layer(len(Y[0]))]
        self.lenght = len(self.layers)
        for i in range(self.lenght - 1):
            self.layers[i].weights = [[rd.random() for j in range(self.layers[i + 1].lenght)] for k in range(
                self.layers[i].lenght)]  # MATRICE DI ADIACENZE RIGHE = LAYER 0, CLN = LAYER 1
        return

    def feedfw(self, x):
        self.layers[0].O = x
        for i in range(self.lenght - 1):
            for j in range(self.layers[i + 1].lenght):
                self.layers[i + 1].I[j] = np.dot(self.layers[i].O, np.transpose(self.layers[i].weights)[j]) + \
                                          self.layers[i + 1].b[j]
                self.layers[i + 1].O[j] = sigmoid(self.layers[i + 1].I[j])

    def totError(self, x, y):
        self.feedfw(x)
        Error = sum(np.square(np.subtract(y, self.layers[-1].O))) / (self.layers[-1].lenght * 2)
        print(Error)

    def backpropagation(self, x, y):
        self.feedfw(x)
        self.layers[-1].dElayers = np.dot(np.subtract(self.layers[-1].O, y) / self.layers[-1].lenght,
                                          Dsigmoid(self.layers[-1].I))
        for i in reversed(range(1, self.lenght)):
            self.layers[i].dElayers

    def debug(self):
        for layer in self.layers:
            print(layer.O)
            print(layer.weights, "\n")
