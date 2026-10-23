from sklearn.ensemble import HistGradientBoostingClassifier

def H_Grad_Boosting(training_data, testing_data, args):

    H_Grad_Boost = HistGradientBoostingClassifier(**args)

    training_data_X = training_data.loc[ : , training_data.columns != "Accident_Severity"]
    training_data_Y = training_data["Accident_Severity"]

    H_Grad_Boost.fit(training_data_X,training_data_Y)

    testing_data_X = testing_data.loc[ : , testing_data.columns != "Accident_Severity"]
    testing_data_Y = testing_data["Accident_Severity"]

    H_Grad_Boost_Y = H_Grad_Boost.predict(testing_data_X)

    return(H_Grad_Boost_Y, testing_data_Y)