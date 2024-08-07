# -*- coding: utf-8 -*-

#Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from scipy import stats

#Reading the data file
pums_df = pd.read_csv('ss13hil.csv')

#Creating a figure with 2 rows and 2 columns of subplots and setting the size of the figure to 16x12 inches
figure, axis = plt.subplots(2, 2, sharex=False, sharey=False, figsize=(16, 12))

#Setting the title of the figure
figure.suptitle("Output", fontsize=16)

#Ploting a pie chart of the household languages
#Droping missing values from the 'HHL' column
pie_data = pums_df['HHL'].dropna()
#Defing the labels for the pie chart
keys = ['English only', 'Spanish', 'Other Indo-European', 'Asian and Pacific Island languages', 'Other']
#Ploting the pie chart and create a legend
patches, texts = axis[0][0].pie(pie_data.value_counts().values, startangle=-120)
axis[0][0].legend(patches, keys, loc="upper left")
#Setting the title and y-axis label for the subplot
axis[0][0].set_title('Household Languages', loc='center')
axis[0][0].set_ylabel('HHL')

#Ploting a histogram of the household income data
#Droping missing values from the 'HINCP' column
hist_data = pums_df['HINCP'].dropna()
#Defing the bins for the histogram using a log scale
bins = np.logspace(np.log10(10), np.log10(10**7), 100)
#Ploting the histogram and add a Gaussian KDE curve
axis[0][1].hist(hist_data, bins=bins, density=True, alpha=0.5, color='g')
kde = stats.gaussian_kde(hist_data)
axis[0][1].grid()
axis[0][1].plot(bins, kde(bins), color='black', linestyle='--', linewidth=1)
#Setting the x-axis scale to log and add title, x-axis and y-axis labels for the subplot
axis[0][1].set_xscale('log')
axis[0][1].set_title('Distribution of Household Income')
axis[0][1].set_ylabel('Density')
axis[0][1].set_xlabel('Household Income($)- Log Scaled')
#Formating the y-axis tick labels to six decimal places
axis[0][1].yaxis.set_major_formatter(FormatStrFormatter('%.6f'))

#Ploting a bar chart of the number of vehicles available in households
#Grouping the data by the number of vehicles and sum the weights (WGTP)
bar_data = pums_df.groupby('VEH')['WGTP'].sum() / 1000
#Converting the weights to integers
data = bar_data.apply(int)
#Getting the x and y data for the bar chart
veh = data.index
wgtp = data.values
#Ploting the bar chart and add title, x-axis and y-axis labels for the subplot
axis[1][0].bar(veh, wgtp, color='red', width=0.9)
axis[1][0].set_title('Vehicles Available in Households')
axis[1][0].set_ylabel('Thousands of Households')
axis[1][0].set_xlabel('# of Vehicles')

#ploting a scatter plot of property taxes versus property

#Selecting the necessary columns from the DataFrame and drop any rows with missing values in these columns
scatter_data = pums_df[['VALP', 'TAXP', 'WGTP', 'MRGP']].dropna()

#Removing any rows where TAXP column value is 1
scatter_data = scatter_data[scatter_data.TAXP != 1]

#Create a dictionary to convert TAXP values to dollars
#The conversion is based on the range of values for each category of TAXP
#The resulting dictionary will be used to replace TAXP values with dollar amounts
conversion_dictionary = {}
for i in range(2, 69):
    if i == 2:
        conversion_dictionary[i] = 1
    elif i <= 22:
        conversion_dictionary[i] = (i - 2) * 50
    elif 23 <= i <= 62:
        conversion_dictionary[i] = 1000 + (i - 22) * 100
    else:
        conversion_dictionary[i] = 5000 + (i - 63) * 1000

#Converting TAXP column values to dollar amounts using the conversion_dictionary
taxp = [conversion_dictionary[x] for x in scatter_data['TAXP'].tolist()]

#Converting other columns to lists for plotting
valp = scatter_data['VALP'].tolist()
wgtp = [x / 8 for x in scatter_data['WGTP'].tolist()]
mrgp = scatter_data['MRGP'].tolist()

#Creating a colormap for the scatter plot
cmap = plt.cm.get_cmap('coolwarm')

#Ploting the scatter plot and set various properties of the plot
im = axis[1][1].scatter(valp, taxp, s=wgtp, c=mrgp, vmin=0, vmax=5000, cmap=cmap, alpha=0.5)
axis[1][1].set_title('Property Taxes vs. Property Values', fontsize=10)
axis[1][1].set_xlabel('Property Value ($)', fontsize=8)
axis[1][1].set_ylabel('Taxes ($)', fontsize=8)
axis[1][1].set_xlim(0, 1200000)
axis[1][1].tick_params(axis='both', labelsize=8)

#Adding a colorbar to the plot and set various properties of the colorbar
cbar = figure.colorbar(im, ax=axis[1][1])
cbar.ax.set_ylabel('First Mortgage Payment (Monthly $)', fontsize=8)
cbar.ax.tick_params(axis='both', labelsize=8)

#Saving the plot to a pums.png file in Landscape mode
plt.savefig('pums.png', orientation='landscape', bbox_inches='tight')
