import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d, ColumnDataSource

#  Importing values from XML file in game data
url = 'https://raw.githubusercontent.com/roastduckie/Stationeers-Furnace-Plot/master/recipes.csv'
recipes = pd.read_csv(
    url,
    index_col=0,
    header=0,
    low_memory=False
)

output_file('index.html')
#  making csv usable
source = ColumnDataSource = ColumnDataSource(recipes)
t_min = source.data['Min Temp'].tolist()
t_max = source.data['Max Temp'].tolist()
p_min = source.data['Min Pressure'].tolist()
p_max = source.data['Max Pressure'].tolist()

#  creating the plot
p = figure(
    plot_width=500,
    plot_height=500,
    x_range=(0, 10000),
    title='Furnace Recipes by Temperature vs Pressure',
    x_axis_label='Temperature (K)',
    y_axis_label='Pressure (kPa)',
)

p.y_range = Range1d(0, 10000)

p.patches(
    xs=[t_min, t_min, t_max, t_max],
    ys=[p_min, p_max, p_max, p_min],
    alpha=0.5
)

show(p)
