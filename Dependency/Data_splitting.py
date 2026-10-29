import pandas    

def selecting():
    #reading cleaned file
    dataset = pandas.read_csv("./Dataset/Clean_UK_Accident.csv")

    #selecting 10k value / class
    dataset = dataset.groupby('Accident_Severity').sample(n=15000)

    #splitting data
    data_training = dataset.sample(frac=0.75)
    data_testing = dataset.drop(data_training.index)

    return({"training_data":data_training,"testing_data":data_testing})

def targeting(dataset):

    training_data_X = dataset["training_data"].loc[ : , dataset["training_data"].columns != "Accident_Severity"]
    training_data_Y = dataset["training_data"]["Accident_Severity"]
    
    testing_data_X = dataset["testing_data"].loc[ : , dataset["testing_data"].columns != "Accident_Severity"]
    testing_data_Y = dataset["testing_data"]["Accident_Severity"]

    return({"training_data_X":training_data_X,"training_data_Y":training_data_Y,"testing_data_X":testing_data_X,"testing_data_Y":testing_data_Y})

def normalization(dataset):
    for column in dataset.columns.to_list():
        min = -dataset[column].min()
        max = dataset[column].max()
        if((min)>max):
            dataset[column] = dataset[column]/min
        else:
            dataset[column] = dataset[column]/max
    return dataset