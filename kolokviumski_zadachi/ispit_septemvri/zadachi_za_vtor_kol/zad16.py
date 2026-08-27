import os

from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'




def split_dataset(data, P):
    n = int(len(data) * P / 100)
    
    return data[:n], data[n:]

def acc(y_true, y_pred):
    correct = 0
    for x, y in zip(y_true, y_pred):
        if x == y:
            correct += 1
    return correct / len(y_true) * 100

def clean_dataset(train_x, train_y, label):
    new_train_x = []
    new_train_y = []
    for x, y in zip(train_x, train_y):
        if y == label:
            new_train_x.append(x)
            new_train_y.append(1)
        else:
            new_train_x.append(x)
            new_train_y.append(0)

    return new_train_x, new_train_y
    

def tree_ensemble(train_X, train_y, test_X, test_y, crit, L):
    tree1 = DecisionTreeClassifier(criterion=crit, max_leaf_nodes=L, random_state=0)
    tree2 = DecisionTreeClassifier(criterion=crit, max_leaf_nodes=L, random_state=0)
    tree3 = DecisionTreeClassifier(criterion=crit, max_leaf_nodes=L, random_state=0)

    x, y = clean_dataset(train_X, train_y, "Roach")
    tree1.fit(x, y)
    x, y = clean_dataset(train_X, train_y, "Perch")
    tree2.fit(x, y)
    x, y = clean_dataset(train_X, train_y, "Bream")
    tree3.fit(x, y)

    pred1 = tree1.predict(test_X)
    pred2 = tree2.predict(test_X)
    pred3 = tree3.predict(test_X)

    correct =0
    for x,y,z, w in zip(pred1, pred2, pred3, test_y):
        if w == "Roach":
            if x == 1 and y != 1 and z != 1:
                correct += 1
        if w == "Perch":
            if y == 1 and x != 1 and z != 1:
                correct += 1
        if w == "Bream":
            if z == 1 and x != 1 and y != 1:
                correct += 1

    return correct / len(test_y)





if __name__ == '__main__':
    dataset = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'], [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'], [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch'], [320.0, 27.8, 30.0, 31.6, 24.1, 15.1, 'Perch'], [160.0, 21.1, 22.5, 25.0, 25.6, 15.2, 'Roach'], [700.0, 30.4, 33.0, 38.3, 38.8, 13.8, 'Bream'], [500.0, 29.5, 32.0, 37.3, 37.3, 13.6, 'Bream'], [290.0, 24.0, 26.3, 31.2, 40.0, 13.8, 'Bream'], [650.0, 31.0, 33.5, 38.7, 37.4, 14.8, 'Bream'], [500.0, 26.8, 29.7, 34.5, 41.1, 15.3, 'Bream']]

    procent = int(input())
    crit = input()
    L = int(input())

    train, test = split_dataset(dataset, procent)

    print(len(train))
    print(len(test))
    
    tree1 = DecisionTreeClassifier(criterion=crit, max_leaf_nodes=L)


    train_X = [x[:-1] for x in train]
    train_y = [x[-1] for x in train]

    test_X = [x[:-1] for x in test]
    test_y = [x[-1] for x in test]

    tree1.fit(train_X, train_y)
    pred = tree1.predict(test_X)

    print(f"Tochnost so originalniot klasifikator: {acc(test_y, pred)}")
    print(f"Tochnost so kolekcija od klasifikatori: {tree_ensemble(train_X, train_y, test_X, test_y, crit, L)}")