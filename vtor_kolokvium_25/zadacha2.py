import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

def generateClassifier():
    return MLPRegressor(
            activation="relu",
            random_state=0,
            learning_rate_init=0.001,
            max_iter=30,
            hidden_layer_sizes=(100,),
            )


def get_acc(nn, y_test, x_test):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for x, y in zip(x_test, y_test):
        clas = "dirty" if y>4.0 else "clean" 
        y_pred = "dirty" if nn.predict([x])[0]>4.0 else "clean"
        
        if clas==y_pred:
            if clas=="dirty":
                tn+=1
            else:
                tp+=1
        else:
            if clas=="dirty":
               fp+=1
            else:
                fn+=1
    return (tp+tn) / (tp + tn + fn + fp)
        
    print(nn.predict([x_test[-1]])[0])

def remove_anomalies(data, a, b, c):
    for row in data:
        if row[0]>a:
            row[0] = a
        if row[1]>b:
            row[1] = b
        if row[2]>c:
            row[2] = c
    return data
if __name__ == '__main__':
    dataset = np.array(pd.read_csv("dataset.csv").values.tolist())
    clsf = generateClassifier()
    X = dataset[:, :-1]
    y = dataset[:, -1]
    train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.7)
    clsf.fit(train_X, train_y)
    
    a = float(input())
    b = float(input())
    c = float(input())
    print(f"Accuracy on original data: {get_acc(clsf, test_y, test_X)}")
    X_anomalied = remove_anomalies(X, a, b, c)
    train_X, test_X, train_y, test_y = train_test_split(X_anomalied, y, train_size=0.7)
    clsf.fit(train_X, train_y)
    print(f"Accuracy on anomaly data: {get_acc(clsf, test_y, test_X)}")
