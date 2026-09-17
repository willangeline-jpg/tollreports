# 🚀 Toll Reports Dashboard - Setup Guide

**Complete step-by-step instructions to set up automated toll reports with TELUS branding**

---

## ⏱️ Estimated Time: 15-20 minutes

---

## 📋 Prerequisites

You need:
- [ ] GitHub account (already have it!)
- [ ] The tollreports repository
- [ ] Two Excel files:
  - `YBR.xlsx`
  - `2026_Month_end_Misoteps_Exception_and_AEM__1_.xlsx`

---

## 🎯 PART 1: Upload Files to GitHub

### **Step 1: Go to Your Repository**

Open this URL in your browser:
```
https://github.com/willangeline-jpg/tollreports
```

You should see:
```
willangeline-jpg / tollreports (Public)
```

### **Step 2: Click [Code] Tab**

Make sure you're on the **[Code]** tab (main repository view)

### **Step 3: Create .github/workflows Folder**

1. Click **[Add file ▼]** button (top right)
2. Click **"Create new file"**
3. In the filename box, type:
   ```
   .github/workflows/toll-reports-auto-update.yml
   ```
4. **Paste** the workflow file content (see Appendix A)
5. Scroll down → Click **[Commit new file]**

### **Step 4: Upload Python Script**

1. Click **[Add file ▼]** → **"Upload files"**
2. Select `generate_toll_reports.py` from your computer
3. Click **[Commit changes]**

### **Step 5: Upload Requirements File**

1. Click **[Add file ▼]** → **"Upload files"**
2. Select `requirements.txt` from your computer
3. Click **[Commit changes]**

### **Step 6: Upload Excel Data Files**

1. Click **[Add file ▼]** → **"Upload files"**
2. Select both Excel files:
   - `YBR.xlsx`
   - `2026_Month_end_Misoteps_Exception_and_AEM__1_.xlsx`
3. Click **[Commit changes]**

---

## 🎨 PART 2: Enable GitHub Pages

GitHub Pages will host your reports online for free!

### **Step 1: Go to Settings**

1. Click **[Settings]** tab (top right of repo)
2. You should see the settings page

### **Step 2: Find Pages**

1. On the left sidebar, scroll down to **"Code, planning, and automation"** section
2. Click **[Pages]**

### **Step 3: Configure GitHub Pages**

You should see:

```
Build and deployment

Source
☑ Deploy from a branch

Branch
[main ▼]     [/ (root) ▼]

[Save]
```

**Make sure:**
- ✅ "Deploy from a branch" is selected
- ✅ Branch is set to **main**
- ✅ Folder is set to **/ (root)**

### **Step 4: Click [Save]**

After a few seconds, you should see:

```
✓ Your site is live at:
https://willangeline-jpg.github.io/tollreports/
```

**Save this URL!** This is where your reports will be hosted.

---

## ⚙️ PART 3: Test the Automation

### **Step 1: Go to Actions Tab**

Click the **[Actions]** tab at the top of the repository

### **Step 2: Find Your Workflow**

You should see:
```
All workflows

Auto-Generate Toll Reports
```

### **Step 3: Run the Workflow**

1. Click **"Auto-Generate Toll Reports"**
2. Click the blue **[Run workflow ▼]** button
3. Keep **main** branch selected
4. Click **[Run workflow]**

### **Step 4: Watch It Run**

You should see a new workflow run appearing:

```
Auto-Generate Toll Reports #1
Status: ⚪ Queued (spinning circle)
```

Wait 1-2 minutes. It will change to:

```
Auto-Generate Toll Reports #1
Status: ✅ Completed (green checkmark)
Total duration: 46 seconds
```

### **Step 5: View the Report**

Once it's complete:

1. Go back to **[Code]** tab
2. You should see two new folders:
   - `reports/` - Contains the HTML report and graphs
   - `data/` - Contains generated data files

3. Open the `reports/` folder
4. You should see:
   - `index.html` - The main report
   - `graphs/` - Folder with all PNG charts

### **Step 6: Open in Browser**

Visit this URL (your GitHub Pages URL):

```
https://willangeline-jpg.github.io/tollreports/
```

You should see your beautiful toll reports with:
- ✅ TELUS brand colors (purple & magenta)
- ✅ Worked vs Received charts
- ✅ Monthly, Quarterly, Yearly views
- ✅ IMIS, AEM, Misoteps systems

---

## 🎯 PART 4: Monthly Workflow

Now that it's set up, here's how to use it every month:

### **Every Month (First Day)**

#### **Step 1: Prepare Files**
- Update your Excel files locally
- Keep the same file names:
  - `YBR.xlsx`
  - `2026_Month_end_Misoteps_Exception_and_AEM__1_.xlsx`

#### **Step 2: Upload to GitHub**
1. Go to repository → **[Code]** tab
2. Click **[Add file ▼]** → **Upload files**
3. Select both Excel files
4. Click **[Commit changes]**

#### **Step 3: Wait for Automation**
1. Go to **[Actions]** tab
2. Watch the workflow run (2-3 minutes)
3. See green ✅ checkmark when done

#### **Step 4: Check Reports**
1. Visit: `https://willangeline-jpg.github.io/tollreports/`
2. Refresh the page (Ctrl+R or Cmd+R)
3. See your new reports with latest data!

