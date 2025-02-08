import os
import pandas as pd
import plotly.express as px

if not os.path.exists("images"):
    os.mkdir("images")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1800 or year == 1820")

fig1820 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : '#836394',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03
            )
## fig1820.update_layout(title_text='Birth Places for Descendants of Lawrence before 1840', title_x=0.5)
fig1820.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1820.update_layout(showlegend = False)
fig1820.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1820.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1820.show()
fig1820.write_image("images/birth-map-1820.png")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1840")

fig1840 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : '#836394',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1840.update_layout(title_text='Birth Places for Descendants of Lawrence before 1860', title_x=0.5)
fig1840.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1840.update_layout(showlegend = False)
fig1840.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1840.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1840.show()
fig1840.write_image("images/birth-map-1840.png")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1860")

fig1860 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1860.update_layout(title_text='Birth Places for Descendants of Lawrence 1880', title_x=0.5)
fig1860.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1860.update_layout(showlegend = False)
fig1860.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1860.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1860.show()
fig1860.write_image("images/birth-map-1860.png")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1880")

fig1880 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1880.update_layout(title_text='Birth Places for Descendants of Lawrence before 1900', title_x=0.5)
fig1880.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1880.update_layout(showlegend = False)
fig1880.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1880.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1880.show()
fig1880.write_image("images/birth-map-1880.png")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1900")

fig1900 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1900.update_layout(title_text='Birth Places for Descendants of Lawrence before 1920', title_x=0.5)
fig1900.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1900.update_layout(showlegend = False)
fig1900.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1900.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1900.show()
fig1900.write_image("images/birth-map-1900.png")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1920")

fig1920 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1920.update_layout(title_text='Birth Places for Descendants of Lawrence before 1940', title_x=0.5)
fig1920.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1920.update_layout(showlegend = False)
fig1920.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)

fig1920.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)

## fig1920.show()
fig1920.write_image("images/birth-map-1920.png")


df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1940")

fig1940 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1940.update_layout(title_text='Birth Places for Descendants of Lawrence before 1960', title_x=0.5)
fig1940.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1940.update_layout(showlegend = False)
fig1940.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1940.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1940.show()
fig1940.write_image("images/birth-map-1940.png")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1960")

fig1960 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1960.update_layout(title_text='Birth Places for Descendants of Lawrence before 1980', title_x=0.5)
fig1960.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1960.update_layout(showlegend = False)
fig1960.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1960.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1960.show()
fig1960.write_image("images/birth-map-1960.png")


df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 1980")

fig1980 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig1980.update_layout(title_text='Birth Places for Descendants of Lawrence before 2000', title_x=0.5)
fig1980.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig1980.update_layout(showlegend = False)
fig1980.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig1980.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig1980.show()
fig1980.write_image("images/birth-map-1980.png")

df = pd.read_csv("bmd-data/birth-locations.csv").query("year == 2000")

fig2000 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig2000.update_layout(title_text='Birth Places for Descendants of Lawrence before 2020', title_x=0.5)
fig2000.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig2000.update_layout(showlegend = False)
fig2000.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig2000.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig2000.show()
fig2000.write_image("images/birth-map-2000.png")

df = pd.read_csv("bmd-data/birth-locations.csv")

fig2000 = px.scatter_geo(df, lat='birth-lat', lon='birth-long', hover_name='place', size='count', facet_col='descendant', facet_col_wrap=2,
                        color="descendant",
                        color_discrete_map = {
                            'John': '#219ebc',      # blue
                            'George' : 'RebeccaPurple',   # black
                            'Amelia' : '#ffb703',   # yellow
                            'Elizabeth' : '#fb8500' # orange
            },
            category_orders = {'descendant':['John','Elizabeth','Amelia','George']},
            facet_row_spacing=0.001, # default is 0.03)
            )

## fig2000.update_layout(title_text='Birth Places for Descendants of Lawrence before 2020', title_x=0.5)
fig2000.for_each_annotation(lambda a: a.update(text=a.text.replace("descendant=", "")))
fig2000.update_layout(showlegend = False)
fig2000.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="#999DA0"
)
fig2000.update_layout(
    margin=dict(l=20, r=20, t=20, b=0),
)
## fig2000.show()
fig2000.write_image("images/birth-map.png")
