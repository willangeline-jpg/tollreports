#!/usr/bin/env python3
import os
import sys

try:
    print("TEST 1: Script started", flush=True)
    sys.stdout.flush()
    
    os.makedirs('reports/graphs', exist_ok=True)
    print("TEST 2: Directories created", flush=True)
    sys.stdout.flush()
    
    import pandas as pd
    print("TEST 3: Pandas imported", flush=True)
    sys.stdout.flush()
    
    df = pd.read_excel('YBR.xlsx', sheet_name='IMIS', skiprows=1)
    print(f"TEST 4: Excel file read, {len(df)} rows", flush=True)
    sys.stdout.flush()
    
    with open('reports/index.html', 'w') as f:
        f.write('<html><body><h1>Test Works!</h1><p>File created successfully at ' + pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S') + '</p></body></html>')
    print("TEST 5: HTML file created", flush=True)
    sys.stdout.flush()
    
    print("SUCCESS: All tests passed!", flush=True)
except Exception as e:
    print(f"ERROR: {str(e)}", flush=True)
    import traceback
    traceback.print_exc()
    sys.stdout.flush()
