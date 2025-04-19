from src.file_handler import parse_dxf
import numpy as np
import pandas as pd

dxf_path = r"C:\Users\Yoni\OneDrive\Desktop\Kolango- Delbena Gama- Gato Road Project Plan.dxf"

df = parse_dxf(dxf_path)
df['station'] = 0.0

for i in range(1, len(df)):
    x0, y0 = df.loc[i-1, 'X'], df.loc[i-1, 'Y']
    x1, y1 = df.loc[i, 'X'], df.loc[i, 'Y']
    dist = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    df.loc[i, 'station'] = df.loc[i-1, 'station'] + dist

total_length_km = df['station'].iloc[-1] / 1000

# Show all points in terminal (if needed)
# print(df.to_string(index=False))

# Save to CSV
df.to_csv("data/output/parsed_alignment.csv", index=False)

print(f"\n✅ Total alignment length: {total_length_km:.2f} km")
print(f"✅ Total points: {len(df)}")
print("✅ Alignment data saved to: data/output/parsed_alignment.csv")
