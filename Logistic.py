#!/usr/bin/python

import math

# The main method
def main():
    global m
    global numInputs
    global numVectors
    global eta
    eta = 0.00000001
    f1 = open('heart-train.txt')
    seq1 = f1.read()
    m = readNumInputs(seq1)
    m = m+1 # to take into account x0 = 1
    numInputs = m
    numVectors = readNumVectors(seq1)
    global data
    data = getFeatures(seq1) #this now has x0 = 1
    probY = getProbY()

    theta = gradAscent() #just commented out
    #for i in range(0, m):
        #print "Theta", i, theta[i]


    # testing part
    f2 = open('heart-test.txt')
    seq2 = f2.read()
    numVectorsTest = readNumVectors(seq2)
    testing = getFeaturesTest(seq2, numVectorsTest)
    predictions = makePredictions(theta, numVectorsTest, testing)
    accuracy = getAccuracy(predictions, testing, numVectorsTest)
    print "Accuracy: ", accuracy, "%"



def makePredictions(theta, numVectorsTest, testing):
    predictions = []
    for i in range(0, numVectorsTest):
        p = sigmoid(thetaTransposeX(theta, testing[i]))
        if p>=0.5:
            predictions.append(1)
        else:
            predictions.append(0)
    return predictions

def LL(theta):
    sum = 0.0
    for i in range(0, numVectors):
        yi = data[i][m]
        xi = data[i]
        firstTerm = yi*math.log(sigmoid(thetaTransposeX(theta, xi)))
        secondTerm = (1-yi)*math.log(1-sigmoid(thetaTransposeX(theta, xi)))
        sum +=(firstTerm+secondTerm)
    return sum

def thetaTransposeX(theta, xi):
    sum = 0.0
    for i in range(0, m):
        if i==0:
            sum+=theta[i]
        else:
            sum+=(theta[i]*(xi[i]))
    return sum

def gradAscent():
    theta = []
    for j in range(0, m):
        theta.append(0.0)
    #print len(theta)
    numIterations = 10000
    for i in range(0, numIterations):
        print "iteration: ", i
        gradient = []
        for j in range(0, m):
            gradient.append(0.0)
        for x in range(0, numVectors):
            z = calculateZ(theta, x) # NEW LINE
            y = deriv(x, z)
            for j in range(0, m):
                X = data[x][j]
                gradient[j]+=(X*y)
        for j in range(0, m):
            theta[j]+= eta*gradient[j]

    return theta

def deriv(x, z):
    y = data[x][m]
    y-=sigmoid(z)
    return y

def sigmoid(z):
    val = 1.0
    denom = 1.0 + math.exp(-z)
    val/=denom
    return val


def calculateZ(theta, x):
    sum = 0.0
    for j in range(0, m):
        sum+=(theta[j]*float(data[x][j]))
    return sum


def readNumInputs(seq):
    numInputs= 10*(int(seq[0])) + int(seq[1]) #2
    return numInputs

def readNumVectors(seq):
    numVectors = (1000*(int(seq[3]))) + (100*(int(seq[4]))) + (10*(int(seq[5]))) + (int(seq[6]))
    return numVectors


def getAccuracy(predictions, testing, numVectorsTest):
    correct = 0.0
    class0Correct = 0.0
    class1Correct = 0.0
    class0 = 0.0
    class1 = 0.0
    for i in range(0, len(predictions)):
        if testing[i][numInputs]==0:
            class0+=1
        if testing[i][numInputs]==1:
            class1+=1
        if (predictions[i]==testing[i][numInputs]):
            if (testing[i][numInputs])==0:
                class0Correct+=1
            if testing[i][numInputs]==1:
                class1Correct+=1
            correct = correct+1
    print "Class 0: tested ", class0, ", correctly classified: ", class0Correct
    print "Class 1: tested ", class1, ", correctly classified: ", class1Correct
    return 100*correct/float(numVectorsTest)

def getProbY():
    probY = []
    num0 = 0.0
    num1 = 0.0
    for i in range(0, numVectors):
        if (data[i][numInputs] == 0):
            num0 = num0 + 1
        if (data[i][numInputs] == 1):
            num1 = num1 + 1
    probY.append(num0 / float(numVectors))
    probY.append(num1 / float(numVectors))
    return probY

def getFeatures(seq1):
    vectors = []
    k = 7
    for j in range(0, numVectors):
        features = []
        features.append(1) #to make x0 = 1
        for i in range(0, numInputs-1+numInputs-1+3):
            if (seq1[k + i] != "\n")&(seq1[k+i]!=',')&(seq1[k+i]!=" ")&(seq1[k+i]!=":"):
                features.append(int(seq1[k + i]))
        k = k + numInputs-1 + numInputs-1 + 3
        vectors.append(features)
    return vectors

def getFeaturesTest(seq1, numVectorsTest):
    vectors = []
    k = 7
    for j in range(0, numVectorsTest):
        features = []
        features.append(1)
        for i in range(0, numInputs-1 +numInputs-1 +3):
            #print (k+i)
            if (seq1[k + i] != "\n")&(seq1[k+i]!=',')&(seq1[k+i]!=" ")&(seq1[k+i]!=":"):
                features.append(int(seq1[k + i]))
        k = k + numInputs-1 + numInputs-1 + 3
        vectors.append(features)
    return vectors


def __iadd__(self, other):
    print 'in __iadd__', other
    self.num = self.num + other
    return self.num

# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
    main()