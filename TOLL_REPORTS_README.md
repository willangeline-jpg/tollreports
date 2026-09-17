# 📊 Toll Reports Dashboard

**Monthly, Quarterly & Yearly Performance Analysis**

A professional toll reporting system with TELUS brand colors generating automated charts and reports for IMIS, Misoteps, and AEM systems.

---

## ✨ Features

✅ **Automatic Report Generation** - Runs monthly via GitHub Actions  
✅ **TELUS Brand Colors** - Professional purple & magenta color scheme  
✅ **Three Analysis Levels** - Monthly, Quarterly, and Yearly views  
✅ **Three Systems** - IMIS, AEM, and Misoteps with individual charts  
✅ **Worked vs Received Tracking** - Compare actual vs expected metrics  
✅ **Professional HTML Reports** - Beautiful, responsive design  
✅ **GitHub Pages Hosting** - Free automatic hosting  

---

## 📁 File Structure

```
tollreports/
├── .github/
│   └── workflows/
│       └── toll-reports-auto-update.yml    (Automation workflow)
├── reports/
│   ├── index.html                           (Main report page)
│   └── graphs/
│       ├── yearly_comparison.png
│       ├── yearly_imis.png
│       ├── yearly_aem.png
│       ├── yearly_misoteps.png
│       ├── quarterly_imis.png
│       ├── quarterly_aem.png
│       ├── quarterly_misoteps.png
│       ├── monthly_imis.png
│       ├── monthly_aem.png
│       └── monthly_misoteps.png
├── data/                                    (Auto-generated data)
├── generate_toll_reports.py                 (Report generator script)
├── requirements.txt                         (Python dependencies)
└── README.md                                (This file)
```

---

## 🎯 How It Works

### **Workflow Process**

```
1. You upload Excel files to the repository
   ↓
2. GitHub Actions detects the changes
   ↓
3. Automation runs the Python script
   ↓
4. Script reads Excel data
   ↓
5. Generates charts with TELUS colors
   ↓
6. Creates professional HTML report
   ↓
7. Saves everything to GitHub
   ↓
8. Reports go LIVE on GitHub Pages! 🎉
```

### **Timing**

- **Automatic:** Every 1st of the month at 8:00 AM UTC
- **Manual Trigger:** Any time via GitHub Actions tab
- **On Upload:** Whenever Excel files are pushed

---

## 📥 Data Files Required

The system works with these Excel files:

### **1. YBR.xlsx**
Contains historical yearly data with sheets:
- `IMIS` - Contains: Year, Total Worked, Total Received
- `AEM` - Contains: Year, Total Worked, Total Received
- `Misoteps` - Contains: Year, Total Worked, Total Received

Format:
```
Year | Total Worked | Total Received
2023 |   231735    |    232948
2024 |   210289    |    208899
```

### **2. 2026_Month_end_Misoteps_Exception_and_AEM_[1].xlsx**
Contains monthly breakdown data with sheets for each month

---

## 📊 Generated Charts

### **TELUS Brand Colors Used**

| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary Purple | #522583 | Main TELUS color (Worked) |
| Magenta | #D80070 | TELUS magenta (Received) |
| Light Purple | #A066CC | Accents |
| Dark Purple | #4B2B72 | Headers |
| Accent Teal | #00B4D8 | Secondary accents |

### **Chart Types**

1. **Yearly Comparison** - Full 5-year history
2. **Quarterly Breakdown** - Q1-Q4 performance
3. **Monthly Details** - All 12 months
4. **System Comparison** - IMIS vs AEM vs Misoteps side-by-side

---

## 🚀 Getting Started

### **Step 1: Clone or Use the Repository**

```bash
git clone https://github.com/willangeline-jpg/tollreports.git
cd tollreports
```

### **Step 2: Set Up GitHub Actions**

1. Go to your repo → **[Settings]** → **[Pages]**
2. Set **Source** to: Deploy from a branch
3. Select **main** branch and **/ (root)** folder
4. Click **[Save]**

### **Step 3: Upload Your Excel Files**

1. Go to **[Code]** tab
2. Click **[Add file]** → **Upload files**
3. Upload your Excel files:
   - `YBR.xlsx`
   - `2026_Month_end_Misoteps_Exception_and_AEM__1_.xlsx`
4. Click **[Commit changes]**

### **Step 4: Watch Automation Run**

1. Go to **[Actions]** tab
2. Watch the workflow execute (1-2 minutes)
3. See the green ✅ checkmark when complete

### **Step 5: View Your Reports**

```
https://willangeline-jpg.github.io/tollreports/
```

