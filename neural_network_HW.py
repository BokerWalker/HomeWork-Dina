import numpy as np
import matplotlib.pyplot as plt

#Niv Lifshitz and Liam Brinker.
#after a lot of debugging we found out what was wrong.
np.random.seed()
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
  # Derivative of sigmoid: f'(x) = f(x) * (1 - f(x))
  fx = sigmoid(x)
  return fx * (1 - fx)


def mse_loss(y_true, y_pred):
  # y_true and y_pred are numpy arrays of the same length.
  return ((y_true - y_pred) ** 2).mean()


class Neuron:
  def __init__(self, weights, bias):
    self.weights = weights
    self.bias = bias
    

  def feedforward(self, inputs):
    # Weight inputs, add bias, then use the activation function
    total = np.dot(self.weights, inputs) + self.bias
    return sigmoid(total)

class OurNeuralNetwork:
     
    def __init__(self):
        self.Hweights = np.full((2,2),0.5)
        self.Oweights = np.full((1,2),0.5)
        self.biases = np.array([1,1,1],dtype = 'float64')
        self.loss_history = []
    def feedforward(self, x):
  # x is a numpy array with 2 elements.
        
        sums_H = (self.Hweights * x).sum(axis=1) + self.biases[:2]
        #1,2
        #sums_H = np.array([sums_H[0].sum(),sums_H[1].sum()])
        
        #1,2
        H1_H2 = sigmoid(sums_H)
        #                   
        o1 = sigmoid((H1_H2 * self.Oweights).sum() + self.biases[2])
        return o1

    def train(self, data, all_y_trues):
        '''
        - data is a (n x 2) numpy array, n = # of samples in the dataset.
        - all_y_trues is a numpy array with n elements.
          Elements in all_y_trues correspond to those in data.
        '''
        learn_rate = 0.1
        epochs = 1000 # number of times to loop through the entire dataset

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
        # --- Do a feedforward (we'll need these values later)
                
                #1,2       [[w1,w2][w3,w4]]    [[x1,x2][x1,x2]]
                sums_H = (self.Hweights * x).sum(axis=1) + self.biases[:2]
                #sums_H = np.array([sums_H[0].sum(),sums_H[1].sum()])
                #2,2
                H1_H2 = sigmoid(sums_H)
                sum_o1 = (H1_H2 * self.Oweights).sum() + self.biases[2]
                
                o1 = sigmoid(sum_o1)
                y_pred = o1
                
                d_L_ypred = -2 * (y_true - y_pred)
                #w,w,b
                O1_derives = np.append(H1_H2,[1]) * deriv_sigmoid(sum_o1)
                
                #(1,2)
                d_ypred_H =  self.Oweights * deriv_sigmoid(sum_o1)
                
                #1,3
                H1_derives = np.append(x,[1]) * deriv_sigmoid(sums_H[0])
                H2_derives = np.append(x,[1]) * deriv_sigmoid(sums_H[1])
                
                #2,2
                H_derives=np.vstack((H1_derives[:2],H2_derives[:2]))
                #(2,2)                        
                self.Hweights -= learn_rate * d_L_ypred * d_ypred_H * H_derives
                #1,2
                self.Oweights -= learn_rate * d_L_ypred * O1_derives[:2]
                
                
                #    1,3           k           k                 1,3                                 1,3
                self.biases -= learn_rate * d_L_ypred * np.append(d_ypred_H,[1]) * np.array([H1_derives[-1],H2_derives[-1],O1_derives[-1]])
            y_preds = np.apply_along_axis(self.feedforward, 1, data)
            loss = mse_loss(all_y_trues,y_preds)
            self.loss_history.append(loss)
            if epoch % 10 == 0:
                print("Epoch %d loss: %.3f" % (epoch, loss))
        fig, ax = plt.subplots()
        ax.set_xlabel('epoch')
        ax.set_ylabel('loss')
        ax.plot(self.loss_history)
        
                          
# Define dataset
data = np.array([
  [-2, -1],  # Alice
  [25, 6],   # Bob
  [17, 4],   # Charlie
  [-15, -6], # Diana
])
all_y_trues = np.array([
  1, # Alice
  0, # Bob
  0, # Charlie
  1, # Diana
])

# Train our neural network!
network = OurNeuralNetwork()
network.train(data, all_y_trues)
  
            
emily = np.array([-7, -3]) # 128 pounds, 63 inches
frank = np.array([20, 2])  # 155 pounds, 68 inches
print("Emily: %.3f" % network.feedforward(emily)) # 0.951 - F
print("Frank: %.3f" % network.feedforward(frank)) #0.039 - M


