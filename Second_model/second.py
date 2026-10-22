from sklearn.svm import SVC

def Second_SVM(training_data, testing_data):

    svm = SVC(
        C=1.0, 
        kernel='rbf', 
        degree=3, 
        gamma='scale', 
        coef0=0.0, 
        shrinking=True, 
        probability='deprecated', 
        tol=0.001, cache_size=200, 
        class_weight=None, 
        verbose=False, 
        max_iter=-1, 
        decision_function_shape='ovr', 
        break_ties=False, 
        random_state=None)

    training_data_X = training_data.loc[ : , training_data.columns != "Accident_Severity"]
    training_data_Y = training_data["Accident_Severity"]
    
    svm.fit(training_data_X,training_data_Y)
    
    testing_data_X = testing_data.loc[ : , testing_data.columns != "Accident_Severity"]
    testing_data_Y = testing_data["Accident_Severity"]
    
    svm_Y = svm.predict(testing_data_X)
    
    return(svm_Y, testing_data_Y)