import os
import pandas as pd
import plotly.express as px

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

df = pd.read_csv("bmd-data/ageofdeath.csv")
fig1 = px.line(df, x="Age at death", y="Persons", line_shape='spline',
            color="Descendant",
            color_discrete_map = {
                'John': '#219ebc',      # blue
                'George' : '#023047',   # black
                'Amelia' : '#ffb703',   # yellow
                'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'Descendant':['John','Elizabeth','Amelia','George']},
            title="Cumulative Age at Death for Descendants of Lawrence O'Hara"
    )
fig1.update_layout(
    plot_bgcolor='white'
)
fig1.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey', 
    dtick = 5
)
fig1.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey', 
    dtick = 10
)
fig1.add_hline(y=50, line_dash="dot", line_color="grey")
fig1.update_layout(yaxis_title="Cumulative Percentage of Persons")
fig1.update_layout(title_text="Cumulative Age at Death for Descendants of Lawrence O'Hara", title_x=0.5)
fig1.show()

fig1.write_image("images/cumulative-age-of-death.png")

df = pd.read_csv("bmd-data/ageofdeath-sex.csv").query("Sex == 'Male'")
fig1a = px.line(df, x="Age at death", y="Persons",line_shape='spline',
            color="Descendant",
            color_discrete_map = {
                'John': '#219ebc',      # blue
                'George' : '#023047',   # black
                'Amelia' : '#ffb703',   # yellow
                'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'Descendant':['John','Elizabeth','Amelia','George']}, 
            title="Cumulative Age at Death for Male Descendants of Lawrence O'Hara by "
    )

fig1a.update_layout(
    plot_bgcolor='white'
)
fig1a.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey', 
    dtick = 5
)
fig1a.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey', 
    dtick = 10
)
fig1a.add_hline(y=50, line_dash="dot", line_color="grey")
fig1a.for_each_annotation(lambda a: a.update(text=a.text.replace("Sex=", "")))
fig1a.update_layout(yaxis_title="Cumulative Percentage of Persons")
fig1a.update_layout(title_text="Cumulative Age at Death for Male Descendants of Lawrence O'Hara", title_x=0.5)
fig1a.show()

fig1a.write_image("images/cumulative-age-of-death-male.png")

df = pd.read_csv("bmd-data/ageofdeath-sex.csv").query("Sex == 'Female'")
fig1a = px.line(df, x="Age at death", y="Persons",line_shape='spline',
            color="Descendant",
            color_discrete_map = {
                'John': '#219ebc',      # blue
                'George' : '#023047',   # black
                'Amelia' : '#ffb703',   # yellow
                'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'Descendant':['John','Elizabeth','Amelia','George']}, 
            title="Cumulative Age at Death for Male Descendants of Lawrence O'Hara by "
    )

fig1a.update_layout(
    plot_bgcolor='white'
)
fig1a.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey', 
    dtick = 5
)
fig1a.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey', 
    dtick = 10
)
fig1a.add_hline(y=50, line_dash="dot", line_color="grey")
fig1a.for_each_annotation(lambda a: a.update(text=a.text.replace("Sex=", "")))
fig1a.update_layout(yaxis_title="Cumulative Percentage of Persons")
fig1a.update_layout(title_text="Cumulative Age at Death for Female Descendants of Lawrence O'Hara", title_x=0.5)
fig1a.show()

fig1a.write_image("images/cumulative-age-of-death-female.png")

df = pd.read_csv("bmd-data/birth-range.csv")
fig2 = px.bar(df, x="Birth Range", y="Persons", 
                color="Region",
                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'At sea'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Birth Range':['1800','1820','1840','1860','1880','1900','1920','1940','1960','1980','2000','2020']},
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
                },
                title="Region of Birth for Descendants of Lawrence O'Hara by Time"
    )
fig2.update_layout(legend_traceorder="reversed")

fig2.update_xaxes(type ='category')
fig2.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig2.update_layout(
    plot_bgcolor='white'
)
fig2.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig2.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig2.update_layout(title_text="Region of Birth for Descendants of Lawrence O'Hara by Time", title_x=0.5)
fig2.show()

fig2.write_image("images/birth-range.png")

df = pd.read_csv("bmd-data/birth-range.csv").query("Descendant == 'John'")
fig2j = px.bar(df, x="Birth Range", y="Persons", 
                color="Region",
##                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'At sea'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Birth Range':['1800','1820','1840','1860','1880','1900','1920','1940','1960','1980','2000','2020']},
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
                },
                title="Region of Birth for Descendants of Lawrence O'Hara by Time"
    )
fig2j.update_layout(legend_traceorder="reversed")

fig2j.update_xaxes(type ='category')
fig2j.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig2j.update_layout(
    plot_bgcolor='white'
)
fig2j.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig2j.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig2j.update_layout(title_text="Region of Birth for Descendants of John O'Hara by Time", title_x=0.5)
fig2j.show()

fig2j.write_image("images/birth-range-john.png")

df = pd.read_csv("bmd-data/birth-range.csv").query("Descendant == 'Elizabeth'")
fig2e = px.bar(df, x="Birth Range", y="Persons", 
                color="Region",
##                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'At sea'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Birth Range':['1800','1820','1840','1860','1880','1900','1920','1940','1960','1980','2000','2020']},
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
                },
                title="Region of Birth for Descendants of Lawrence O'Hara by Time"
    )
fig2e.update_layout(legend_traceorder="reversed")

