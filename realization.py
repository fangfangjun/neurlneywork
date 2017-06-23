import random
import numpy as np

#--class ComputationGraph(object):
#    def forwards(inputs):
#        for gate in

class Ypred(object):
    pass


class NearestNeighbour:
    def __init__(self):
        pass

    def train(self,X,y):
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        num_test = X.shape[0]
        Ypre = np.zeros(num_test,dtype=self.ytr.dtype)

        from pip._vendor.requests.packages.urllib3.connectionpool import xrange
        for i in xrange(num_test):
            distances = np.sum(np.abs(self.Xtr - X[i,:],axis = 1))
            min_index = np.argmin(distances)
            Ypred[i] = self.ytr[min_index]
        return Ypred
