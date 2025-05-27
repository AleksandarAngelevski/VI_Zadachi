import os
import csv
os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from zad1_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]


# def read_file(file_name):
#     with open(file_name) as doc:
#         csv_reader = csv.reader(doc, delimiter=',')

#     return file

if __name__ == '__main__':
    # Vashiot kod tuka
    encoder = OrdinalEncoder()
    acc=0
    encoder.fit([row[:-1] for row in dataset])
    train_set = dataset[:int(len(dataset)*.75)]
    test_set = dataset[int(len(dataset)*.75):]
    classifier = CategoricalNB()

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)
    classifier.fit(train_x,train_y)


    for tx, ty in zip(test_x,test_y):
        pred = classifier.predict([tx])[0]
        if pred == ty:
            acc+=1
    
    input_line = input()
    input_test =  [input_line.split(" ")]
    input_test = encoder.transform(input_test)

    pred_input = classifier.predict(input_test)[0]
    pred_input_probs = classifier.predict_proba(input_test)
    print(acc/len(test_x))
    print(pred_input)
    print(pred_input_probs)
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    # submit_classifier(classifier)
    
    # submit na encoderot
    # submit_encoder(encoder)
