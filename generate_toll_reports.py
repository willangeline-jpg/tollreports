#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

CHART_COLORS = {
    'worked': '#00B050',
    'received': '#4B2B72',
    'white': '#FFFFFF',
    'light_gray': '#F5F5F5',
    'dark_gray': '#333333'
}

plt.style.use('seaborn-v0_8-darkgrid')

class TollReportsGenerator:
    def __init__(self):
        self.reports_dir = 'reports'
        self.data_dir = 'data'
        self.graphs_dir = os.path.join(self.reports_dir, 'graphs')
        self.create_directories()
    
    def create_directories(self):
        os.makedirs(self.reports_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.graphs_dir, exist_ok=True)
    
    def read_ybr_data(self):
        data = {}
        try:
            for system in ['IMIS', 'AEM', 'Misoteps']:
                try:
                    df = pd.read_excel('YBR.xlsx', sheet_name=system, skiprows=1)
                    df.columns = ['Period', 'Year', 'Worked', 'Received']
                    df = df.dropna(subset=['Year', 'Worked', 'Received'])
                    data[system] = df
                    print(f"✓ Loaded YBR {system} data: {len(df)} rows")
                except Exception as e:
                    print(f"⚠ Could not load YBR {system}: {e}")
            return data
        except Exception as e:
            print(f"✗ Error reading YBR file: {e}")
            return data
    
    def create_worked_vs_received_chart(self, system_name, data):
        fig, ax = plt.subplots(figsize=(10, 6))
        periods = data['Period'].astype(str).values
        worked = data['Worked'].values
        received = data['Received'].values
        x = np.arange(len(periods))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, worked, width, label='Total Worked', color=CHART_COLORS['worked'], edgecolor='white', linewidth=1.5, alpha=0.9)
        bars2 = ax.bar(x + width/2, received, width, label='Total Received', color=CHART_COLORS['received'], edgecolor='white', linewidth=1.5, alpha=0.9)
