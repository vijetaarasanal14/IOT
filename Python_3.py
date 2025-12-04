import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# ---------------------------------------------------------
# 1. Define ChipBlock class
# ---------------------------------------------------------
class ChipBlock:
    def __init__(self, name, delay, dynamic_power, leakage, area):
        self.name = name
        self.delay = delay
        self.dynamic_power = dynamic_power
        self.leakage = leakage
        self.area = area

    # Performance Index (lower is better)
    def performance_index(self):
        return self.delay * (self.dynamic_power + self.leakage)

    # Power Density (W/mm^2)
    def power_density(self):
        return (self.dynamic_power + self.leakage) / self.area

    # Timing violation detection (threshold = 1 ns)
    def has_timing_violation(self, limit=1.0):
        return self.delay > limit


# ---------------------------------------------------------
# 2. Sample Input Data (You can modify or load externally)
# ---------------------------------------------------------
data = [
    ("ALU", 0.8, 20, 5, 1.2),
    ("FPU", 1.3, 25, 6, 1.0),
    ("L1 Cache", 0.6, 15, 4, 2.0),
    ("Decoder", 1.1, 10, 3, 0.8),
    ("Control Unit", 0.9, 12, 4, 1.5),
]


# ---------------------------------------------------------
# 3. Convert input data into ChipBlock objects
# ---------------------------------------------------------
blocks = [ChipBlock(*row) for row in data]


# ---------------------------------------------------------
# 4. Create Pandas DataFrame from objects
# ---------------------------------------------------------
df = pd.DataFrame({
    "Block": [b.name for b in blocks],
    "Delay (ns)": [b.delay for b in blocks],
    "Dynamic Power (mW)": [b.dynamic_power for b in blocks],
    "Leakage (mW)": [b.leakage for b in blocks],
    "Area (mm^2)": [b.area for b in blocks],
    "Performance Index": [b.performance_index() for b in blocks],
    "Power Density": [b.power_density() for b in blocks],
    "Timing Violation": [b.has_timing_violation() for b in blocks]
})


# ---------------------------------------------------------
# 5. NumPy calculations
# ---------------------------------------------------------
mean_delay = np.mean(df["Delay (ns)"])
max_power_density = np.max(df["Power Density"])

print("Mean Delay:", mean_delay)
print("Maximum Power Density:", max_power_density)


# ---------------------------------------------------------
# 6. Identify the worst block by performance index
# ---------------------------------------------------------
worst_block = df.loc[df["Performance Index"].idxmax()]
print("\nWorst Block Based on Performance Index:")
print(worst_block)


# ---------------------------------------------------------
# 7. Generate CSV and JSON reports
# ---------------------------------------------------------
df.to_csv("vlsi_summary.csv", index=False)
df.to_json("vlsi_summary.json", orient="records", indent=4)

print("\nFiles saved: vlsi_summary.csv, vlsi_summary.json")


# ---------------------------------------------------------
# 8. Delay Bar Plot
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Block"], df["Delay (ns)"])
plt.xlabel("Block")
plt.ylabel("Delay (ns)")
plt.title("Delay Comparison of VLSI Blocks")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
