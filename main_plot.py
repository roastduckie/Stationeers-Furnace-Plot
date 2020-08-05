import pandas as pd

url = 'https://raw.githubusercontent.com/roastduckie/Stationeers-Furnace-Plot/master/recipes.csv'
recipes = pd.read_csv(url, index_col=0, header=0, low_memory=False)
print(recipes)
