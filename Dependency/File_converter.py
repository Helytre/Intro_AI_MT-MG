import pandas

def selecting():
    #reading cleaned file
    dataset = pandas.read_csv("./Dataset/Clean_UK_Accident.csv")

    #selecting 10k value / class
    dataset = dataset.groupby('Accident_Severity').sample(n=10000, random_state=1)

    return(dataset)

def cleaning():
    #reading file
    dataset = pandas.read_csv("./Dataset/UK_Accident.csv")

    #delete useless column
    dataset = dropping(dataset)

    #delete extreme value
    dataset = deleting_extreme(dataset)

    #deleting low class count value
    dataset = deleting_low(dataset)

    #replacing str value by number

    #writing clean dataset for machine learning use
    dataset.to_csv("./Dataset/Clean_UK_Accident.csv")

    return(dataset)

def dropping(dataset):
    dropping_column = ["Location_Easting_OSGR", "Location_Northing_OSGR", "LSOA_of_Accident_Location", "Police_Force", "Local_Authority_(District)", "Local_Authority_(Highway)", "1st_Road_Number", "2nd_Road_Number", "Date", "Pedestrian_Crossing-Human_Control", "Special_Conditions_at_Site", "Carriageway_Hazards", "Did_Police_Officer_Attend_Scene_of_Accident"]
    for column_name in dropping_column:
        if column_name in dataset.columns:
            dataset.drop(column_name, axis=1, inplace=True)
        else:
            print("Column do not exist : ", column_name)
    return(dataset)

def deleting_extreme(dataset):
    #std method (4*std)
    std_column = ["Number_of_Casualties","Number_of_Vehicles"]
    mean_values = {}
    std_values = {}
    for column_name in std_column:
        mean_values[column_name] = dataset[column_name].mean()
        std_values[column_name] = dataset[column_name].std()
    for column_name in std_column:
        dataset = dataset[dataset[column_name] <= (mean_values[column_name]+4*std_values[column_name])]
        dataset = dataset[dataset[column_name] >= (mean_values[column_name]-4*std_values[column_name])]
    
    #IQR method : 
    IQR_column = []
    Q1 = {}
    Q3 = {}
    for column_name in IQR_column:
        Q1[column_name] = dataset[column_name].quantile(0.25)
        Q3[column_name] = dataset[column_name].quantile(0.75)
    for column_name in IQR_column:
        dataset = dataset[dataset[column_name] <= (Q3[column_name]+1.5*(Q3[column_name]-Q1[column_name]))]
        dataset = dataset[dataset[column_name] >= (Q1[column_name]-1.5*(Q3[column_name]-Q1[column_name]))]
        
    return(dataset)

def deleting_low(dataset):
    dataset = dataset[dataset["Speed_limit"] >= 20]
    dataset = dataset[dataset["Urban_or_Rural_Area"] != 3]
    return dataset

cleaning()
