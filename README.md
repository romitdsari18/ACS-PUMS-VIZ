# ACS-PUMS-VIZ

To create a program in Python that performs the following using the matplotlib and pandas packages:

1. Loads the ss13hil.csv file that contains the PUMS dataset (assume it's in the current directory) and create a Data Frame object from it. 

2. Create a figure with 2x2 subplots. The required subplots are as follows: 

     2.1 Upper Left Subplot - Pie chart containing the number of household records for different values of the HHL (household language) attribute. The plot should have no wedge labels, but     
         should have a legend in the upper left corner. The pie needs to be rotated appropriately (see example figure on last page).
   
     2.2 Upper Right Subplot - Histogram of HINCP (household income) with KDE plot superimposed. You should use a log scale on the x-axis with log-spaced bins (HINT: use np.logspace). 

     2.3 Lower Left Subplot - Bar chart of Thousands of Households for each VEH (vehicles available) value (exclude Nan). Make sure to use the WGTP value to count how many households are 
         represented by each household record and divide the sum by 1000. 

     2.4 Lower Right Subplot - Scatter plot of TAXP (property taxes) vs. VALP (property value). Make sure to convert TAXP into the appropriate numeric value, using the lower bound of the 
         interval (e.g., 2 -> $1, 16 -> $700, …). Use WGTP as the size of each marker, ‘o’ as the marker type, and MRGP (first mortgage payment) as the color value. Add a colorbar. 

3. Display the figure and save it in a file called ‘pums.png’

   # Explaination

1. Initially we have imported the required libraries.

2. Then by using the Pandas data frame we have imported the ‘ss13hil.csv’ file.

3. Then we have created a figure with 2 rows and 2 columns of subplots with a size of 16x12 inches and the title of the charts.

4. Then we have created the four subplots as per requirements.    

5. The first subplot is a pie chart that shows the distribution of household languages. It drops any missing values from the "HHL" column, defines the labels for the pie chart, plots the pie 
   chart, and creates a legend. It also sets the title and y-axis label for the subplot.

6. The second subplot is a histogram of the household income data. It drops any missing values from the "HINCP" column, defines the bins for the histogram using a log scale, plots the 
   histogram, and adds a Gaussian KDE curve. It sets the x-axis scale to log and adds a title, x-axis, and y-axis labels for the subplot. It also formats the y-axis tick labels to six decimal 
   places. 

7. The third subplot is a bar chart that shows the number of vehicles available in households. It groups the data by the number of vehicles and sums the weights (WGTP). It converts the weights 
   to integers and gets the x and y data for the bar chart. It plots the bar chart and adds a title, x-axis, and y-axis labels for the subplot. 

8. The fourth subplot is a scatter plot that shows property taxes versus property values. It selects the necessary columns from the Data Frame and drops any rows with missing values in these 
   columns. It removes any rows where the TAXP column value is 1. It creates a dictionary to convert TAXP values to dollars based on the range of values for each category of TAXP. It converts 
   TAXP column values to dollar amounts using the conversion dictionary. It converts other columns to lists for plotting. It creates a colormap for the scatter plot and plots the scatter plot 
   with various properties set for the plot.

9. Finally, the output is saved in to ‘pums.png’ file


