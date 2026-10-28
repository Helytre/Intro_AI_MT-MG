import pandas

def one_hot(dataset):
    one_hot_column = ["Road_Type", "Junction_Control", "Pedestrian_Crossing-Physical_Facilities",
                      "Light_Conditions", "Weather_Conditions", "Road_Surface_Conditions",
                      "1st_Road_Class", "2nd_Road_Class", "Day_of_Week"]
    return pandas.get_dummies(dataset, columns=one_hot_column, dtype=int)


def one_hot_encoding(data_training, data_testing):
    full = one_hot(pandas.concat([data_training,data_testing]))
    training = full.loc[data_training.index]
    testing = full.loc[data_testing.index]
    return{"training" : training, "testing" : testing}