fig2e.update_xaxes(type ='category')
fig2e.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig2e.update_layout(
    plot_bgcolor='white'
)
fig2e.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig2e.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig2e.update_layout(title_text="Region of Birth for Descendants of Elizabeth O'Hara by Time", title_x=0.5)
fig2e.show()

fig2e.write_image("images/birth-range-elizabeth.png")

df = pd.read_csv("bmd-data/birth-range.csv").query("Descendant == 'Amelia'")
fig2a = px.bar(df, x="Birth Range", y="Persons", 
                color="Region",
##                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'At sea'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Birth Range':['1800','1820','1840','1860','1880','1900','1920','1940','1960','1980','2000','2020']},
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
                },
                title="Region of Birth for Descendants of Lawrence O'Hara by Time"
    )
fig2a.update_layout(legend_traceorder="reversed")

fig2a.update_xaxes(type ='category')
fig2a.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig2a.update_layout(
    plot_bgcolor='white'
)
fig2a.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig2a.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig2a.update_layout(title_text="Region of Birth for Descendants of Amelia O'Hara by Time", title_x=0.5)
fig2a.show()

fig2a.write_image("images/birth-range-amelia.png")

df = pd.read_csv("bmd-data/birth-range.csv").query("Descendant == 'George'")
fig2g = px.bar(df, x="Birth Range", y="Persons", 
                color="Region",
##                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'At sea'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Birth Range':['1800','1820','1840','1860','1880','1900','1920','1940','1960','1980','2000','2020']},
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
                },
                title="Region of Birth for Descendants of Lawrence O'Hara by Time"
    )
fig2g.update_layout(legend_traceorder="reversed")

fig2g.update_xaxes(type ='category')
fig2g.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig2g.update_layout(
    plot_bgcolor='white'
)
fig2g.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig2g.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig2g.update_layout(title_text="Region of Birth for Descendants of George O'Hara by Time", title_x=0.5)
fig2g.show()

fig2g.write_image("images/birth-range-george.png")

df = pd.read_csv("bmd-data/death-range.csv")
fig2b = px.bar(df, x="Death Range", y="Persons", 
                color="Region",
                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'At sea'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Death Range':['1820','1840','1860','1880','1900','1920','1940','1960','1980','2000','2020']},
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
                },
                title="Region of Death for Descendants of Lawrence O'Hara by Time"
    )
fig2b.update_layout(legend_traceorder="reversed")

fig2b.update_xaxes(type ='category')
fig2b.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig2b.update_layout(
    plot_bgcolor='white'
)
fig2b.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig2b.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig2b.update_layout(title_text="Region of Death for Descendants of Lawrence O'Hara by Generation", title_x=0.5)
fig2b.show()

fig2b.write_image("images/death-range.png")

df = pd.read_csv("bmd-data/all-births.csv")

fig3 = px.bar(df, x="Generation", y="Persons",
                color="Region",
                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'At sea'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Generation':['1','2','3','4','5','6','7','8']},
                color_discrete_map = {
                    'India': '#b45248', # indiared
                    'Burma': '#d48c84', # rosybrown
                    'South East Asia': '#167288', # teal
                    'Australia & New Zealand': '#3cb464', # medium sea green
                    'Africa': '#8cdaec', # skyblue
                    'UK & Ireland': '#643c6a', # purple 
                    'North America': '#9bddb1', # aquamarine
                    'Europe': '#d6cfa2', # goldenrod
                    'Alive': '#8cdaec', # skyblue
                    'At sea': '#a89a49', # dark-khaki
                },
                title="Region of Birth for Descendants of Lawrence O'Hara by Generation"
    )
fig3.update_layout(legend_traceorder="reversed")
fig3.update_xaxes(type ='category')
fig3.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig3.update_layout(
    plot_bgcolor='white'
)
fig3.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig3.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig3.update_layout(title_text="Region of Birth for Descendants of Lawrence O'Hara by Generation", title_x=0.5)
fig3.show()
fig3.write_image("images/births-gen.png")

df = pd.read_csv("bmd-data/all-deaths.csv")

fig4 = px.bar(df, x="Generation", y="Persons",
                color="Region",
                facet_col="Descendant",
                category_orders = {'Region':['India','Burma','South East Asia','North America','UK & Ireland','Australia & New Zealand','Africa','Europe', 'Alive'],
                                   'Descendant':['John','Elizabeth','Amelia','George'],
                                   'Generation':['1','2','3','4','5','6','7','8']},
                color_discrete_map = {
                     'India': '#b45248', # indiared
                    'Burma': '#d48c84', # rosybrown
                    'South East Asia': '#167288', # teal
                    'Australia & New Zealand': '#3cb464', # medium sea green
                    'Africa': '#8cdaec', # skyblue
                    'UK & Ireland': '#643c6a', # purple 
                    'North America': '#9bddb1', # aquamarine
                    'Europe': '#d6cfa2', # goldenrod
                    'Alive': 'mistyrose', 
                    'At sea': '#a89a49', # dark-khaki
                },
                title="Region of Death for Descendants of Lawrence O'Hara by Generation"

    )
fig4.update_layout(legend_traceorder="reversed")
fig4.update_xaxes(type ='category')
fig4.for_each_annotation(lambda a: a.update(text=a.text.replace("Descendant=", "")))
fig4.update_layout(
    plot_bgcolor='whitesmoke'
)
fig4.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black'
)
fig4.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey'
)
fig4.update_layout(title_text="Region of Death for Descendants of Lawrence O'Hara by Generation", title_x=0.5)
fig4.show()
fig4.write_image("images/deaths-gen.png")


