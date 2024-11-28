# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from energy_data import generate_energy_data
from optimization import optimize_energy_usage

# Set the page layout
st.set_page_config(page_title='Smart Home Energy Optimizer', layout='wide')

# Title
st.title('Smart Home Energy Usage Optimization')

# Sidebar for user inputs
st.sidebar.header('User Input Parameters')
days = st.sidebar.slider('Select number of days', min_value=7, max_value=60, value=30)

# Load data
data = generate_energy_data(days=days)

# Display raw data
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Energy Consumption Data')
    st.dataframe(data.head())

# Plot energy consumption
st.subheader('Energy Consumption Over Time')
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(data['Timestamp'], data['Energy_Consumption_kWh'], label='Actual Consumption')
ax.set_xlabel('Time')
ax.set_ylabel('Energy Consumption (kWh)')
st.pyplot(fig)

# Optimization
st.subheader('Energy Optimization Suggestions')
optimized_data = optimize_energy_usage(data.copy())

# Display optimization results
st.write('Total Energy Consumption Before Optimization: {:.2f} kWh'.format(data['Energy_Consumption_kWh'].sum()))
st.write('Total Energy Consumption After Optimization: {:.2f} kWh'.format(optimized_data['Optimized_Energy_kWh'].sum()))

# Plot optimized consumption
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(optimized_data['Timestamp'], optimized_data['Optimized_Energy_kWh'], label='Optimized Consumption', color='green')
ax2.set_xlabel('Time')
ax2.set_ylabel('Energy Consumption (kWh)')
st.pyplot(fig2)
