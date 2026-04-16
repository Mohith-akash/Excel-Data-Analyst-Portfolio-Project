# Advanced Excel Data Analyst Portfolio Project

This repository contains a detailed analysis of **12,894 unique job postings**, built entirely in Microsoft Excel. The project transforms 60MB of raw, messy data into a fully interactive, multi-chart dashboard.

This project demonstrates advanced proficiency in **Power Query**, the **Power Pivot Data Model**, **DAX**.

---

## Dashboard Preview

![Top 15 Skills](Dashboard%202.png)
![Most Required Postings](DashBoard%201.png)
![Job Postings by Country](Dashboard%203.png)
![Most Used Words](Dashboard%204.png)

---

## Key Findings & Statistics

* **Total Jobs Analyzed:** **12,894** unique postings.
* **Skill Analysis:** Processed **228,745** individual skill mentions. The top 3 skills are **Data analysis**, **SQL**, and **Project management**.
* **Job Title Analysis:** Standardized over 2,000 messy job titles. The top 3 most common roles are **Data Analyst** (4,058 jobs), **Business Analyst** (1,978 jobs), and **System Analyst** (1,167 jobs).
* **Keyword Analysis:** Processed **3.1+ million** words. The top keywords are **'business'** (305k), **'data'** (284k), and **'systems'** (85k).
* **Geography:** The **United States** accounts for **10,386** of the job postings.

---

## Technical Workflow & Skills Demonstrated

### 1. Data Cleaning & Transformation (Power Query)
* Executed **70+ sequential steps** to clean and standardize the 13k-row dataset.
* Used **Conditional Columns** (with 35+ rules) to consolidate 2,000+ messy job titles into ~20 clean, standard roles.
* Used **Split Column** and **Unpivot Other Columns** to transform the `job_skills` column into 228,745 rows for analysis.

### 2. Data Modeling (Power Pivot & DAX)
* Loaded the final 228,745-row table into the **Excel Data Model (Power Pivot)** to bypass Excel's row limit and enable high-performance analysis.
* Wrote a custom **DAX** measure to solve the "fan trap" problem and accurately count the true number of unique jobs:
    * `Total Unique Postings = DISTINCTCOUNT('postings 2'[job_link])`
* This measure correctly returns the **12,894** job total from the 228k-row data model.

### 3. Data Visualization (Interactive Dashboard)
* Built 4 **PivotCharts** based on the Data Model.
* Connected all charts to 3 master **Slicers** (`job_level`, `job_type`, `search_country`) using **Report Connections** for a fully interactive experience.

### 4. Version Control (Git LFS)
* Used **Git LFS (Large File Storage)** to version control and upload the 35MB Excel file and 60MB CSV file, bypassing GitHub's 25MB limit.

---

## Files in this Repository

* **`Data Analysis Job Analysis Final.xlsx` (35MB):** The final Excel workbook containing all Power Query steps, the Data Model, DAX measures, and the interactive dashboard.
* **`raw postings file.csv` (60MB):** The original, raw data source.
* **`DashBoard 1.png`, `Dashboard 2.png`, `Dashboard 3.png`, `Dashboard 4.png`:** Screenshots of the final dashboard.
