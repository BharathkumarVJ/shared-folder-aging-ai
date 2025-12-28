import os
import pandas as pd
from datetime import datetime

base_path = r"base_path = r"C:\Users\thebh\Desktop\python"

data = []

for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        pdf_dates = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(".pdf"):
                    pdf_dates.append(os.path.getmtime(os.path.join(root, file)))
        if pdf_dates:
            oldest = min(pdf_dates)
            data.append({
                "folder_name": folder,
                "oldest_modified_date": datetime.fromtimestamp(oldest)
            })

df = pd.DataFrame(data)
df["days_inactive"] = (datetime.now() - df["oldest_modified_date"]).dt.days
df["risk_flag"] = df["days_inactive"].apply(lambda x: "HIGH RISK" if x > 180 else "OK")

df.to_csv("sample_output/folder_aging_report.csv", index=False)
print(df)
