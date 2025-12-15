import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os
import sys

# Add project root to sys path so tests can run (important for Task 2.2)
# sys.path.append(os.path.dirname(os.path.abspath(__file__))) # This is not strictly needed for this fix, but good practice

# 1. Load the dataset
print("Loading dataset...")
df = pd.read_csv("data/dataset.csv")

# --- FIX: Clean up column names by stripping spaces ---
df.columns = df.columns.str.strip() 
# -----------------------------------------------------

# 2. Split data into features (X) and target (y)
X = df.drop("target", axis=1)
y = df["target"]

# 3. Train a simple model
print("Training model...")
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X, y)

# 4. Save the model to the models folder
output_path = "models/model.pkl"
with open(output_path, "wb") as f:
    pickle.dump(clf, f)

print(f"Model saved to {output_path}")