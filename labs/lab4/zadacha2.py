from zad2_dataset import dataset
from sklearn.ensemble import RandomForestClassifier


if __name__ == "__main__":

    col_index = int(input())
    number_trees = int(input())
    crit_value = str(input())
    array = input().split(" ")
    array = [float(e) for e in array]
    array.pop(col_index)
    data = [row for row in dataset]
    for row in data:
        row.pop(col_index)
    

    train = data[:int(0.85 * len(data))]
    train_x = [row[:-1] for row in train]
    train_y = [row[-1] for row in train]

    test = data[int(0.85 * len(data)):]
    test_x = [row[:-1] for row in test]
    test_y = [row[-1] for row in test]

    classifier = RandomForestClassifier(n_estimators=number_trees, criterion=crit_value, random_state=0)
    classifier.fit(train_x, train_y)

    acc = 0
    for (x, y) in zip(test_x, test_y):
        if classifier.predict([x])[0] == y:
            acc += 1

    print('Accuracy: '+str(acc / len(test)))
    print (str(classifier.predict([array])[0]))
    print(str(classifier.predict_proba([array])[0]))


