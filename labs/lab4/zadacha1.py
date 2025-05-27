import os

# from numpy import _1DShapeT
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from zad1_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
# from submission_script import *
# from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
#from submission_script import *
#from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset

if __name__ == '__main__':
    # Vashiot kod tuka
    procent = input()
    procent = float(procent)/100
    criterion = input()

    encoder = OrdinalEncoder()
    encoder.fit([x[:-1] for x in dataset])

    training_dataset = dataset[int((1-procent)*len(dataset)):]
    test_dataset = dataset[:int((1-procent)*len(dataset))]

    train_x = [x[:-1] for x in training_dataset]
    train_y = [x[-1] for x in training_dataset]
    train_x = encoder.transform(train_x)

    test_x = [x[:-1] for x in test_dataset]
    test_y = [x[-1] for x in test_dataset]
    test_x = encoder.transform(test_x)
    
    
    classifier = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier.fit(train_x,train_y)



    a=0

    for (x,y) in zip(test_x,test_y):
        if classifier.predict([x])[0] == y:
            a+=1
    
    

    importances = list(classifier.feature_importances_)


    print('Depth: '+str(classifier.get_depth()))
    print('Number of leaves :'+str(classifier.get_n_leaves()))
    print('Accuracy: ' +str(a / len(test_dataset)))
    print('Most important feature: '+ str(importances.index(max(importances))))
    print('Least important feature: '+ str(importances.index(min(importances))))


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

