#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

print("START", flush=True)

os.makedirs('reports/graphs', exist_ok=True)

COLORS = {'worked': '#00B050', 'received': '#4B2B72'}
plt.style.use('seaborn-v0_8-darkgrid')

print("LOADING", flush=True)
ybr_data = {}
for system in ['IMIS', 'AEM', 'Misoteps']:
    df = pd.read_excel('YBR.xlsx', sheet_name=system, skiprows=1)
    df.columns = ['Period', 'Year', 'Worked', 'Received']
    df = df.dropna(subset=['Year', 'Worked', 'Received'])
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df = df.dropna(subset=['Year'])
    ybr_data[system] = df

print("CHARTS", flush=True)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for system, df in ybr_data.items():
    # YEARLY - Get unique years only, sorted ascending (2022, 2023, 2024, 2025)
    yearly_data = df.drop_duplicates(subset=['Year'], keep='first').sort_values('Year', ascending=True).head(5)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(yearly_data))
    ax.bar(x - 0.175, yearly_data['Worked'], 0.35, label='Total Worked', color=COLORS['worked'])
    ax.bar(x + 0.175, yearly_data['Received'], 0.35, label='Total Received', color=COLORS['received'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    ax.set_title(f'{system} Worked vs Received')
    ax.set_xticks(x)
    ax.set_xticklabels([str(int(v)) for v in yearly_data['Year'].values], rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    fig.savefig(f'reports/graphs/yearly_{system.lower()}.png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    # QUARTERLY
    data = df.head(4).copy()
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(data))
    ax.bar(x - 0.175, data['Worked'], 0.35, label='Total Worked', color=COLORS['worked'])
    ax.bar(x + 0.175, data['Received'], 0.35, label='Total Received', color=COLORS['received'])
    ax.set_xlabel('Quarter')
    ax.set_ylabel('Count')
    ax.set_title(f'{system} Worked vs Received')
    ax.set_xticks(x)
    ax.set_xticklabels([f'Q{i+1}' for i in range(len(data))], rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    fig.savefig(f'reports/graphs/quarterly_{system.lower()}.png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    
    # MONTHLY
    data = df.head(12).copy()
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(data))
    ax.bar(x - 0.175, data['Worked'], 0.35, label='Total Worked', color=COLORS['worked'])
    ax.bar(x + 0.175, data['Received'], 0.35, label='Total Received', color=COLORS['received'])
    ax.set_xlabel('Month')
    ax.set_ylabel('Count')
    ax.set_title(f'{system} Worked vs Received')
    ax.set_xticks(x)
    ax.set_xticklabels(months[:len(data)], rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    fig.savefig(f'reports/graphs/monthly_{system.lower()}.png', dpi=300, bbox_inches='tight')
    plt.close(fig)

print("HTML", flush=True)
html = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Toll Reports</title><style>body{font-family:Arial;background:#f0f0f0;padding:20px}.container{max-width:1600px;margin:0 auto;background:white;border-radius:10px;padding:40px}header{text-align:center;border-bottom:4px solid #4B2B72;padding-bottom:20px;margin-bottom:30px}h1{color:#333;font-size:2.5em}.subtitle{color:#00B050;font-weight:bold}.legend{display:flex;justify-content:center;gap:40px;margin:20px 0}.legend-item{display:flex;align-items:center;gap:10px}.legend-color{width:30px;height:30px;border-radius:4px}.worked{background:#00B050}.received{background:#4B2B72}.section-title{color:#4B2B72;font-size:2em;font-weight:bold;margin:30px 0 20px 0;border-bottom:3px solid #00B050;padding-bottom:10px}.system-title{color:#4B2B72;font-size:1.5em;margin:20px 0 10px 0}.wrapper{display:grid;grid-template-columns:1fr 1fr;gap:30px}table{width:100%;border-collapse:collapse}th{background:#4B2B72;color:white;padding:10px}td{padding:8px;border:1px solid #ddd}img{max-width:100%;border-radius:5px}footer{text-align:center;margin-top:50px;border-top:2px solid #4B2B72;padding-top:20px}</style></head><body><div class="container"><header><h1>📊 Toll Reports Dashboard</h1><div class="subtitle">Monthly, Quarterly & Yearly Performance Analysis</div></header><div class="legend"><div class="legend-item"><div class="legend-color worked"></div>Total Worked</div><div class="legend-item"><div class="legend-color received"></div>Total Received</div></div>'

html += '<section><h2 class="section-title">📈 Yearly Performance</h2>'
for system in ['Misoteps', 'IMIS', 'AEM']:
    yearly_data = ybr_data[system].drop_duplicates(subset=['Year'], keep='first').sort_values('Year', ascending=True).head(5)
    html += f'<div class="system-title">{system} Yearly</div><div class="wrapper"><div><table><tr><th>Year</th><th>Worked</th><th>Received</th></tr>'
    for _, row in yearly_data.iterrows():
        html += f'<tr><td>{int(row["Year"])}</td><td>{int(row["Worked"]):,}</td><td>{int(row["Received"]):,}</td></tr>'
    html += f'</table></div><div><img src="graphs/yearly_{system.lower()}.png"></div></div>'

html += '</section><section><h2 class="section-title">📊 Quarterly Performance</h2>'
for system in ['Misoteps', 'IMIS', 'AEM']:
    data = ybr_data[system].head(4)
    html += f'<div class="system-title">{system} Quarterly</div><div class="wrapper"><div><table><tr><th>Quarter</th><th>Worked</th><th>Received</th></tr>'
    for i, (_, row) in enumerate(data.iterrows()):
        html += f'<tr><td>Q{i+1}</td><td>{int(row["Worked"]):,}</td><td>{int(row["Received"]):,}</td></tr>'
    html += f'</table></div><div><img src="graphs/quarterly_{system.lower()}.png"></div></div>'

html += '</section><section><h2 class="section-title">📅 Monthly Performance</h2>'
for system in ['Misoteps', 'IMIS', 'AEM']:
    data = ybr_data[system].head(12)
    html += f'<div class="system-title">{system} Monthly</div><div class="wrapper"><div><table><tr><th>Month</th><th>Worked</th><th>Received</th></tr>'
    for i, (_, row) in enumerate(data.iterrows()):
        html += f'<tr><td>{months[i] if i < 12 else ""}</td><td>{int(row["Worked"]):,}</td><td>{int(row["Received"]):,}</td></tr>'
    html += f'</table></div><div><img src="graphs/monthly_{system.lower()}.png"></div></div>'

html += f'</section><footer>Last Updated: {datetime.now().strftime("%B %d, %Y")}</footer></div></body></html>'

with open('reports/index.html', 'w') as f:
    f.write(html)

print("DONE", flush=True)
