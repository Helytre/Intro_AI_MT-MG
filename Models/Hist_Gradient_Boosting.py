from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def H_Grad_Boosting(dataset, PCA):

    categorical_list = 'from_dtype'
    if(not PCA):
        categorical_list = ["Day_of_Week","1st_Road_Class","Road_Type","Junction_Control","2nd_Road_Class","Pedestrian_Crossing-Physical_Facilities","Light_Conditions","Weather_Conditions","Road_Surface_Conditions","Urban_or_Rural_Area","Did_Police_Officer_Attend_Scene_of_Accident"]

    args_list = [
    ("Hist_GB_default",{
        "loss":'log_loss',
        "learning_rate":0.1,
        "max_iter":100,
        "max_leaf_nodes":31,
        "max_depth":None,
        "min_samples_leaf":20,
        "l2_regularization":0.0,
        "max_features":1.0,
        "max_bins":255,
        "categorical_features":'from_dtype',
        "monotonic_cst":None,
        "interaction_cst":None,
        "warm_start":False,
        "early_stopping":'auto',
        "scoring":'loss',
        "validation_fraction":0.1,
        "n_iter_no_change":10,
        "tol":1e-07,
        "verbose":0,
        "random_state":None,
        "class_weight":None
    }),
    ("Hist_GB_tuned",{
        "loss":'log_loss',
        "learning_rate":0.03,
        "max_iter":140,
        "max_leaf_nodes":31,
        "max_depth":None,
        "min_samples_leaf":30,
        "l2_regularization":0.0,
        "max_features":0.5,
        "max_bins":255,
        "categorical_features":categorical_list,
        "monotonic_cst":None,
        "interaction_cst":None,
        "warm_start":False,
        "early_stopping":False,
        "scoring":'accuracy',
        "validation_fraction":0.0001,
        "n_iter_no_change":10,
        "tol":1e-07,
        "verbose":0,
        "random_state":None,
        "class_weight":None
    })]

    result = []

    for args in args_list:
        H_Grad_Boost = HistGradientBoostingClassifier(**args[1])
        H_Grad_Boost.fit(dataset["training_data_X"],dataset["training_data_Y"])
        H_Grad_Boost_Y = H_Grad_Boost.predict(dataset["testing_data_X"])

        result.append((args[0],accuracy_score(dataset["testing_data_Y"], H_Grad_Boost_Y),f1_score(dataset["testing_data_Y"], H_Grad_Boost_Y, average="macro")))

    return(result)