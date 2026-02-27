import pandas as pd

# Files list
files = ["data/raw/posts.csv", 
         "data/raw/comments.csv", 
         "data/raw/jobs.csv",
         "data/raw/applications.csv"]

report = []

for file in files:
    df = pd.read_csv(file)
   
    total_rows = len(df)
    missing_values = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    
    invalid_dates = 0
    if "created_at" in df.columns:
        invalid_dates = pd.to_datetime(df["created_at"], errors="coerce").isna().sum()
    
    report.append([file, total_rows, missing_values, duplicates, invalid_dates])

report_df = pd.DataFrame(report, 
                         columns=["file_name", "total_rows", "missing_values", "duplicates", "invalid_dates"])

report_df.to_csv("data_quality_report.csv", index=False)

print(report_df)
import os

os.makedirs("outputs", exist_ok=True)

report_df.to_csv("outputs/data_quality_report.csv", index=False)

print("Data quality report saved successfully!")