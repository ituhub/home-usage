# energy_data.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_energy_data(days=30):
    date_range = pd.date_range(end=datetime.now(), periods=days, freq='H')
    np.random.seed(42)  # For reproducible results
    energy_consumption = np.random.normal(loc=1.5, scale=0.5, size=len(date_range))
    energy_consumption = np.clip(energy_consumption, 0.5, 3)  # kWh usage per hour

    data = pd.DataFrame({
        'Timestamp': date_range,
        'Energy_Consumption_kWh': energy_consumption
    })
    return data
