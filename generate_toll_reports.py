#!/usr/bin/env python3
"""
Toll Reports Generator with Tables & Charts
Generates professional reports with tables and charts side by side
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# Colors - Green for Worked, Purple for Received
CHART_COLORS = {
    'worked': '#00B050',         # Bright GREEN
    'received': '#4B2B72',       # Dark PURPLE
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
        """Create Worked vs Received comparison chart"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        periods = data['Period'].astype(str).values
        worked = data['Worked'].values
        received = data['Received'].values
        
        x = np.arange(len(periods))
        width = 0.35
        
        # GREEN for Worked, PURPLE for Received
        bars1 = ax.bar(x - width/2, worked, width, label='Total Worked', 
                       color=CHART_COLORS['worked'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        bars2 = ax.bar(x + width/2, received, width, label='Total Received', 
                       color=CHART_COLORS['received'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        
        ax.set_xlabel('Period', fontsize=11, fontweight='bold')
        ax.set_ylabel('Count', fontsize=11, fontweight='bold')
        ax.set_title(f'{system_name} Worked vs Received', 
                    fontsize=13, fontweight='bold', color=CHART_COLORS['dark_gray'])
        ax.set_xticks(x)
        ax.set_xticklabels(periods, rotation=45, ha='right')
        
        # Add value labels
        for bar in bars1:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}', ha='center', va='bottom', fontsize=8, color=CHART_COLORS['dark_gray'])
        
        for bar in bars2:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}', ha='center', va='bottom', fontsize=8, color=CHART_COLORS['dark_gray'])
        
        ax.legend(fontsize=10, loc='upper left')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        fig.patch.set_facecolor(CHART_COLORS['white'])
        ax.set_facecolor(CHART_COLORS['light_gray'])
        
        plt.tight_layout()
        return fig
    
    def extract_yearly_data(self, ybr_data):
        """Extract yearly summary data"""
        yearly_data = {}
        for system, df in ybr_data.items():
            yearly_data[system] = df.head(5)
        return yearly_data
    
    def extract_quarterly_data(self, ybr_data):
        """Extract quarterly data"""
        quarterly_data = {}
        for system, df in ybr_data.items():
            quarterly_data[system] = df.head(4)
        return quarterly_data
    
    def extract_monthly_data(self, ybr_data):