---

## 📋 Monthly Workflow

**Follow these steps every month:**

### **Before Month Ends**
- [ ] Prepare updated Excel files on your computer
- [ ] Have both files ready to upload

### **First Day of Month**
- [ ] Go to GitHub repository
- [ ] Click [Code] tab
- [ ] Upload the 2 Excel files
- [ ] Files are detected automatically
- [ ] Automation starts running

### **After Upload (2-3 minutes)**
- [ ] Go to [Actions] tab
- [ ] Wait for workflow to complete
- [ ] See green ✅ success checkmark
- [ ] Check reports at GitHub Pages URL
- [ ] Share with your team

---

## 🔄 Manual Trigger

If you want to run the automation manually:

1. Go to **[Actions]** tab
2. Click **"Auto-Generate Toll Reports"**
3. Click **[Run workflow ▼]**
4. Select **main** branch
5. Click **[Run workflow]**

The reports will generate in ~2 minutes!

---

## 📱 Sharing Reports

**Send your team these links:**

### **Main Report Dashboard**
```
https://willangeline-jpg.github.io/tollreports/
```
Interactive dashboard with all charts (Monthly, Quarterly, Yearly)

### **Direct to Repository**
```
https://github.com/willangeline-jpg/tollreports
```
For those who want to see the code or data files

---

## 🛠️ Customization

### **Change Colors**

Edit `generate_toll_reports.py` - Find the `TELUS_COLORS` dictionary:

```python
TELUS_COLORS = {
    'primary_purple': '#522583',    # Change this
    'magenta': '#D80070',            # Or this
    # ...
}
```

### **Add More Systems**

1. Edit `generate_toll_reports.py`
2. Add your system name to the `systems` list
3. Update Excel file with data for that system
4. Re-run the automation

### **Change Report Sections**

Edit the HTML template in `generate_toll_reports.py` - Find the `create_html_report()` function and customize the HTML content.

---

## ⚠️ Troubleshooting

### **Problem: Automation Shows Red ❌**

**Solution:**
1. Go to **[Actions]** → Failed workflow
2. Click on the job to see error details
3. Common causes:
   - File names don't match exactly
   - Excel file is corrupted
   - Missing required columns
4. Fix the file and re-upload

### **Problem: Reports Don't Appear**

**Solution:**
1. Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
2. Wait 2-3 minutes for GitHub Pages to build
3. Check that GitHub Pages is enabled in Settings
4. Verify files are in the reports/ folder

### **Problem: Charts Look Wrong**

**Solution:**
1. Check Excel file data format
2. Ensure proper column headers
3. Verify no empty rows or corrupted cells
4. Re-save Excel file and re-upload

---

## 📝 Important Rules

### ✅ DO

- ✅ Keep Excel file names EXACTLY the same
- ✅ Update files monthly consistently
- ✅ Check Actions tab for success/failure
- ✅ Hard refresh browser after waiting
- ✅ Close Excel files before uploading (Excel locks files)
- ✅ Keep proper data format (no extra spaces or merged cells)

### ❌ DON'T

- ❌ Rename the Excel files
- ❌ Delete files from /reports/ or /data/ folders
- ❌ Edit .github/workflows/ unless you know Python/YAML
- ❌ Upload multiple times in quick succession
- ❌ Leave Excel files open while uploading
- ❌ Change the folder structure

---

## 💡 Tips & Tricks

1. **Speed Up Automation**: Close Excel files before uploading
2. **Better Charts**: Keep data clean (no merged cells, consistent format)
3. **Mobile Viewing**: Reports are responsive - works on phones too!
4. **Download Charts**: Right-click any chart → Save image
5. **Print Reports**: Use browser Print function (Ctrl+P) for PDF export
6. **Archive Reports**: GitHub automatically keeps history of all files

---

## 📞 Support

If you need help:

1. Check the Actions tab for error messages
2. Review this README for common issues
3. Contact your team administrator
4. Check GitHub documentation: https://docs.github.com

---

## 📈 What's Next?

Future enhancements you could add:

- [ ] Add email notifications when reports are ready
- [ ] Create dashboard with filters
- [ ] Add year-over-year comparison
- [ ] Generate PDF reports automatically
- [ ] Add exception tracking alerts
- [ ] Create custom metrics dashboard

---

## 📄 License

This toll reporting system is maintained by your organization.

---

## ✨ Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-09-17 | Initial release with monthly, quarterly, yearly charts |

---

**Last Updated:** September 2026

**Questions?** Contact your repository administrator or check the team guide!

Happy reporting! 📊✨