#### **Step 5: Share with Team**
Send them this link:
```
https://willangeline-jpg.github.io/tollreports/
```

---

## ✅ Verification Checklist

After setup, verify everything works:

### **In GitHub Repository:**
- [ ] `.github/workflows/toll-reports-auto-update.yml` file exists
- [ ] `generate_toll_reports.py` file exists
- [ ] `requirements.txt` file exists
- [ ] `YBR.xlsx` file is uploaded
- [ ] `2026_Month_end_Misoteps_Exception_and_AEM__1_.xlsx` file is uploaded

### **In Actions Tab:**
- [ ] Workflow "Auto-Generate Toll Reports" exists
- [ ] Latest run shows ✅ Success (green checkmark)
- [ ] Reports generated without errors

### **In GitHub Pages:**
- [ ] Pages is enabled (Settings → Pages)
- [ ] URL shows: `https://willangeline-jpg.github.io/tollreports/`

### **In Reports:**
- [ ] `reports/index.html` exists
- [ ] `reports/graphs/` folder has PNG files:
  - [ ] yearly_comparison.png
  - [ ] yearly_imis.png
  - [ ] yearly_aem.png
  - [ ] yearly_misoteps.png
  - [ ] quarterly_*.png files (3 files)
  - [ ] monthly_*.png files (3 files)

### **Online:**
- [ ] Visit: `https://willangeline-jpg.github.io/tollreports/`
- [ ] See beautiful report with TELUS colors
- [ ] Charts show Worked vs Received data
- [ ] Monthly, Quarterly, Yearly sections visible

---

## 🆘 Troubleshooting

### **Problem: Workflow Shows Red ❌ Error**

**Check:**
1. Click the failed workflow to see error details
2. Look for error message in logs
3. Common issues:
   - Excel file names don't match exactly
   - Excel files are corrupted
   - Missing required columns

**Fix:**
1. Fix the Excel file on your computer
2. Delete the bad file from GitHub
3. Re-upload the corrected file
4. Run workflow again

### **Problem: Pages URL Shows 404 Error**

**Solution:**
1. Go to Settings → Pages
2. Verify "Deploy from a branch" is selected
3. Verify branch is **main** and folder is **/ (root)**
4. Wait 2-3 minutes for GitHub Pages to build
5. Try again

### **Problem: Automation Runs But No Reports Appear**

**Solution:**
1. Check that `generate_toll_reports.py` is in the root folder
2. Check that `requirements.txt` is in the root folder
3. Verify Excel files have correct data
4. Run automation manually and check logs

### **Problem: Charts Look Wrong or Are Empty**

**Solution:**
1. Check Excel file structure matches expected format
2. Verify no merged cells in Excel
3. Ensure proper column headers
4. Check for extra blank rows
5. Re-save Excel file and re-upload

---

## 📞 Need Help?

### **Quick Fixes:**

1. **Hard Refresh Browser:** `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
2. **Clear Browser Cache:** Delete cookies and cached files
3. **Try Different Browser:** Sometimes browser cache causes issues
4. **Wait Longer:** GitHub Pages can take 2-3 minutes to update

### **Check These:**

1. Actions tab - Is the workflow succeeding?
2. Settings → Pages - Is GitHub Pages enabled?
3. Code tab - Are all files in the right place?
4. Browser console - Any error messages?

### **Still Stuck?**

1. Check your Excel file format matches documentation
2. Review the README for common issues
3. Contact your team administrator

---

## 🎓 You're All Set! 🎉

Congratulations! Your toll reports system is now:

✅ **Automated** - Runs monthly automatically  
✅ **Branded** - TELUS colors and styling  
✅ **Professional** - Beautiful HTML reports  
✅ **Accessible** - Shared via GitHub Pages URL  
✅ **Scalable** - Easy to add more systems or metrics  

---

## 🚀 What's Next?

### **For Monthly Updates:**
- [ ] Set calendar reminder for 1st of month
- [ ] Prepare Excel files by end of month
- [ ] Upload on 1st of month
- [ ] Share reports with team

### **For Customization:**
- [ ] Edit colors in `generate_toll_reports.py`
- [ ] Add new systems or metrics
- [ ] Modify HTML report layout
- [ ] Create custom analysis views

### **For Team:**
- [ ] Share the GitHub Pages URL
- [ ] Share the team guide (TEAM_MEMBER_GUIDE.docx)
- [ ] Show them how reports work
- [ ] Assign someone to update files monthly

---

## 📚 Resources

| Resource | Link |
|----------|------|
| GitHub Documentation | https://docs.github.com |
| GitHub Pages Guide | https://pages.github.com |
| TELUS Brand Colors | Internal resources |
| This Setup Guide | See above |

---

## ✨ Final Checklist

Before considering setup complete:

- [ ] All files uploaded to GitHub
- [ ] GitHub Pages enabled
- [ ] Workflow runs successfully
- [ ] Reports appear at GitHub Pages URL
- [ ] Team members have access to reports
- [ ] Team guide shared with relevant people
- [ ] Monthly update process documented

---

**Congratulations! Your Toll Reports Dashboard is ready to go!** 🎉📊

For questions, refer to the README or contact your administrator.

Last Updated: September 2026
