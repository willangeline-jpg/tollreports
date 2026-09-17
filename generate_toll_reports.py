#!/usr/bin/env python3
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

try:
    print("START: Initializing...", flush=True)
    
    os.makedirs('reports/graphs', exist_ok=True)
    print("INIT: Directories created", flush=True)
    
    COLORS = {'worked': '#00B050', 'received': '#4B2B72', 'white': '#FFFFFF', 'light_gray': '#F5F5F5'}
    plt.style.use('seaborn-v0_8-darkgrid')
    
    print("READ: Loading Excel data...", flush=True)
    ybr_data = {}
    for system in ['IMIS', 'AEM', 'Misoteps']:
        df = pd.read_excel('YBR.xlsx', sheet_name=system, skiprows=1)
        df.columns = ['Period', 'Year', 'Worked', 'Received']
        df = df.dropna(subset=['Year', 'Worked', 'Received'])
        ybr_data[system] = df
        print(f"LOAD: {system} - {len(df)} rows", flush=True)
    
    print("CHART: Creating charts...", flush=True)
    for system, df in ybr_data.items():
        for period_type, data_slice in [('yearly', df.head(5)), ('quarterly', df.head(4)), ('monthly', df.head(12))]:
            fig, ax = plt.subplots(figsize=(10, 6))
            periods = data_slice['Period'].astype(str).values
            x = np.arange(len(periods))
            width = 0.35
            
            ax.bar(x - width/2, data_slice['Worked'], width, label='Total Worked', color=COLORS['worked'], edgecolor='white', linewidth=1.5, alpha=0.9)
            ax.bar(x + width/2, data_slice['Received'], width, label='Total Received', color=COLORS['received'], edgecolor='white', linewidth=1.5, alpha=0.9)
            
            ax.set_xlabel('Period', fontsize=11, fontweight='bold')
            ax.set_ylabel('Count', fontsize=11, fontweight='bold')
            ax.set_title(f'{system} Worked vs Received', fontsize=13, fontweight='bold')
            ax.set_xticks(x)
            ax.set_xticklabels(periods, rotation=45, ha='right')
            ax.legend(fontsize=10)
            ax.grid(axis='y', alpha=0.3)
            fig.patch.set_facecolor(COLORS['white'])
            ax.set_facecolor(COLORS['light_gray'])
            plt.tight_layout()
            
            fig.savefig(f'reports/graphs/{period_type}_{system.lower()}.png', dpi=300, bbox_inches='tight')
            plt.close(fig)
            print(f"SAVE: {period_type}_{system.lower()}.png", flush=True)
    
    print("HTML: Creating HTML report...", flush=True)
    html = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Toll Reports</title><style>* {margin: 0; padding: 0; box-sizing: border-box;} body {font-family: Arial; background: #f0f0f0; padding: 20px;} .container {max-width: 1600px; margin: 0 auto; background: white; border-radius: 10px; padding: 40px;} header {text-align: center; border-bottom: 4px solid #4B2B72; padding-bottom: 20px; margin-bottom: 30px;} h1 {color: #333; font-size: 2.5em;} .subtitle {color: #00B050; font-size: 1.2em; font-weight: bold;} .section-title {color: #4B2B72; font-size: 2em; font-weight: bold; margin: 30px 0 20px 0; border-bottom: 3px solid #00B050; padding-bottom: 10px;} .system-section {margin-bottom: 40px;} .system-title {color: #4B2B72; font-size: 1.5em; font-weight: bold; margin: 20px 0 10px 0;} .table-chart-wrapper {display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 30px;} table {width: 100%; border-collapse: collapse; font-size: 0.9em;} th {background: #4B2B72; color: white; padding: 10px; text-align: left;} td {padding: 8px; border: 1px solid #ddd;} tr:nth-child(even) {background: #f9f9f9;} img {max-width: 100%; border-radius: 5px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);} .legend {display: flex; justify-content: center; gap: 40px; margin: 20px 0;} .legend-item {display: flex; align-items: center; gap: 10px; font-weight: bold;} .legend-color {width: 30px; height: 30px; border-radius: 4px;} .worked {background: #00B050;} .received {background: #4B2B72;} footer {text-align: center; margin-top: 50px; padding-top: 20px; border-top: 2px solid #4B2B72; color: #888;}</style></head><body><div class="container"><header><h1>📊 Toll Reports Dashboard</h1><div class="subtitle">Monthly, Quarterly & Yearly Performance Analysis</div><div style="color: #888; font-size: 0.9em; margin-top: 10px;">Generated: ' + datetime.now().strftime('%B %d, %Y at %I:%M %p') + '</div></header><div class="legend"><div class="legend-item"><div class="legend-color worked"></div><span>Total Worked</span></div><div class="legend-item"><div class="legend-color received"></div><span>Total Received</span></div></div>'
    
    yearly = {sys: df.head(5) for sys, df in ybr_data.items()}
    quarterly = {sys: df.head(4) for sys, df in ybr_data.items()}
    monthly = {sys: df.head(12) for sys, df in ybr_data.items()}
    
    html += '<section><h2 class="section-title">📈 Yearly Performance</h2>'
    for system in ['Misoteps', 'IMIS', 'AEM']:
        if system.lower() in yearly:
            html += f'<div class="system-section"><h3 class="system-title">{system} Yearly Data</h3><div class="table-chart-wrapper"><div><table><thead><tr><th>Period</th><th>Total Worked</th><th>Total Received</th></tr></thead><tbody>'
            for _, row in yearly[system.lower()].iterrows():
                html += f'<tr><td>{row["Period"]}</td><td>{int(row["Worked"]):,}</td><td>{int(row["Received"]):,}</td></tr>'
            html += f'</tbody></table></div><div><img src="graphs/yearly_{system.lower()}.png" alt="{system}"></div></div></div>'
    
    html += '</section><section><h2 class="section-title">📊 Quarterly Performance</h2>'
    for system in ['Misoteps', 'IMIS', 'AEM']:
        if system.lower() in quarterly:
            html += f'<div class="system-section"><h3 class="system-title">{system} Quarterly Data</h3><div class="table-chart-wrapper"><div><table><thead><tr><th>Quarter</th><th>Total Worked</th><th>Total Received</th></tr></thead><tbody>'
            for i, (_, row) in enumerate(quarterly[system.lower()].iterrows()):
                html += f'<tr><td>Q{i+1}</td><td>{int(row["Worked"]):,}</td><td>{int(row["Received"]):,}</td></tr>'
            html += f'</tbody></table></div><div><img src="graphs/quarterly_{system.lower()}.png" alt="{system}"></div></div></div>'
    
    html += '</section><section><h2 class="section-title">📅 Monthly Performance</h2>'
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for system in ['Misoteps', 'IMIS', 'AEM']:
        if system.lower() in monthly:
            html += f'<div class="system-section"><h3 class="system-title">{system} Monthly Data</h3><div class="table-chart-wrapper"><div><table><thead><tr><th>Month</th><th>Total Worked</th><th>Total Received</th></tr></thead><tbody>'
            for i, (_, row) in enumerate(monthly[system.lower()].iterrows()):
                if i < len(months):
                    html += f'<tr><td>{months[i]}</td><td>{int(row["Worked"]):,}</td><td>{int(row["Received"]):,}</td></tr>'
            html += f'</tbody></table></div><div><img src="graphs/monthly_{system.lower()}.png" alt="{system}"></div></div></div>'
    
    html += f'</section><footer><p>Last Updated: {datetime.now().strftime("%B %d, %Y")}</p></footer></div></body></html>'
    
    with open('reports/index.html', 'w') as f:
        f.write(html)
    print("HTML: Report created", flush=True)
    
    print("=" * 80, flush=True)
    print("✅ SUCCESS: All reports generated!", flush=True)
    print("=" * 80, flush=True)

except Exception as e:
    print(f"ERROR: {str(e)}", flush=True)
    import traceback
    traceback.print_exc()
