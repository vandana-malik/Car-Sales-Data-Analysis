import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px



st.header('Used cars sales market')
st.write('Filter the data below to see the data by manufacturer')


data = pd.read_csv('vehicles_us.csv')


# fixing data
data['is_4wd'] = data['is_4wd'].fillna('0')
data['paint_color'] = data['paint_color'].fillna('unknown')

data.dropna(inplace=True)

data['is_4wd'] = data['is_4wd'].astype(int)
data['model_year'] = data['model_year'].astype(int)
data['cylinders'] = data['cylinders'].astype(int)
data['date_posted'] = pd.to_datetime(data['date_posted'], format='%Y-%m-%d')




 # extract car company name from the model information
data['car_company'] = data['model'].str.split(' ').str[0]
company = data['car_company'].unique()

selected_menu = st.selectbox('Select a manufacturer', company )

#min and max for the car model selected by the user

year = data.loc[data['car_company'] == selected_menu, 'model_year']
min_year, max_year = int(year.min()), int(year.max())

year_range = st.slider("Choose model year", value=(min_year, max_year), min_value=min_year,max_value= max_year)
selected_range = list(range(year_range[0], year_range[1]+1))

#Create a checkbox widget
checkbox = st.checkbox('Do you want to see 4 wheel drive?', value=True)
checkbox_value = []
if checkbox == True:
    checkbox_value = 1
else:
    checkbox_value = 0


data_filtered = data[(data.car_company == selected_menu) & (data.model_year.isin(list(selected_range))) & (data.is_4wd == checkbox_value)]
item_count = len(data_filtered)
st.write(item_count,'Items found')

data_filtered


st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distibution of price varies depending on  transmission, cylinders, type and condition
""")

list_for_hist = ['transmission','cylinders','type','condition']

selected_type = st.selectbox('Split for price distribution',list_for_hist)

fig1 = px.histogram(data, x="price",color = selected_type )
fig1.update_layout(title= "<b> Price DIstribution by {}</b>".format(selected_type))
st.plotly_chart(fig1)


def age_category(x):
    if x<5: return '<5'
    elif  x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'

data['age'] = 2024 - data['model_year']

data['age_category'] = data['age'].apply(age_category)

list_for_scatter = ['odometer','model_year','days_listed']

choice_for_scatter = st.selectbox('Price dependency on',list_for_scatter)

fig2 = px.scatter(data, x="price", y=choice_for_scatter, color ="age_category",hover_data=['model_year'])
fig2.update_layout(title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)