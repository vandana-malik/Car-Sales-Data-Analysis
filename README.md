# Car-Sales-Data-Analysis

This is a tool to analyze Used car Sales data. 

Understanding the dataset: Follwing are the features provided in the dataset
price                
model_year         
model           
condition             
cylinders              
fuel             
odometer           
transmission          
type                  
paint_color           
is_4wd              
date_posted 
days_listed 


2 New features are added as required:
a. days_listed - this is dervied by calculating difference between today and 'date_posted'
b. car_complany = this is derived from 'model'


The user has the option to select the fallowing:
1. car manufacturer from the drop down.
2. range of years  (the range in the year adjusts the values based on the car manufactures selected in the previous selection)
3. check box to see if the user wants to see cars with 4wd or not.

Output:
1. The total number items that matches the user selection
2. The data that matches the user selection.

Visualizations:
The user is able to see the histograms and statterplots to visulaize the realationship of the price of teh car with other features.

Instructions to use the repository

Installing
Follow these steps to get the project set up on your local machine:

Clone the repository to your local machine using the following command:

git clone https://github.com/vandana-malik/Car-Sales-Data-Analysis


Navigate to terminal and give the following command to view the dashboard and test it out.
 streamlit run app.py


Web app link: https://car-data-analysis.onrender.com

