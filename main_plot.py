import pandas as pd

url = 'https://github.com/roastduckie/Stationeers-Furnace-Plot/blob/master/recipes.csv'
recipes = pd.read_csv(url, header=0, low_memory=False)
print(recipes)
