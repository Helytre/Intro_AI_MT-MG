from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def SVM_svc(dataset):

    args_list = [
    ("SVM_default",{
        "C":1.0, 
        "kernel":'rbf', 
        "degree":3, 
        "gamma":'scale', 
        "coef0":0.0, 
        "shrinking":True, 
        "probability":'deprecated', 
        "tol":0.001, 
        "cache_size":200, 
        "class_weight":None, 
        "verbose":False, 
        "max_iter":-1, 
        "decision_function_shape":'ovr', 
        "break_ties":False, 
        "random_state":None
    }),
    ("SVM_tuned",{
        "C":1.0, 
        "kernel":'rbf', 
        "degree":3, 
        "gamma":'scale', 
        "coef0":0.0, 
        "shrinking":True, 
        "probability":'deprecated', 
        "tol":0.001, 
        "cache_size":200, 
        "class_weight":None, 
        "verbose":False, 
        "max_iter":-1, 
        "decision_function_shape":'ovr', 
        "break_ties":False, 
        "random_state":None
    })]

    result = []

    for args in args_list:
        svm = SVC(**args[1])
        svm.fit(dataset["training_data_X"],dataset["training_data_Y"])
        svm_Y = svm.predict(dataset["testing_data_X"])
    
        result.append((args[0],accuracy_score(dataset["testing_data_Y"], svm_Y),f1_score(dataset["testing_data_Y"], svm_Y, average="macro")))

    return result