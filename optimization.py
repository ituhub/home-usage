# optimization.py

import pandas as pd

def optimize_energy_usage(data):
    # Simulate time-of-use rates: cheaper at night (10 PM - 6 AM)
    data['Hour'] = data['Timestamp'].dt.hour
    data['Rate'] = data['Hour'].apply(lambda x: 0.10 if 22 <= x or x < 6 else 0.20)  # $ per kWh

    # Optimization: Shift some usage to cheaper times
    # For simplicity, reduce consumption during peak hours by 10%
    peak_hours = (data['Hour'] >= 16) & (data['Hour'] <= 21)
    data.loc[peak_hours, 'Optimized_Energy_kWh'] = data.loc[peak_hours, 'Energy_Consumption_kWh'] * 0.9
    data.loc[~peak_hours, 'Optimized_Energy_kWh'] = data.loc[~peak_hours, 'Energy_Consumption_kWh']

    return data
