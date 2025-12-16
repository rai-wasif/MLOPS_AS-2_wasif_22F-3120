import pandas as pd
import os
import pickle
import pytest
# We removed "from src.train import clf" here, 
# as the tests rely on the saved model.pkl file instead.

# A fixture to ensure dependencies are loaded before tests run
@pytest.fixture(scope="session", autouse=True)
def run_training_script():
    # This runs the training script once before all tests
    # to ensure the model and data are available (i.e., model.pkl is saved).
    print("\n--- Running src/train.py to ensure model.pkl is available ---")
    os.system("python src/train.py")
    print("------------------------------------------------------------------")
    
def test_data_loading_shape():
    """Test if the dataset loads correctly and has the expected shape."""
    # We must explicitly use the fix you put in train.py by stripping columns
    df = pd.read_csv("data/dataset.csv")
    df.columns = df.columns.str.strip() # Re-apply the column strip logic for safety
    
    # Check if we have 3 rows and 3 columns
    expected_rows = 3
    expected_cols = 3
    assert df.shape == (expected_rows, expected_cols), "Dataset shape is incorrect"

def test_target_column_exists():
    """Test if the 'target' column is present."""
    df = pd.read_csv("data/dataset.csv")
    df.columns = df.columns.str.strip() # Re-apply the column strip logic for safety
    assert "target" in df.columns, "Target column 'target' is missing from the dataset"
    
def test_model_pkl_exists():
    """Test if the trained model file was saved."""
    model_path = "models/model.pkl"
    assert os.path.exists(model_path), "Model file model.pkl was not found"

def test_model_can_predict():
    """Test if the loaded model can make a prediction."""
    model_path = "models/model.pkl"
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
        
    # Test with dummy data (must have the same number of features as training data: 2)
    dummy_input = pd.DataFrame({'feature1': [0.5], 'feature2': [0.5]})
    
    # Check if prediction runs without error and returns 1 prediction
    try:
        prediction = model.predict(dummy_input)
        assert len(prediction) == 1, "Model did not return exactly one prediction"
    except Exception as e:
        pytest.fail(f"Model prediction failed: {e}")