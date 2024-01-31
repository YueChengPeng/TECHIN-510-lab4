"""
Change this to a world clock app
"""

import time
import pytz
import datetime
import streamlit as st
import requests

placeholder = st.empty()

time_zones = [
    "UTC", 
    "US/Eastern", "US/Central", "US/Mountain", "US/Pacific",
    "Europe/London", "Europe/Berlin", "Europe/Moscow",
    "Asia/Tokyo", "Asia/Shanghai", "Asia/Kolkata", "Asia/Dubai",
    "Australia/Sydney", "Australia/Perth",
    "Africa/Johannesburg", "Africa/Cairo", 
    "America/Sao_Paulo", "America/Buenos_Aires",
    "America/Toronto", "America/Mexico_City",
    "Pacific/Auckland", "Pacific/Honolulu"
]

# Streamlit app
st.title("World Clock")

# Layout for time displays and selection boxes - 2 rows, each with 2 columns
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Create separate selection boxes for time zones in each column
tz_selection1 = col1.selectbox("Time Zone 1", time_zones, key='tz1')
tz_display1 = col1.empty()

tz_selection2 = col2.selectbox("Time Zone 2", time_zones, key='tz2')
tz_display2 = col2.empty()

tz_selection3 = col3.selectbox("Time Zone 3", time_zones, key='tz3')
tz_display3 = col3.empty()

tz_selection4 = col4.selectbox("Time Zone 4", time_zones, key='tz4')
tz_display4 = col4.empty()

# Add a separation line
st.markdown("---")

st.title("UNIX Timestamp")

# UNIX Timestamp display
unix_time_display = st.empty()

# Bottom row for UNIX timestamp input and conversion
bottom_col1, bottom_col2 = st.columns(2)
unix_timestamp_input = bottom_col1.text_input("Convert UNIX timestamp to Human time")
converted_time_display = bottom_col2.empty()

# Add a separation line
st.markdown("---")

st.title("Current Weather in Bellevue, WA")
weather_display = st.empty()

weather_base_url = "https://api.weather.gov/points/"
Bellevue_coords = "47.6104,-122.2007"

while True:
    # Update each time display
    if tz_selection1:
        timezone = pytz.timezone(tz_selection1)
        current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        tz_display1.metric("Current Time", current_time)

    if tz_selection2:
        timezone = pytz.timezone(tz_selection2)
        current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        tz_display2.metric("Current Time", current_time)

    if tz_selection3:
        timezone = pytz.timezone(tz_selection3)
        current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        tz_display3.metric("Current Time", current_time)

    if tz_selection4:
        timezone = pytz.timezone(tz_selection4)
        current_time = datetime.datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
        tz_display4.metric("Current Time", current_time)

    # Update UNIX timestamp
    unix_timestamp = int(time.time())
    unix_time_display.metric("UNIX Timestamp", unix_timestamp)

    # Convert and display the entered UNIX timestamp
    if unix_timestamp_input:
        try:
            entered_unix_timestamp = int(unix_timestamp_input)
            human_time = datetime.datetime.fromtimestamp(entered_unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            converted_time_display.metric("Converted Time", human_time)
        except ValueError:
            converted_time_display.error("Invalid UNIX timestamp")
    
    # get weather

    try:
        res_weather = requests.get(weather_base_url + Bellevue_coords)
        res_dict = res_weather.json()

        res_weather_detail = requests.get(res_dict['properties']['forecastHourly']) # use the forecast property to get the weather data
        res_dict = res_weather_detail.json()

        # get date '2024-01-17'
        current_date = datetime.date.today()
        formatted_date = current_date.strftime('%Y-%m-%d')

        # e.g. 2024-01-30T17:00:00, the hour is rounded down
        formatted_hour = datetime.datetime.now().strftime('%Y-%m-%dT%H:00:00')

        # print(datetime.datetime.now())
            
        for period in res_dict["properties"]["periods"]:
            # we are interested in the weather data of the day time of that day
            if period["startTime"].startswith(formatted_hour) and period["endTime"].startswith(formatted_date):
                weather_display.markdown("Hourly weather on " + formatted_hour + ", Bellevue. Fetch real-time data using the weather API from https://api.weather.gov/points/  \n  \n" 
                        + "Temperature: " + str(period["temperature"]) + "°F, relativeHumidity: " + str(period["relativeHumidity"]["value"]) + ", " + period["shortForecast"])
                break
    except Exception as ex:
        print('Exception:')
        print(ex)


    time.sleep(1)