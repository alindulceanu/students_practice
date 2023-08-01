import pandas as pd

mydataset = {
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(pd.__version__)

a = [1, 7, 2]

myvar = pd.Series(a, index = ['a', 'b', 'c'])

print(myvar)

calories = {'day1': 400, 'day2': 800, 'day3': 266}

myvar = pd.Series(calories, index = ['day1', 'day2'])

print(myvar)

data = {
    'calories': [450, 300, 600],
    'duration': [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar.loc[2])

myvar = pd.read_csv('data.csv')
pd.options.display.max_rows = 9999

print(myvar.to_string())
print(pd.options.display.max_rows)

df = pd.read_json('data.json')

print(df.to_string())

print(myvar.info())

print(myvar.head(13))

print(myvar.tail(15))

#new_df = myvar.dropna(inplace = True)

print(myvar.to_string)

new_myvar = myvar['Calories'].fillna(130)

print(new_myvar.to_string())

new_myvar = myvar['Calories'].fillna(myvar['Calories'].mean())

print(new_myvar.to_string())

new_myvar = myvar['Calories'].fillna(myvar['Calories'].median())

print(new_myvar.to_string())

new_myvar = myvar['Calories'].fillna(myvar['Calories'].mode()[0])

print(new_myvar.to_string())


