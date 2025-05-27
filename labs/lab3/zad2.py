import os
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import GaussianNB
os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset
from zad2_dataset import dataset
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'], 
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'], 
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    acc=0
    dataset = [[float(i) for i in row]for row in dataset]
    classifier = GaussianNB()
    encoder = OrdinalEncoder()
    train_set = dataset[:int(0.85*len(dataset))]
    test_set = dataset[int(0.85*len(dataset)):]
    test_set
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    classifier.fit(train_X,train_Y)
    
    for tx,ty in zip(test_X,test_Y):
        prediction = classifier.predict([tx])[0]
        if ty == prediction:
            acc+=1

    print(acc/len(test_set))
    input_line = input()
    input_test  = input_line.split(" ")
    input_test = [float(i) for i in input_test]
    prediction = classifier.predict([input_test])[0]
    print(int(prediction))
    print(classifier.predict_proba([input_test]))


    
    
    
    
    
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    
    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)
    
    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)
    
    # submit na klasifikatorot
    # submit_classifier(classifier)
    
    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
