import streamlit as st
import datetime
import matplotlib.pyplot as plt
import random

def generate_dummy_weather():
    forecast_data = {'list': []}
    current_time = datetime.datetime.now()
    for i in range(10):
        entry = {
            'dt': (current_time + datetime.timedelta(hours=i * 6)).timestamp(),
            'main': {'temp': round(random.uniform(15, 35), 1), 'humidity': random.randint(40, 80)},
            'weather': [{'description': random.choice(['clear sky', 'few clouds', 'rain', 'thunderstorm'])}]
        }
        forecast_data['list'].append(entry)
    return forecast_data

def plot_forecast(forecast_data):
    dates = [datetime.datetime.fromtimestamp(entry['dt']) for entry in forecast_data['list']]
    temps = [entry['main']['temp'] for entry in forecast_data['list']]
    
    plt.figure(figsize=(10, 4))
    plt.plot(dates, temps, marker='o', linestyle='-', color='b')
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.title('5-Day Weather Forecast')
    plt.xticks(rotation=45)
    plt.grid()
    st.pyplot(plt)

# Streamlit UI
st.title("Real-time Weather Forecasting App (Dummy Data)")
city = st.text_input("Enter City Name", "New Delhi")

if st.button("Get Forecast"):
    weather_data = generate_dummy_weather()
    st.subheader(f"Current Weather in {city}")
    temp = weather_data['list'][0]['main']['temp']
    humidity = weather_data['list'][0]['main']['humidity']
    condition = weather_data['list'][0]['weather'][0]['description']
    st.write(f"🌡 Temperature: {temp}°C")
    st.write(f"💧 Humidity: {humidity}%")
    st.write(f"🌤 Condition: {condition.title()}")
    
    st.subheader("5-Day Forecast")
    plot_forecast(weather_data)
