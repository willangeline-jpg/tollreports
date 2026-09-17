#!/usr/bin/env python3
"""
Toll Reports Generator - Monthly, Quarterly & Yearly
Generates charts and reports with TELUS brand colors
Worked vs Received comparisons for IMIS, Misoteps, AEM
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# TELUS Brand Colors
TELUS_COLORS = {
    'primary_purple': '#522583',
    'magenta': '#D80070',
    'light_purple': '#A066CC',
    'dark_purple': '#4B2B72',
    'accent_teal': '#00B4D8',
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
        fig, ax = plt.subplots(figsize=(14, 8))
        
        periods = data['Period'].astype(str).values
        worked = data['Worked'].values
        received = data['Received'].values
        
        x = np.arange(len(periods))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, worked, width, label='Worked', 
                       color=TELUS_COLORS['primary_purple'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        bars2 = ax.bar(x + width/2, received, width, label='Received', 
                       color=TELUS_COLORS['magenta'], 
                       edgecolor='white', linewidth=1.5, alpha=0.9)
        
        ax.set_xlabel(f'{period_type.capitalize()} Period', fontsize=13, fontweight='bold')
        ax.set_ylabel('Count', fontsize=13, fontweight='bold')
        ax.set_title(f'{system_name} - Worked vs Received ({period_type.capitalize()})', 
                    fontsize=16, fontweight='bold', color=TELUS_COLORS['primary_purple'], pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(periods, rotation=45, ha='right')
        
        for bar in bars1:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}', ha='center', va='bottom', fontsize=9)
        
        for bar in bars2:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}', ha='center', va='bottom', fontsize=9)
        
        ax.legend(fontsize=12, loc='upper left', framealpha=0.95)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        fig.patch.set_facecolor(TELUS_COLORS['white'])
        ax.set_facecolor(TELUS_COLORS['light_gray'])
        
        plt.tight_layout()
        return fig
    
    def create_comparison_chart(self, data_dict, period_type='yearly'):
        """Create side-by-side comparison of all systems"""
        fig, axes = plt.subplots(1, 3, figsize=(20, 7))
        fig.suptitle(f'Toll Reports - Worked vs Received Comparison ({period_type.capitalize()})', 
                    fontsize=18, fontweight='bold', color=TELUS_COLORS['primary_purple'], y=1.02)
        
        systems = ['IMIS', 'AEM', 'Misoteps']
        
        for idx, (ax, system) in enumerate(zip(axes, systems)):
            if system in data_dict:
                data = data_dict[system]
                
                periods = data['Period'].astype(str).values
                worked = data['Worked'].values
                received = data['Received'].values
                
                x = np.arange(len(periods))
                width = 0.35
                
                ax.bar(x - width/2, worked, width, label='Worked', 
                      color=TELUS_COLORS['primary_purple'], edgecolor='white', linewidth=1.5, alpha=0.9)
                ax.bar(x + width/2, received, width, label='Received', 
                      color=TELUS_COLORS['magenta'], edgecolor='white', linewidth=1.5, alpha=0.9)
                
                ax.set_title(system, fontsize=14, fontweight='bold', color=TELUS_COLORS['primary_purple'], pad=15)
                ax.set_xticks(x)
                ax.set_xticklabels(periods, rotation=45, ha='right', fontsize=10)
                ax.set_ylabel('Count', fontsize=11, fontweight='bold')
                ax.grid(axis='y', alpha=0.3, linestyle='--')
                ax.set_axisbelow(True)
                ax.set_facecolor(TELUS_COLORS['light_gray'])
                
                if idx == 0:
                    ax.legend(fontsize=10, loc='upper left', framealpha=0.95)
        
        fig.patch.set_facecolor(TELUS_COLORS['white'])
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
        """Extract monthly data"""
        monthly_summary = {}
        for system, df in ybr_data.items():
            monthly_summary[system] = df[df['Period'].astype(str).str.contains('M|Month', case=False, na=False)]
            if len(monthly_summary[system]) == 0:
                monthly_summary[system] = df.head(12)
        return monthly_summary
    
    def generate_yearly_charts(self, ybr_data):
        """Generate yearly charts"""
        print("\n📊 Generating Yearly Charts...")
        yearly_data = self.extract_yearly_data(ybr_data)
        
        for system, data in yearly_data.items():
            if len(data) > 0:
                fig = self.create_worked_vs_received_chart(system, data, 'yearly')
                filepath = os.path.join(self.graphs_dir, f'yearly_{system.lower()}.png')
                fig.savefig(filepath, dpi=300, bbox_inches='tight')
                plt.close(fig)
                print(f"✓ Saved: yearly_{system.lower()}.png")
        
        fig = self.create_comparison_chart(yearly_data, 'yearly')
        filepath = os.path.join(self.graphs_dir, 'yearly_comparison.png')
        fig.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"✓ Saved: yearly_comparison.png")
    
    def generate_quarterly_charts(self, ybr_data):
        """Generate quarterly charts"""
        print("\n📊 Generating Quarterly Charts...")
        quarterly_data = self.extract_quarterly_data(ybr_data)
        
        for system, data in quarterly_data.items():
            if len(data) > 0:
                data_copy = data.copy()
                data_copy['Period'] = [f'Q{i+1}' for i in range(len(data_copy))]
                fig = self.create_worked_vs_received_chart(system, data_copy, 'quarterly')
                filepath = os.path.join(self.graphs_dir, f'quarterly_{system.lower()}.png')
                fig.savefig(filepath, dpi=300, bbox_inches='tight')
                plt.close(fig)
                print(f"✓ Saved: quarterly_{system.lower()}.png")
    
    def generate_monthly_charts(self, ybr_data):
        """Generate monthly charts"""
        print("\n📊 Generating Monthly Charts...")
        monthly_data = self.extract_monthly_data(ybr_data)
        
        for system, data in monthly_data.items():
            if len(data) > 0:
                data_copy = data.copy()
                months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                data_copy['Period'] = months[:len(data_copy)]
                fig = self.create_worked_vs_received_chart(system, data_copy, 'monthly')
                filepath = os.path.join(self.graphs_dir, f'monthly_{system.lower()}.png')
                fig.savefig(filepath, dpi=300, bbox_inches='tight')
                plt.close(fig)
                print(f"✓ Saved: monthly_{system.lower()}.png")
    
    def create_html_report(self):
        """Create HTML report"""
        print("\n📄 Generating HTML Report...")
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toll Reports - Monthly, Quarterly & Yearly</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Arial', 'Helvetica', sans-serif; background: linear-gradient(135deg, #522583 0%, #4B2B72 100%); color: #333; padding: 20px; }}
        .container {{ max-width: 1400px; margin: 0 auto; background: white; border-radius: 10px; box-shadow: 0 10px 40px rgba(82, 37, 131, 0.2); padding: 40px; }}
        header {{ text-align: center; margin-bottom: 50px; border-bottom: 4px solid #522583; padding-bottom: 30px; }}
        h1 {{ color: #522583; font-size: 2.5em; margin-bottom: 10px; }}
        .subtitle {{ color: #D80070; font-size: 1.2em; font-weight: bold; }}
        .timestamp {{ color: #888; font-size: 0.95em; margin-top: 15px; }}
        .section {{ margin-bottom: 50px; }}
        .section-title {{ color: #522583; font-size: 2em; font-weight: bold; margin: 30px 0 20px 0; padding-bottom: 10px; border-bottom: 3px solid #D80070; }}
        .charts-grid {{ display: grid; grid-template-columns: 1fr; gap: 30px; margin-top: 30px; }}
        .chart-container {{ background: #f9f9f9; border: 2px solid #E5E5E5; border-radius: 8px; padding: 20px; text-align: center; }}
        .chart-container img {{ max-width: 100%; height: auto; border-radius: 5px; box-shadow: 0 4px 12px rgba(82, 37, 131, 0.1); }}
        .chart-title {{ color: #522583; font-size: 1.3em; font-weight: bold; margin-bottom: 15px; }}
        .comparison-section {{ background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%); border: 3px solid #522583; border-radius: 10px; padding: 30px; margin: 30px 0; }}
        .telus-badge {{ display: inline-block; background: linear-gradient(135deg, #522583 0%, #D80070 100%); color: white; padding: 8px 16px; border-radius: 20px; font-weight: bold; margin-top: 10px; }}
        footer {{ text-align: center; margin-top: 50px; padding-top: 30px; border-top: 2px solid #522583; color: #888; }}
        .legend {{ display: flex; justify-content: center; gap: 40px; margin: 20px 0; flex-wrap: wrap; }}
        .legend-item {{ display: flex; align-items: center; gap: 10px; font-weight: bold; }}
        .legend-color {{ width: 30px; height: 30px; border-radius: 4px; border: 2px solid white; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); }}
        .worked {{ background-color: #522583; }}
        .received {{ background-color: #D80070; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Toll Reports Dashboard</h1>
            <div class="subtitle">Monthly, Quarterly & Yearly Performance Analysis</div>
            <div class="telus-badge">Powered by TELUS</div>
            <div class="timestamp">Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</div>
        </header>
        
        <div class="legend">
            <div class="legend-item">
                <div class="legend-color worked"></div>
                <span>Worked</span>
            </div>
            <div class="legend-item">
                <div class="legend-color received"></div>
                <span>Received</span>
            </div>
        </div>
        
        <section class="section">
            <h2 class="section-title">📈 Yearly Performance</h2>
            <div class="comparison-section">
                <h3 class="chart-title">Worked vs Received - All Systems Comparison</h3>
                <div class="charts-grid">
                    <div class="chart-container">
                        <img src="graphs/yearly_comparison.png" alt="Yearly Comparison">
                    </div>
                </div>
            </div>
            <h3 class="chart-title" style="margin-top: 30px;">Individual System Performance</h3>
            <div class="charts-grid">
                <div class="chart-container">
                    <h4 class="chart-title">IMIS</h4>
                    <img src="graphs/yearly_imis.png" alt="IMIS Yearly">
                </div>
                <div class="chart-container">
                    <h4 class="chart-title">AEM</h4>
                    <img src="graphs/yearly_aem.png" alt="AEM Yearly">
                </div>
                <div class="chart-container">
                    <h4 class="chart-title">Misoteps</h4>
                    <img src="graphs/yearly_misoteps.png" alt="Misoteps Yearly">
                </div>
            </div>
        </section>
        
        <section class="section">
            <h2 class="section-title">📊 Quarterly Performance</h2>
            <div class="charts-grid">
                <div class="chart-container">
                    <h4 class="chart-title">IMIS - Quarterly</h4>
                    <img src="graphs/quarterly_imis.png" alt="IMIS Quarterly">
                </div>
                <div class="chart-container">
                    <h4 class="chart-title">AEM - Quarterly</h4>
                    <img src="graphs/quarterly_aem.png" alt="AEM Quarterly">
                </div>
                <div class="chart-container">
                    <h4 class="chart-title">Misoteps - Quarterly</h4>
                    <img src="graphs/quarterly_misoteps.png" alt="Misoteps Quarterly">
                </div>
            </div>
        </section>
        
        <section class="section">
            <h2 class="section-title">📅 Monthly Performance</h2>
            <div class="charts-grid">
                <div class="chart-container">
                    <h4 class="chart-title">IMIS - Monthly</h4>
                    <img src="graphs/monthly_imis.png" alt="IMIS Monthly">
                </div>
                <div class="chart-container">
                    <h4 class="chart-title">AEM - Monthly</h4>
                    <img src="graphs/monthly_aem.png" alt="AEM Monthly">
                </div>
                <div class="chart-container">
                    <h4 class="chart-title">Misoteps - Monthly</h4>
                    <img src="graphs/monthly_misoteps.png" alt="Misoteps Monthly">
                </div>
            </div>
        </section>
        
        <footer>
            <p>Toll Reports System | Automated Monthly, Quarterly & Yearly Performance Analysis</p>
            <p style="margin-top: 10px; font-size: 0.9em;">Last Updated: {datetime.now().strftime('%B %d, %Y')}</p>
        </footer>
    </div>
</body>
</html>"""
        
        html_path = os.path.join(self.reports_dir, 'index.html')
        with open(html_path, 'w') as f:
            f.write(html_content)
        
        print(f"✓ HTML report created: {html_path}")
    
    def generate_all_reports(self):
        """Generate all reports and charts"""
        print("=" * 80)
        print("🚀 TOLL REPORTS GENERATOR - TELUS BRAND")
        print("=" * 80)
        
        print("\n📖 Reading Data Files...")
        ybr_data = self.read_ybr_data()
        
        if not ybr_data:
            print("✗ No data available. Exiting.")
            return
        
        self.generate_yearly_charts(ybr_data)
        self.generate_quarterly_charts(ybr_data)
        self.generate_monthly_charts(ybr_data)
        self.create_html_report()
        
        print("\n" + "=" * 80)
        print("✅ REPORT GENERATION COMPLETE!")
        print("=" * 80)
        print(f"\n📊 Reports available at: {os.path.abspath(self.reports_dir)}")
        print(f"📈 Charts available at: {os.path.abspath(self.graphs_dir)}")

if __name__ == '__main__':
    generator = TollReportsGenerator()
    generator.generate_all_reports()
