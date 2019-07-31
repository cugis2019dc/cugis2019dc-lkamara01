# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:16:34 2019

@author: STEM
"""

cadburybox(m,d,w)
cadburybox = ("6 milk chocolate", "5 dark chocolate", "8 white chocolate")
print("There are", m, "," d, ",", "and", w)
    
cami = "6 milk chocolates"
cada = "5 dark chocolates"
cawhi = "and 8 white chocolates"

def cadbox(m,d,w):
    print("There are",m,",",d,",",w)
    
cadbox(cami,cada,cawhi)

c1 = "dark"
c2 = "milk"
c3 = "white"

dark = 5
milk = 6
white =8

#dict
choc1 = {"milk chocolate":5}
choc2 = {"dark chocolate":8}
choc3 = {"white chocolate":3}
print("there are", choc1, ",", choc2, ",", "and", choc3)

chocbox = {"dark":5,"milk":6,"white":8}

a1 = {"age":32}
a2 = {"age": 28}
a3 = {"age":45}
a4 = {"age":38}
print("steve is", a1, "lia is", a2, "vin is", "and katie is", a4)

ages = {"steve is":32,", lia is":28, ", vin is":45, "and katie is":38}
ages

gender = {"steve":"m","lia":"f","vin":"m","katie":"f"}
gender

#learning how to use lists
studentlist = [['steve',32,'M'],["lia",28,"F"],["vin",45,"M"],['katie',38,"F"]]
studentlist

import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
studentdf

chocolist = [["milk",5],["dark",8],["white",3]]
chocolist

chocolistdf = pandas.DataFrame(chocolist,columns=("choc type","quantity"))
chocolistdf

#referencing
studentdf["name"]
studentdf["age"]
studentdf["gender"]

chocolistdf["choc type"]
chocolistdf["quantity"]

studentlist2 = [["steve",32,"m"],["lia",28,"f"],["vin",45,"m"],["katie",38,"f"]]
studentlist2

studentdf2 = pandas.DataFrame(studentlist2,columns=("name","age","gender"),index=["1","2","3","4"])
studentdf2

#plotting data

import plotly
dir(plotly)
from plotly.offline import plot




#proxy for long names
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf2["name"],y=studentdf2["age"])
plot([studentbar])


chocobar = go.Bar(x=chocolistdf["choc type"],y=chocolistdf["quantity"])
plot([chocobar])

titles = go.Layout(title = "number of chocolates by type")

fig = go.Figure(data=[chocobar], layout=titles)
plot(fig)


























