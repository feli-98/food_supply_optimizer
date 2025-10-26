import pandas as pd
import numpy as np

np.random.seed(42)

n = 100
data = {
    'region': [f'Region_{i}' for i in range(n)],
    'surplus': np.random.randint(100, 1000, size=n),
    'deficit': np.random.randint(50, 800, size=n),
    'distance_km': np.random.uniform(10, 500, size=n).round(2),
    'cost_per_km': np.random.uniform(0.5, 5.0, size=n).round(2),
    'perishability': np.random.uniform(0.1, 1.0, size=n).round(2),
    'population': np.random.randint(1000, 100000, size=n),
    'market_price': np.random.uniform(10, 100, size=n).round(2)
}

df = pd.DataFrame(data)
df.to_csv('food_allocation.csv', index=False)
print("✅ Simulated dataset saved as food_allocation.csv")