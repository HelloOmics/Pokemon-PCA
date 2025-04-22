# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 10:50:45 2025

@author: Hello0mics
"""
import os

# Ask Current directory
current_directory = os.getcwd()
print(current_directory)

# if needed change current directory
os.chdir(r"C:\Users\roxan\OneDrive\Desktop\Masters_Biology_FU\DIY_data_science\datasets\Pokemon")


#import csv file
import pandas as pd
data = pd.read_csv(r"C:\Users\roxan\OneDrive\Desktop\Masters_Biology_FU\DIY_data_science\datasets\Pokemon\all_pokemon_data.csv") 
# don't forget to add .csv afetr file name or won't be able to find it

# view the data
print(data.head()) # Displays first 5 rows
print(data.columns) # displays all column names

data.info()
data.describe() # calculate statistics: count/mean/std/min/perecntiles/max

# to explore df further open data in variable explorer

#-----------------------------------------------------------------------------

# Which pokemon are the fastest? Highest Defense? etc?

#-----------------------------------------------------------------------------

# what is the highest value for speed?
max_value_Speed = data['Speed'].max()

# Query all rows where column 'xyz' is equal to the maximum value
result_Speed = data[data['Speed'] == max_value_Speed]

# Display the result
print(result_Speed) # regieleki is the fastest 

#-----------------

print(data.columns) # choose Defense

# Find the maximum value in column 'xyz' => Defense
max_value_Defense = data['Defense'].max()

# Query all rows where column 'xyz' is equal to the maximum value
result_Defense = data[data['Defense'] == max_value_Defense]

# Display the result
print(result_Defense) 
# steelix-mega, shuckle, aggron-mega

#----------

print(data.columns) # look for proper column name = Attack

# Find the maximum value in column 'xyz' => Attack
max_value_att = data['Attack'].max()

# Query all rows where column 'xyz' is equal to the maximum value
result_att = data[data['Attack'] == max_value_att]

# Display the result
print(result_att)

#---------------------------------------------------------------------------
# Let's plot all pokemon comparing Defense & Attack!
# Add names as labels, interactive 2D Plot
#--------------------------------------------------------------------------

import plotly.express as px

# create the plot, choose from bar, scatter, line etc
# add each pokemon name as a label
fig = px.scatter(data, x='Defense', y='Attack', title='Glass Cannons vs Tanks', 
                 hover_name='Name')

#Customize Your Plot: Add titles, labels, or modify aesthetics.
fig.update_layout(
    xaxis_title="Defense",
    yaxis_title="Attack",
    title_font=dict(size=20),
    template="plotly_dark" # applies dark theme
    )

# show your figure
fig.show() # spyder is having difdiculty in rendering/showing the plot?

# open plot as an html file
fig.write_html("plot.html")

import webbrowser

# Path to the HTML file
file_path = "plot.html"

# Open the file in the default web browser
webbrowser.open(file_path)

#---------------------------------------------------------------------------
# Let's plot all pokemon comparing Defense & Health!
# Add names as labels, interactive 2D Plot
# this time also colour code the data points for their primary typing
#-----------------------------------------------------------------------------

# create the plot, choose from bar, scatter, line etc
# include pokemon name as a label + primary typing
fig2 = px.scatter(data, x='Defense', y='Health', title='Defense Tanks vs Health Tanks', 
                 hover_name='Name', color="Primary Typing")

#Customize Your Plot: Add titles, labels, or modify aesthetics.
fig2.update_layout(
    xaxis_title="Defense",
    yaxis_title="Attack",
    title_font=dict(size=20),
    template="plotly_dark" # applies dark theme
    )

# show you figure
fig2.show() # spyder is having difdiculty in rendering/showing the plot?

# open plot as an html file
fig2.write_html("plot2.html")

import webbrowser

# Path to the HTML file
file_path2 = "plot2.html"

# Open the file in the default web browser
webbrowser.open(file_path2)

#----------------------------------------------------------------------------
# Let's do our first PCA to cluster the data points
# use all numerical dats (PCA only works on numerical)
# Apply dimensionality reduction via PCA with only 2 principal components
# start simple then add complexity
#-----------------------------------------------------------------------------

import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: load + subset data set
# --> loading in this case already done = data variable
# PCA can only be done for numerical data, need to make a subset of numerical data only
print(data.columns) # check column names for further selection of data subset
subset_data = data[["Health", "Attack", "Defense", "Special Attack", "Special Defense",
                   "Speed"]]
# add double brackets:
#you need to pass a list of column names instead of a tuple. 
#Tuples are not the correct format for column indexing in pandas DataFrames.
# other way possible:
# columns_to_keep = ["Health", "Attack", "Defense", "Special Attack", "Special Defense",
#                   "Speed",]
#subset_data = data[columns_to_keep]


# Step 2: Save names for labels later
names = data['Name'] 
types = data["Primary Typing"] 
# our numerical subset no loner contains names
# so need to save for reattaching and plotting 


# Step 3: Standardize the data
scaler = StandardScaler() 
subset_scaled = scaler.fit_transform(subset_data)

# Step 4: Apply PCA
pca = PCA(n_components=2) # keep 2, start simple then add complexity
principal_components = pca.fit_transform(subset_scaled)


# Step 5: Create a Dataframe for PCA results
pca_result = pd.DataFrame(data =  principal_components, columns =["PC1", "PC2"])
print(pca_result)
pca_result['Name'] = names  # Add the names back
pca_result["Primary Typing"] = types
print(pca_result)

# Step 6: How much variance does our model describe?
# is model a good fit?
# should we add more principal components to add more complexity?
# -> often the case necessary when analysing genetic data

print("Explained Variance Ratio:", pca.explained_variance_ratio_)
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)
# first two components explain 45% and 18% of the variance found in the data
# [0.451811   0.18303996]

cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
print("Cumulative explained variance:", cumulative_variance)

#-----------------------------------------------------------------------------
# Let's use 6 components for our PCA
# will moer complexity explain the variance in our data better?
#---------------------------------------------------------------------------

# First 3 steps stay the same, are using the same data

# Step 4: Apply PCA
pca6 = PCA(n_components=6) 
principal_components = pca6.fit_transform(subset_scaled)


# Step 5: Create a Dataframe for PCA results
pca_result6 = pd.DataFrame(data =  principal_components, columns =["PC1", "PC2",
                                                                   "PC3", "PC4",
                                                                   "PC5", "PC6"])
print(pca_result6)
pca_result6['Name'] = names  # Add the names back
pca_result6['Primary Typing'] = types # Add the typing back
print(pca_result6)

#Step 6: Analyze Explained Variance
print("Explained Variance Ratio:", pca6.explained_variance_ratio_) 

# How to check cumulative variance 
cumulative_variance = np.cumsum(pca6.explained_variance_ratio_)
print("Cumulative explained variance:", cumulative_variance)

plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance)
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Choosing the Optimal Number of Components')
plt.grid()
plt.show()
# 6 components explain 100% the variance in the data
# overfitting?

# Step 7 Visualisations
import plotly.express as px

# first thre components of PCA6
fig6 = px.scatter_3d(
    pca_result6, 
    x='PC1', 
    y='PC2', 
    z='PC3', 
    hover_name='Name',  # Use names as labels
    title='PCA 3D Visualization',
    color="Primary Typing",
    template="plotly_dark" 

)

# open plot as an html file
fig6.write_html("plot6.html")

import webbrowser

# Path to the HTML file
file_path6 = "plot6.html"

# Open the file in the default web browser
webbrowser.open(file_path6)


#------- Visualise PC4/5/6

fig62 = px.scatter_3d(
    pca_result6, 
    x='PC4', 
    y='PC5', 
    z='PC6', 
    hover_name='Name',  # Use names as labels
    title='PCA 3D Visualization',
    color="Primary Typing",
    template="plotly_dark" 

)

# open plot as an html file
fig62.write_html("plot62.html")

import webbrowser

# Path to the HTML file
file_path62 = "plot62.html"

# Open the file in the default web browser
webbrowser.open(file_path62)


