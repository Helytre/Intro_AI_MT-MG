from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def coord_positive(dataset):
    for column in dataset.columns.to_list():
        if(dataset[column].min()<0):
            c = dataset[column]
            dataset[column] = c-dataset[column].min()
    return dataset

def Categorical_Naive_Bayes(dataset):
    args_list = [
        ("C_NB_default",{
            "alpha":1.0,
            "force_alpha":True,
            "fit_prior":True,
            "class_prior":None,
            "min_categories":None
        }),
        ("C_NB_tuned",{
            "alpha":25.0,
            "force_alpha":True,
            "fit_prior":True,
            "class_prior":None,
            "min_categories":None
        })]
    
    dataset["training_data_X"] = coord_positive(dataset["training_data_X"])
    dataset["testing_data_X"] = coord_positive(dataset["testing_data_X"])

    result = []

    for args in args_list:
        Categorical_NB = CategoricalNB(**args[1])
        Categorical_NB.fit(dataset["training_data_X"],dataset["training_data_Y"])
        Categorical_NB_Y = Categorical_NB.predict(dataset["testing_data_X"])

        result.append((args[0],accuracy_score(dataset["testing_data_Y"], Categorical_NB_Y),f1_score(dataset["testing_data_Y"], Categorical_NB_Y, average="macro")))
            
    return result