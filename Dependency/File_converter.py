import pandas

#reading file
dataset = pandas.read_csv("./Dataset/UK_Accident.csv",na_filter=False)

#delete useless column
dropping_column = ["Location_Easting_OSGR", "Location_Northing_OSGR", "LSOA_of_Accident_Location"]
for column in dropping_column:
    dataset.drop(column, axis=1, inplace=True)

#delete extreme value

#selecting 10k value / class
dataset = dataset.groupby('Accident_Severity').sample(n=10000)

print(dataset["Accident_Severity"].value_counts())
#writing clean dataset for machine learning use
dataset.to_csv("./Dataset/Clean_UK_Accident.csv")