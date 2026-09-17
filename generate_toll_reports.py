#!/usr/bin/env python3
"""
Toll Reports Generator - Monthly, Quarterly & Yearly
Generates charts and reports with TELUS brand colors
Worked vs Received comparisons for IMIS, Misoteps, AEM
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams
import numpy as np
import os
from datetime import datetime
import json
from pathlib import Path

# TELUS Brand Colors
TELUS_COLORS = {
    'primary_purple': '#522583',    # Main TELUS purple
    'magenta': '#D80070',            # TELUS magenta
    'light_purple': '#A066CC',       # Light purple
    'dark_purple': '#4B2B72',        # Dark purple
    'accent_teal': '#00B4D8',        # Accent color
    'white': '#FFFFFF',
    'light_gray': '#F5F5F5',
    'dark_gray': '#333333'
}

# Set matplotlib style for TELUS branding
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
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
        """Read YBR.xlsx file - contains historical data"""
        data = {}
        try:
            for system in ['IMIS', 'AEM', 'Misoteps']:
                try:
                    df = pd.read_excel('YBR.xlsx', sheet_name=system, skiprows=1)
                    # Rename columns
                    df.columns = ['Period', 'Year', 'Worked', 'Received']
                    # Clean data
                    df = df.dropna(subset=['Year', 'Worked', 'Received'])
                    data[system] = df
                    print(f"✓ Loaded YBR {system} data: {len(df)} rows")
                except Exception as e:
                    print(f"⚠ Could not load YBR {system}: {e}")
            return data
        except Exception as e:
            print(f"✗ Error reading YBR file: {e}")
            return data
    
    def read_monthly_data(self):
        """Read 2026 monthly data from second Excel file"""
        monthly_data = {}
        try:
            xl_file = pd.ExcelFile('2026_Month_end_Misoteps_Exception_and_AEM__1_.xlsx')
            
            # Map month names to month numbers
            month_mapping = {
                'January': 1, 'February': 2, 'March': 3, 'April': 4,
                'May': 5, 'June': 6, 'July': 7, 'August': 8,
                'September': 9, 'October': 10, 'November': 11, 'December': 12,
                'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
            }
            
            for sheet in xl_file.sheet_names:
                if sheet in month_mapping:
                    try:
                        df = pd.read_excel('2026_Month_end_Misoteps_Exception_and_AEM__1_.xlsx', 
                                          sheet_name=sheet)
                        # Extract key metrics (customize based on actual data structure)
                        monthly_data[sheet] = df
                        print(f"✓ Loaded monthly data for {sheet}")
                    except Exception as e:
                        print(f"⚠ Could not load {sheet} data: {e}")
            
            return monthly_data
        except Exception as e:
            print(f"✗ Error reading monthly file: {e}")
            return monthly_data
    
    def create_worked_vs_received_chart(self, system_name, data, period_type='yearly'):
        """Create Worked vs Received comparison chart with TELUS colors"""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Prepare data
        periods = data['Period'].astype(str).values
        worked = data['Worked'].values
        received = data['Received'].values
        
        # Set up x-axis
        x = np.arange(len(periods))
        width = 0.35
        
        # Create bars with TELUS colors
        bars1 = ax.bar(x - width/2, worked, width, label='Worked', 
                       color=TELUS_COLORS['primary_purple'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        bars2 = ax.bar(x + width/2, received, width, label='Received', 
                       color=TELUS_COLORS['magenta'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        
        # Customize chart
        ax.set_xlabel(f'{period_type.capitalize()} Period', fontsize=13, fontweight='bold', color=TELUS_COLORS['dark_gray'])
        ax.set_ylabel('Count', fontsize=13, fontweight='bold', color=TELUS_COLORS['dark_gray'])
        ax.set_title(f'{system_name} - Worked vs Received ({period_type.capitalize()})', 
                    fontsize=16, fontweight='bold', color=TELUS_COLORS['primary_purple'], pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(periods, rotation=45, ha='right')
        
        # Add value labels on bars
        for bar in bars1:
