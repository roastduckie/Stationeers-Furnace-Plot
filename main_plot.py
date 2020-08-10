import pandas as pd
from bokeh.layouts import row
from bokeh.models import ColumnDataSource, HoverTool, Range1d
from bokeh.palettes import Colorblind5
from bokeh.plotting import figure, output_file, show

#  Importing values from XML file in game data
url = 'https://raw.githubusercontent.com/roastduckie/Stationeers-Furnace-Plot/master/recipes.csv'
df = pd.read_csv(
    url,
    index_col=0,
    header=0,
    low_memory=False
)

output_file('index.html')
#  making csv usable
source = ColumnDataSource(df)

hover = HoverTool()
hover.tooltips = [
    ('Minimum Pressure: ', '@MinPressure'),
    ('Maximum Pressure: ', '@MaxPressure'),
    ('Minimum Temperature: ', '@MinTemp'),
    ('Maximum Temperature: ', '@MaxTemp'),
    ('Materials: ', '@Materials')
]

#  creating the plot
standard = figure(
    plot_width=500,
    plot_height=500,
    x_range=(0, 2500),
    title='Standard Alloy Temperatures and Pressures',
    x_axis_label='Temperature (K)',
    y_axis_label='Pressure (kPa)',
)

standard.y_range = Range1d(0, 10000)

xs_standard = []
ys_standard = []
for i in range(7, 12, 1):
   xs_standard.append([df.iloc[i, 2], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 3]])
   ys_standard.append([df.iloc[i, 0], df.iloc[i,1], df.iloc[i,1], df.iloc[i,0]])

standard.patches(
    xs=xs_standard,
    ys=ys_standard,
    alpha=0.2
)

standard.add_tools(hover)

Super = figure(
    plot_width=500,
    plot_height=500,
    x_range=(0, 2500),
    title='Super Alloy Temperatures and Pressures',
    x_axis_label='Temperature (K)',
    y_axis_label='Pressure (kPa)',
)

Super.y_range = Range1d(0, 6000)

xs_super = []
ys_super = []
for i in range(12, 17, 1):
   xs_super.append([df.iloc[i, 2], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 3]])
   ys_super.append([df.iloc[i, 0], df.iloc[i,1], df.iloc[i,1], df.iloc[i,0]])

Super.patches(
    xs=xs_super,
    ys=ys_super,
    alpha=0.2
)
Super.add_tools(hover)

# show(row(standard, Super))
