from bokeh.models.annotations import Tooltip
from capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource  

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") #converts datetime to string for start time
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S") #converts datetime to string for end time

cds=ColumnDataSource(df) #data source

p=figure(x_axis_type='datetime', height=300, width=1000, title="Motion Graph") #settings for the graph

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")]) #display when hovered, however needs string instead of datetime
p.add_tools(hover)

q=p.quad(left="Start",right="End", bottom=0, top=1, color="green", source=cds) #create barchart from source 

output_file("Graph1.html") 
show(p) #display result