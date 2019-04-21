from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
start=datetime.datetime(2015,3,2) #start time of collecting datas
end=datetime.datetime(2015,3,10) #end time of collecting datas

df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end) #GOOG is the stock market name of Google stock market

df1=df[df.Close > df.Open]
df2=df[df.Close < df.Open]

p=figure(x_axis_type='datetime',width=1000,height=300,sizing_mode="scale_width") #sizing_mode is responsiveness of graph w.r.t page
p.title.text="CandleSticks Chart"
p.grid.grid_line_alpha=0.3 #Intensity of Grid Lines

hours_12=12*60*60*1000 #Total time(in miliseconds) of market and that will be the width of the rectangle

p.segment(df.index,df.High,df.index,df.Low,color="black")

p.rect(df1.index,(df1.Open+df1.Close)/2, hours_12, abs(df1.Open-df1.Close),fill_color="#CCFFFF",line_color="black")
p.rect(df2.index,(df2.Open+df2.Close)/2, hours_12, abs(df2.Open-df2.Close),fill_color="#FF3333",line_color="black")


output_file("CS.html")
show(p)

#Reference- "Python-The Mega Course,UDEMY"
#For more information/query feel free to contact:-
#Chanchal Kumar
#ckgec98@gmail.com
#Edits Are Welcomed !!
