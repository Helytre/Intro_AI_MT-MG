from sklearn.svm import SVC

def Second_SVM(training_data, testing_data, args):

    svm = SVC(*args)

    training_data_X = training_data.loc[ : , training_data.columns != "Accident_Severity"]
    training_data_Y = training_data["Accident_Severity"]
    
    svm.fit(training_data_X,training_data_Y)
    
    testing_data_X = testing_data.loc[ : , testing_data.columns != "Accident_Severity"]
    testing_data_Y = testing_data["Accident_Severity"]
    
    svm_Y = svm.predict(testing_data_X)
    
    return(svm_Y, testing_data_Y)