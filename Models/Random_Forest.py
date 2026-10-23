from sklearn.ensemble import RandomForestClassifier

def Forest(training_data, testing_data, args):

    R_Forest = RandomForestClassifier(**args)

    training_data_X = training_data.loc[ : , training_data.columns != "Accident_Severity"]
    training_data_Y = training_data["Accident_Severity"]

    R_Forest.fit(training_data_X,training_data_Y)

    testing_data_X = testing_data.loc[ : , testing_data.columns != "Accident_Severity"]
    testing_data_Y = testing_data["Accident_Severity"]

    R_Forest_Y = R_Forest.predict(testing_data_X)

    return(R_Forest_Y, testing_data_Y)