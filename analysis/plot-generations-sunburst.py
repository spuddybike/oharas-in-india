import os
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

if not os.path.exists("images"):
    os.mkdir("images")

# 'India': '#b45248', # indiared
# 'Burma': '#d48c84', # rosybrown
# 'South East Asia': '#167288', # teal
# 'Australia & New Zealand': '#3cb464', # medium sea green
# 'Africa': '#8cdaec', # skyblue
# 'UK & Ireland': '#643c6a', # purple 
# 'North America': '#9bddb1', # aquamarine
# 'Europe': '#d6cfa2', # goldenrod
# 'Alive': 'mistyrose', 
# 'At sea': '#a89a49', # dark-khaki
# '#836394', # medium purple

# 'John': '#219ebc',      # blue
# 'George' : '#023047',   # black
# 'Amelia' : '#ffb703',   # yellow
# 'Elizabeth' : '#fb8500' # orange



df = pd.read_csv("bmd-data\bmds-generation.csv").query('Descendant == "John"')
fig4=px.sunburst(df, path=['Descendant','Generation',"Birth Region","Death Region"], values='count', color='Birth Region',
                 color_discrete_map = {
                    'India': '#b45248', # indiared
                    'Burma': '#d48c84', # rosybrown
                    'South East Asia': '#167288', # teal
                    'Australia & New Zealand': '#3cb464', # medium sea green
                    'Africa': 'lightgrey', # skyblue
                    'UK & Ireland': '#643c6a', # purple 
                    'North America': '#9bddb1', # aquamarine
                    'Europe': '#d6cfa2', # goldenrod
                    'Alive': '#8cdaec', # skyblue
                    'At sea': '#a89a49', # dark-khaki
                })
fig4.update_traces(sort=False, selector=dict(type='sunburst'))
fig4.update_traces(textfont=dict(family="Arial", size=8),insidetextorientation='radial')

fig4.show()
fig4.write_image("images/bmds-john.png")

df = pd.read_csv("bmd-data\bmds-generation.csv").query('Descendant == "George"')
fig5=px.sunburst(df, path=['Descendant','Generation',"Birth Region","Death Region"], values='count', color='Birth Region',
                 color_discrete_map = {
                    'India': '#b45248', # indiared
                    'Burma': '#d48c84', # rosybrown
                    'South East Asia': '#167288', # teal
                    'Australia & New Zealand': '#3cb464', # medium sea green
                    'Africa': 'lightgrey', # skyblue
                    'UK & Ireland': '#643c6a', # purple 
                    'North America': '#9bddb1', # aquamarine
                    'Europe': '#d6cfa2', # goldenrod
                    'Alive': '#8cdaec', # skyblue
                    'At sea': '#a89a49', # dark-khaki
                })
fig5.update_traces(sort=False, selector=dict(type='sunburst'))
fig5.update_traces(textfont=dict(family="Arial", size=8),insidetextorientation='radial')
fig5.show()
fig5.write_image("images/bmds-george.png")

df = pd.read_csv("bmd-data\bmds-generation.csv").query('Descendant == "Amelia"')
fig4=px.sunburst(df, path=['Descendant','Generation',"Birth Region","Death Region"], values='count', color='Birth Region',
                 color_discrete_map = {
                    'India': '#b45248', # indiared
                    'Burma': '#d48c84', # rosybrown
                    'South East Asia': '#167288', # teal
                    'Australia & New Zealand': '#3cb464', # medium sea green
                    'Africa': 'lightgrey', # skyblue
                    'UK & Ireland': '#643c6a', # purple 
                    'North America': '#9bddb1', # aquamarine
                    'Europe': '#d6cfa2', # goldenrod
                    'Alive': '#8cdaec', # skyblue
                    'At sea': '#a89a49', # dark-khaki
                })
fig4.update_traces(sort=False, selector=dict(type='sunburst'))
fig4.update_traces(textfont=dict(family="Arial", size=8),insidetextorientation='radial')
fig4.show()
fig4.write_image("images/bmds-amelia.png")

df = pd.read_csv("bmd-data\bmds-generation.csv").query('Descendant == "Elizabeth"')
fig5=px.sunburst(df, path=['Descendant','Generation',"Birth Region","Death Region"], values='count', color='Birth Region',
                 color_discrete_map = {
                    'India': '#b45248', # indiared
                    'Burma': '#d48c84', # rosybrown
                    'South East Asia': '#167288', # teal
                    'Australia & New Zealand': '#3cb464', # medium sea green
                    'Africa': 'lightgrey', # skyblue
                    'UK & Ireland': '#643c6a', # purple 
                    'North America': '#9bddb1', # aquamarine
                    'Europe': '#d6cfa2', # goldenrod
                    'Alive': '#8cdaec', # skyblue
                    'At sea': '#a89a49', # dark-khaki
                })
fig5.update_traces(sort=False, selector=dict(type='sunburst'))
fig5.update_traces(textfont=dict(family="Arial", size=8),insidetextorientation='radial')
fig5.show()
fig5.write_image("images/bmds-elizabeth.png")
## fig4.update_layout(title_text='EDDI Participants 2008-2024', title_x=0.5)
## fig4.update_traces(textfont=dict(family="TimesRoman", size=9),insidetextorientation='radial')

