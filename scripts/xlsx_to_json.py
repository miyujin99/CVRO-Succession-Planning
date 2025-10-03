import pandas as pd, json, sys

# đọc file Excel
df = pd.read_excel("assets/departments.xlsx", sheet_name=0)

# chuẩn hóa tên cột
df.columns = [c.strip().lower() for c in df.columns]

# group theo dept_key + dept_name
out = {}
for (k, name), g in df.groupby(["dept_key","dept_name"], dropna=False):
    roles = sorted(r for r in g["role"].dropna().astype(str).unique())
    out[str(k)] = {"name": str(name), "roles": roles}

# ghi file JSON ra /data
with open("data/departments.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("✅ Generated departments.json")
