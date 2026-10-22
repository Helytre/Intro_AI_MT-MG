from sklearn.ensemble import RandomForestClassifier

def First_Forest(training_data, testing_data):

    R_Forest = RandomForestClassifier(
        n_estimators=100, 
        criterion='gini', 
        max_depth=None, 
        min_samples_split=2, 
        min_samples_leaf=1, 
        min_weight_fraction_leaf=0.0, 
        max_features='sqrt', 
        max_leaf_nodes=None, 
        min_impurity_decrease=0.0, 
        bootstrap=True, 
        oob_score=False, 
        n_jobs=None, 
        random_state=None, 
        verbose=0, 
        warm_start=False, 
        class_weight=None, 
        ccp_alpha=0.0, 
        max_samples=None, 
        monotonic_cst=None)

    training_data_X = training_data.loc[ : , training_data.columns != "Accident_Severity"]
    training_data_Y = training_data["Accident_Severity"]

    R_Forest.fit(training_data_X,training_data_Y)

    testing_data_X = testing_data.loc[ : , testing_data.columns != "Accident_Severity"]
    testing_data_Y = testing_data["Accident_Severity"]

    R_Forest_Y = R_Forest.predict(testing_data_X)

    return(R_Forest_Y, testing_data_Y)