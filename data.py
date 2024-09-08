import pandas as pd
data = pd.read_csv("Lesson_2/titanic.csv")
print(data)
print(data.info())  #It prints the columns, non-null count and data type.
print(data.head())  #It prints the first five of the data.
print(data.tail())  #It prints the last five of the data.

d = (data[["Name", "Age", "Sex", "Survived"]])

print(d.to_string())  #It will print the entire data.
print()
print(pd.options.display.max_rows)

print(data["Age"].mean()) #It prints the average of all the ages of the passengers.
print(data[["Age", "Fare"]].median())

#Average age of male vs. female using groupby
print(data[["Age", "Sex"]].groupby("Sex").mean())
print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"]*data["Pclass"]
print(data.info())