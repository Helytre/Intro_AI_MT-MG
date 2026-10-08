import pandas

def cleaning():
    #reading file
    dataset = pandas.read_csv("./Dataset/UK_Accident.csv")

    #delete useless column
    dropping_column = ["Location_Easting_OSGR", "Location_Northing_OSGR", "LSOA_of_Accident_Location"]
    for column_name in dropping_column:
        if column_name in dataset.columns:
            dataset.drop(column_name, axis=1, inplace=True)
        else:
            print("Column do not exist : ", column_name)

    print(dataset["Accident_Severity"].value_counts())

    #delete extreme value
    #std method (4*std)
    std_column = ["Number_of_Casualties"]
    mean_values = {}
    std_values = {}
    for column_name in std_column:
        mean_values[column_name] = dataset[column_name].mean()
        std_values[column_name] = dataset[column_name].std()
    for column_name in std_column:
        dataset = dataset[dataset[column_name] <= (mean_values[column_name]+4*std_values[column_name])]
        dataset = dataset[dataset[column_name] >= (mean_values[column_name]-4*std_values[column_name])]
    
    #IQR method : "Number_of_Casualties"
    IQR_column = []
    Q1 = {}
    Q3 = {}
    for column_name in IQR_column:
        Q1[column_name] = dataset[column_name].quantile(0.25)
        Q3[column_name] = dataset[column_name].quantile(0.75)
    for column_name in IQR_column:
        dataset = dataset[dataset[column_name] <= (Q3[column_name]+1.5*(Q3[column_name]-Q1[column_name]))]
        dataset = dataset[dataset[column_name] >= (Q1[column_name]-1.5*(Q3[column_name]-Q1[column_name]))]
        

    print(dataset["Accident_Severity"].value_counts())

    #selecting 10k value / class
    dataset = dataset.groupby('Accident_Severity').sample(n=10000)

    #replacing str value by number

    #writing clean dataset for machine learning use
    dataset.to_csv("./Dataset/Clean_UK_Accident.csv")

    return(dataset)

cleaning()