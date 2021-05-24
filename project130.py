import pandas as pd
import csv

df = pd.read_csv("project129_final.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name2"]
del df["Distance2"]
del df["Mass2"]
del df["Radius2"]

print(df.shape)

print(list(df))
['Star_name', 'Distance', 'Mass', 'Radius']
df = df.rename({
    "Star_name":"name_of_star",
    "Mass":"planet_mass",
    "Radius":"planet_radius",

},axis = "columns")

df.to_csv("project130_2.csv")