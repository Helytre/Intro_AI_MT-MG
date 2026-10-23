from sklearn.naive_bayes import CategoricalNB

def Categorical_Naive_Bayes(training_data, testing_data, args):

    Categorical_NB = CategoricalNB(**args)

    training_data_X = training_data.loc[ : , training_data.columns != "Accident_Severity"]
    training_data_Y = training_data["Accident_Severity"]

    Categorical_NB.fit(training_data_X,training_data_Y)

    testing_data_X = testing_data.loc[ : , testing_data.columns != "Accident_Severity"]
    testing_data_Y = testing_data["Accident_Severity"]

    Categorical_NB_Y = Categorical_NB.predict(testing_data_X)

    return(Categorical_NB_Y, testing_data_Y)