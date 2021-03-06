from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.autompg import autompg as df

p = Scatter(df, x='mpg', y='hp', title="HP vs MPG",
            xlabel="Miles Per Gallon", ylabel="Horsepower")

p.logo = None # remove Bokeh's logo

output_file("scatter.html")

show(p)