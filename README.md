# Pokemon-PCA
PCA Analysis of full Pokemon Dataset available on Kaggle

# Step 1) Explore the Data:
- First basic data exploration was done by looking at the head, the columns, datatypes and basic statistics were colected via .describe()
- Then I looked for the Pokemon with highest Speed, Defense and Attack Stats

# Step 2) Plot the Data:
- Interactive 2D plotly plot was made where all Pokemon are plotted for Defense on Y-achsis and Attack on X-achsis
- Interactive 2D plotly plot was made where all Pokemon are plotted for Defense on Y-achsis and Health on X-achsis. Datapoints were coloured dependent on their primary typing.
- Names were kept as labels for datapoints for both plots, so can see which Pokemon it is when your cursor hovers over the data point
![plot](https://github.com/user-attachments/assets/14b8a1e6-acb1-4171-9b14-65df2db0da7f)
![plot2](https://github.com/user-attachments/assets/d3ff6811-f3a9-4807-9229-51fc736883f8)




# Step 3) PCA Analysis:
- A) PCA Analysis with 2 components was first done for simplicity sake. Cumulative explained Variance:  0.63485096
- B) PCA Analysis with 6 components was done. Cumulative explained Variance: 1 => risk of Overfitting?
- Two 3D plots were made of the second PCA with 6 components. First plot shows PC1 vs PC2 vs PC3, second plot shows PC4 vs PC5 vs PC6
- Again, names of the pokemon were used as datapoint labels to be seen when the cursor hovers over the datapoint, the colour of the datapoint is dependent on the primary typing of the Pokemon.
- 3D interactive html plot can be zoomed in/out as well turned around 360 degree achsis in any direction.
![plot6](https://github.com/user-attachments/assets/6bbbe392-c736-434e-8bef-0e5765ce10f5)
![plot62](https://github.com/user-attachments/assets/5b8c27b9-aad1-479b-a1f9-6eb40ff176d7)


