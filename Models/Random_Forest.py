from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def Forest(dataset):

    args_list = [
    ("R_Forest_default",{
        "n_estimators": 100,
        "criterion": "gini",
        "max_depth": None,
        "min_samples_split": 2,
        "min_samples_leaf": 1,
        "min_weight_fraction_leaf": 0.0,
        "max_features": "sqrt",
        "max_leaf_nodes": None,
        "min_impurity_decrease": 0.0,
        "bootstrap": True,
        "oob_score": False,
        "n_jobs": None,
        "random_state": None,
        "verbose": 0,
        "warm_start": False,
        "class_weight": None,
        "ccp_alpha": 0.0,
        "max_samples": None,
        "monotonic_cst":None
    }),
    ("R_Forest_tuned",{
        "n_estimators": 100,
        "criterion": "gini",
        "max_depth": None,
        "min_samples_split": 2,
        "min_samples_leaf": 1,
        "min_weight_fraction_leaf": 0.0,
        "max_features": "sqrt",
        "max_leaf_nodes": None,
        "min_impurity_decrease": 0.0,
        "bootstrap": True,
        "oob_score": False,
        "n_jobs": None,
        "random_state": None,
        "verbose": 0,
        "warm_start": False,
        "class_weight": None,
        "ccp_alpha": 0.0,
        "max_samples": None,
        "monotonic_cst":None
    })]

    result = []

    for args in args_list:
        R_Forest = RandomForestClassifier(**args[1])
        R_Forest.fit(dataset["training_data_X"],dataset["training_data_Y"])      
        R_Forest_Y = R_Forest.predict(dataset["testing_data_X"])

        result.append((args[0],accuracy_score(dataset["testing_data_Y"], R_Forest_Y),f1_score(dataset["testing_data_Y"], R_Forest_Y, average="macro")))

    return(result)