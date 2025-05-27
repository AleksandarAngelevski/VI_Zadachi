import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

def read_file(file_name):
    with open(file_name) as doc :
        csv_reader =csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset
if __name__ == '__main__':
    dataset = read_file("car.csv")
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    training_set = dataset[: int(len(dataset)*0.7)]
    train_x = [row[:-1] for row in training_set]
    train_y = [row[-1] for row in training_set]

    train_x = encoder.transform(train_x)

    testing_set = dataset[int(len(dataset)*0.7):]
    test_x = [row[:-1] for row in testing_set]
    test_y = [row[-1] for row in testing_set]
    test_x = encoder.transform(test_x)


    classifier = CategoricalNB()
    classifier.fit(train_x,train_y)
