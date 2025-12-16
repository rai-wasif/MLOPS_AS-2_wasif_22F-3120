import pandas as pd
import pickle
# from sklearn.model_selection import train_test_split  <-- REMOVED THIS LINE (F401 fix)
from sklearn.ensemble import RandomForestClassifier
import os
import sys

# 1. Load the dataset
print("Loading dataset...")
df = pd.read_csv("data/dataset.csv")

# --- CRITICAL FIX: Clean up column names by stripping hidden spaces ---
df.columns = df.columns.str.strip() 
# ---------------------------------------------------------------------

# 2. Split data into features (X) and target (y)
X = df.drop("target", axis=1)
y = df["target"]

# 3. Train a simple model
print("Training model...")
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

# 4. Ensure the 'models' directory exists before saving
if not os.path.exists("models"):
    os.makedirs("models")

# 5. Save the model to the models folder
output_path = "models/model.pkl"
with open(output_path, "wb") as f:
    pickle.dump(clf, f)

print(f"Model saved to {output_path}")

# Add a single empty line here for W391 fix