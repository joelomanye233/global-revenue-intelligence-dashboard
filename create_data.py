import pandas as pd
import numpy as np

# Branch names
branches = [
    "New York Branch", "Los Angeles Branch", "Chicago Branch", "Houston Branch",
    "Phoenix Branch", "Philadelphia Branch", "San Antonio Branch", "San Diego Branch",
    "Dallas Branch", "San Jose Branch", "Austin Branch", "Jacksonville Branch",
    "Fort Worth Branch", "Columbus Branch", "Charlotte Branch", "Indianapolis Branch",
    "Seattle Branch", "Denver Branch", "Washington DC Branch", "Boston Branch"
]

# Years and months
years = [2024, 2025, 2026, 2027, 2028]
months = list(range(1, 13))

data = []

np.random.seed(42)  # for reproducibility

for year in years:
    for month in months:
        for branch in branches:
            # Random revenue between 5000 and 20000
            revenue = np.random.randint(5000, 20001)
            date = pd.Timestamp(year=year, month=month, day=1)
            data.append([date, branch, f"${revenue}"])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "Branch", "Revenue"])

# Parse Revenue to numeric
df["RevenueNumeric"] = df["Revenue"].str.replace("$", "", regex=True).astype(float)

# Save to CSV
df.to_csv("test_data.csv", index=False)
print("✅ test_data.csv created successfully with 20 branches, 5 years, 12 months each!")
