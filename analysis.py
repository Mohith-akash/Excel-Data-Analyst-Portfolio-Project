"""
Companion script to the Excel dashboard.

Reproduces the "Top Skills by Demand" finding using pandas, as a sanity
check against the Power Query + Data Model version in the .xlsx file.

The full analysis (70+ Power Query steps, Power Pivot Data Model,
DAX measures, 4 interactive PivotCharts with slicers) lives in
'Data Analysis Job Analysis Final.xlsx'. This script is a minimal
code artifact for reviewers who want to see the core transformation
logic at a glance.

Expected result (per README): top 3 skills are Data analysis, SQL,
Project management, out of ~228,745 total skill mentions across
12,894 unique postings.
"""
import pandas as pd

CSV_PATH = "raw postings file.csv"

# Load only the columns we need. job_link is used to dedupe postings,
# mirroring the DAX measure: DISTINCTCOUNT('postings 2'[job_link]).
df = pd.read_csv(CSV_PATH, usecols=["job_link", "job_skills"])

# Drop rows with no skills listed (matches Power Query's filter step).
df = df.dropna(subset=["job_skills"])
df = df[df["job_skills"].str.strip() != ""]

# Dedupe on job_link so one posting contributes its skills once.
df = df.drop_duplicates(subset=["job_link"])

# Split the comma-separated job_skills column into one row per skill
# (the Power Query equivalent is Split Column -> Unpivot Other Columns).
skills = (
    df["job_skills"]
    .str.split(",")
    .explode()
    .str.strip()
)
skills = skills[skills != ""]

# Case-normalize so 'Data Analysis' and 'Data analysis' merge, then
# title-case for display. The Excel version does similar consolidation
# via Conditional Columns in Power Query.
skills = skills.str.lower().str.title()

print(f"Unique postings with skills: {df['job_link'].nunique():,}")
print(f"Total skill mentions:        {len(skills):,}")
print()
print("Top 15 skills by job postings mentioning them:")
print(skills.value_counts().head(15).to_string())
