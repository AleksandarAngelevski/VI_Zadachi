from typing import TypeAliasType
from sklearn import tree
from sklearn.preprocessing import OrdinalEncoder
if __name__ == "__main__":
    dataset = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
           ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
           ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['D', 'A', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
           ['D', 'A', 'O', '1', '2', '1', '1', '2', '1', '1', '0'],
           ['D', 'A', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
           ['D', 'K', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['C', 'R', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
           ['B', 'X', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
           ['D', 'S', 'O', '1', '2', '1', '1', '2', '1', '1', '0'],
           ['C', 'H', 'I', '1', '3', '1', '1', '2', '1', '2', '0'],]
    percent = int(input())
    crit = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    classifier = tree.DecisionTreeClassifier(random_state=0, criterion=crit)
    print(percent/100 * len(dataset))
    print(crit)
    train_x = [ row[:-1] for row in dataset[int(percent/100 * len(dataset)):]]
    train_y = [ row[-1] for row in dataset[int(percent/100 * len(dataset)):]]


    test_x = [ row[:-1] for row in dataset[:int(((100-percent)/100) * len(dataset))]]
    test_y = [ row[-1] for row in dataset[:int(((100-percent)/100) * len(dataset))]]

    train_x = encoder.transform(train_x)
    test_x = encoder.transform(test_x)

    classifier.fit(train_x,train_y)
    
    acc = 0
    for x,y in zip(test_x,test_y):
        pred = classifier.predict([x])[0]
        if pred == y :
            acc+=1

    importances = list(classifier.feature_importances_)

    print("Depth: " + str(classifier.get_depth()))
    print("Number of leaves: "+ str(classifier.get_n_leaves()))
    print("Accuracy: " + str(acc/len(test_x)))
    print("Most important feature: "+str(importances.index(max(importances))))
    print("Least important feature: "+str(importances.index(min(importances))))



