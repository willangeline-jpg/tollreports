#!/usr/bin/env python3
"""
Toll Reports Generator - Monthly, Quarterly & Yearly
Generates charts and reports with Green & Purple colors
Worked vs Received comparisons for IMIS, Misoteps, AEM
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# Updated Colors - Green for Worked, Purple for Received
CHART_COLORS = {
    'worked': '#00B050',         # Bright Green
    'received': '#4B2B72',       # Dark Purple
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
        """Create necessary directories"""
        os.makedirs(self.reports_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.graphs_dir, exist_ok=True)
        
    def read_ybr_data(self):
        """Read YBR.xlsx file"""
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
    
    def create_worked_vs_received_chart(self, system_name, data, period_type='yearly'):
        """Create Worked vs Received comparison chart with Green & Purple"""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        periods = data['Period'].astype(str).values
        worked = data['Worked'].values
        received = data['Received'].values
        
        x = np.arange(len(periods))
        width = 0.35
        
        # Green bars for Worked, Purple bars for Received
        bars1 = ax.bar(x - width/2, worked, width, label='Total Worked', 
                       color=CHART_COLORS['worked'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        bars2 = ax.bar(x + width/2, received, width, label='Total Received', 
                       color=CHART_COLORS['received'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        
        ax.set_xlabel(f'{period_type.capitalize()} Period', fontsize=13, fontweight='bold')
        ax.set_ylabel('Count', fontsize=13, fontweight='bold')
        ax.set_title(f'{system_name} Worked vs Received', 
                    fontsize=16, fontweight='bold', color=CHART_COLORS['dark_gray'], pad=20)
        ax.set_xticks(x)
