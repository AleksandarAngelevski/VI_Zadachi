from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder 



if __name__ == "__main__":

    encoder = OrdinalEncoder()
    classifier = CategoricalNB()
    
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
               ['C', 'H', 'I', '1', '3', '1', '1', '2', '1', '2', '0'],
               ['D', 'R', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],]
    encoder.fit([row[:-1] for row in dataset])


    train_x = [row[:-1] for row in dataset[:int(0.75*len(dataset))]]
    train_y = [row[-1] for row in dataset[:int(0.75*len(dataset))]] 
    test_x = [row[:-1] for row in dataset[int(0.75*len(dataset)):]]
    test_y = [row[-1] for row in dataset[int(0.75*len(dataset)):]]
    
    test_x = encoder.transform(test_x)
    train_x = encoder.transform(train_x)
    classifier.fit(train_x,train_y)

    line = input()
    line_arr = line.split(" ")
   # print(line_arr)
    line_arr  = encoder.transform([line_arr])
    predicted_input = classifier.predict(line_arr)[0]
    predicted_distribution = classifier.predict_proba(line_arr)
    acc=0
    for x,y in zip(test_x,test_y):
        pred = classifier.predict([x])[0]
        if pred == y:
            acc+=1

    print(acc/len(test_x))
    print(predicted_input)
    print(predicted_distribution)

