# We can use the pandas library in python to read in the csv file.
# This creates a pandas dataframe and assigns it to the titanic variable.
titanic = pandas.read_csv("titanic_train.csv")

# Print the first 5 rows of the dataframe.
print(titanic.head(5))
print(titanic.describe())
# Fill missing values of AGE
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
# Find all the unique genders -- the column appears to contain only male and female.
print(titanic["Sex"].unique())

# Replace all the occurences of male with the number 0.
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1
