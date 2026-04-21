import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

if not os.path.exists("images"):
    os.mkdir("images")

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[~df["Death Region"].str.contains('Alive')]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death", font_size=10)
fig.update_traces(node_color = colors_for_nodes)  
fig.update_layout(width=1500)
fig.show()
fig.write_image("images/bmd-sankey-all-dead.png")

#### Generation 1

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[df["Generation"]==1]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 



fig0 = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig0.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death - Generation 1", font_size=10)
fig0.update_traces(node_color = colors_for_nodes)  
fig0.update_layout(width=1500)
fig0.show()
fig0.write_image("images/bmd-sankey-generation-1.png")

#### Generation 2

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[df["Generation"]==2]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 



fig1 = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig1.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death - Generation 2", font_size=10)
fig1.update_traces(node_color = colors_for_nodes)  
fig1.update_layout(width=1500)
fig1.show()
fig1.write_image("images/bmd-sankey-generation-2.png")


#### Generation 3

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[df["Generation"]==3]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 



fig2 = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig2.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death - Generation 3", font_size=10)
fig2.update_traces(node_color = colors_for_nodes)  
fig2.update_layout(width=1500)
fig2.show()
fig2.write_image("images/bmd-sankey-generation-3.png")

#### Generation 4

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[df["Generation"]==4]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 



fig3 = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig3.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death - Generation 4", font_size=10)
fig3.update_traces(node_color = colors_for_nodes)  
fig3.update_layout(width=1500)
fig3.show()
fig3.write_image("images/bmd-sankey-generation-4.png")


#### Generation 5

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[df["Generation"]==5]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 



fig4 = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig4.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death - Generation 5", font_size=10)
fig4.update_traces(node_color = colors_for_nodes)  
fig4.update_layout(width=1500)
fig4.show()
fig4.write_image("images/bmd-sankey-generation-5.png")


#### Generation 6

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[df["Generation"]==6]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 



fig5 = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig5.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death - Generation 6", font_size=10)
fig5.update_traces(node_color = colors_for_nodes)  
fig5.update_layout(width=1500)
fig5.show()
fig5.write_image("images/bmd-sankey-generation-6.png")


#### Generation 7

df = pd.read_csv("bmd-data/sankey-ohara-bmd.csv")

# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# 'India' :'#836394', # medium purple

color_discrete_map = {
                    'BIndia': '#b45248', # indiared
                    'BBurma': '#d48c84', # rosybrown
                    'BSouth East Asia': '#167288', # teal
                    'BAustralia & New Zealand': '#3cb464', # medium sea green
                    'BAfrica': 'lightgrey', # skyblue
                    'BUK & Ireland': '#643c6a', # purple 
                    'BNorth America': '#9bddb1', # aquamarine
                    'BEurope': '#d6cfa2', # goldenrod
                    'BAlive': '#8cdaec', # skyblue
                    'MIndia': '#b45248', # indiared
                    'MBurma': '#d48c84', # rosybrown
                    'MSouth East Asia': '#167288', # teal
                    'MAustralia & New Zealand': '#3cb464', # medium sea green
                    'MAfrica': 'lightgrey', # skyblue
                    'MUK & Ireland': '#643c6a', # purple 
                    'MNorth America': '#9bddb1', # aquamarine
                    'MEurope': '#d6cfa2', # goldenrod
                    'MAlive': '#8cdaec', # skyblue
                    'MUnmarried': '#a89a49', # dark-khaki  
                    'MDied in Childhood' : 'black',
                    'DIndia': '#b45248', # indiared
                    'DBurma': '#d48c84', # rosybrown
                    'DSouth East Asia': '#167288', # teal
                    'DAustralia & New Zealand': '#3cb464', # medium sea green
                    'DAfrica': 'lightgrey', # skyblue
                    'DUK & Ireland': '#643c6a', # purple 
                    'DNorth America': '#9bddb1', # aquamarine
                    'DEurope': '#d6cfa2', # goldenrod
                    'DAlive': '#8cdaec', # skyblue
                    'DAt sea': '#a89a49', # dark-khaki
                 }

filtered_df = df[df["Generation"]==7]

filtered_df["Birth Region"] = 'B' + filtered_df["Birth Region"].astype(str)
filtered_df["Marriage Region"] = 'M' + filtered_df["Marriage Region"].astype(str)
filtered_df["Death Region"] = 'D' + filtered_df["Death Region"].astype(str)

unique_labels = list(filtered_df["Birth Region"].unique()) + list(filtered_df["Marriage Region"].unique()) + list(filtered_df["Death Region"].unique()) 

sankey = filtered_df[["Birth Region","Marriage Region"]].copy()
md = filtered_df[["Marriage Region","Death Region"]].copy()

sankey.rename(columns={"Birth Region": "Source", "Marriage Region" : "Target"}, inplace=True)
md.rename(columns={"Marriage Region" : 'Source', "Death Region": 'Target'}, inplace=True)

sankey = pd.concat([sankey,md])

sankey_inputs = sankey.groupby(["Source","Target"],observed=True).size().reset_index(name='count')

label_to_index ={}
for index,label in enumerate (unique_labels):
  label_to_index[label] = index

source = sankey_inputs["Source"].map(label_to_index)
target = sankey_inputs["Target"].map(label_to_index)
labels = [s[1:] for s in unique_labels]

print (unique_labels)

tmp_colors = (pd.Series(unique_labels)).map(color_discrete_map) 
colors_for_nodes = list(tmp_colors) 



fig6 = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    node = dict(
      pad = 5,
      thickness = 20,
      label = labels,
      line = dict(color = "black", width = 0.5),

    ),
    link = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = sankey_inputs["count"],
  
  ))])

fig6.update_layout(autosize=True,width=800,height=800,title_text="Birth, Marriage and Death - Generation 7", font_size=10)
fig6.update_traces(node_color = colors_for_nodes)  
fig6.update_layout(width=1500)
fig6.show()
fig6.write_image("images/bmd-sankey-generation-7.png")











































