import pandas as pd

# Đọc 2 file Excel
df_population = pd.read_excel("dân số 2025.xlsx")
df_gdp = pd.read_excel("gdp normal per capita 2025.xlsx")

# (Tuỳ chọn) chuẩn hoá cột country: bỏ khoảng trắng, đồng nhất kiểu chuỗi
df_population["country"] = df_population["country"].astype(str).str.strip()
df_gdp["country"] = df_gdp["country"].astype(str).str.strip()

# Ghép theo cột đúng là 'country'
df_merged = pd.merge(
    df_population,
    df_gdp,
    on="country",
    how="inner"
)

# Lưu file kết quả
df_merged.to_excel("population_gdp_2025_merged.xlsx", index=False)

print("✅ Ghép bảng thành công -> population_gdp_2025_merged.xlsx")
print("Số dòng sau khi ghép:", len(df_merged))
