import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Laliga Revenue.csv")
df = df.iloc[:, :6]
df.columns = df.columns.str.strip()
df["Average TV Revenue (€M)"] = (df["Average TV Revenue (€M)"].astype(str).str.replace(",","").astype(float))
df = df.sort_values(by="Average TV Revenue (€M)", ascending=True)
df.plot(kind="barh", x="Club", y="Average TV Revenue (€M)", color="skyblue", legend="False", figsize=(10,8))
plt.title("LaLiga Clubs by Average TV Revenue (€M)", fontsize=12)
plt.ylabel("Club", fontsize=12)
plt.tight_layout()
plt.show()