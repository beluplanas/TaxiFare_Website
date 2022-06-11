import streamlit as st
import datetime
import requests
import pandas as pd

'''
# NY TAXI
'''
st.markdown('''
### No more suprises,
### Calculate the cost of the taxi and compare it with UBER''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
'''
date = st.date_input(
    "Date of pick up",datetime.date.today())
st.write('We will pick you up this day:', date)

time = st.time_input('Time of pick up', datetime.time())
st.write('at this time', time)

pickup_longitude = st.number_input('Pickup longitude',40.75998)
st.write('Pickup longitude ', pickup_longitude)

pickup_latitude = st.number_input('Pickup latitude',-73.9821659)
st.write('Pickup latitude ', pickup_latitude)

dropoff_longitude = st.number_input('Dropoff longitude',40.6600467)
st.write('Dropoff longitude ', dropoff_longitude)

dropoff_latitude = st.number_input('Dropoff latitude',-74.1736653)
st.write('Dropoff latitude ', dropoff_latitude)

passenger_count = st.number_input('Amount of passengers',max_value=4, min_value=1,value=1)
st.write('Amount of passengers ', passenger_count)


url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

#st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


pickup_datetime = f'{date} {time}'

#2. Let's build a dictionary containing the parameters for our API...
data = {'pickup_datetime' : pickup_datetime,
        'pickup_longitude':pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count}

api_data = requests.get(url,params=data).json()

fare = api_data['fare']

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
st.write('Your fare will be',fare)
