import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# ----------------- 1. INITIALIZATION -----------------

# Path to the saved model (adjust if your model.pkl is saved elsewhere)
MODEL_PATH = "models/model.pkl" 

# Load the trained model globally when the application starts
try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}")
    model = None # Set model to None if loading fails

# Create the FastAPI app instance
app = FastAPI(
    title="MLOps Model Inference API",
    description="A simple API for predicting housing prices.",
    version="1.0.0"
)

# Define the data structure for the prediction input using Pydantic
# NOTE: Replace these placeholder feature names/types with your model's actual inputs!
class PredictIn(BaseModel):
    feature_1: float
    feature_2: int
    feature_3: str = "default_value"

# ----------------- 2. ENDPOINTS -----------------

@app.get("/health", tags=["Monitoring"])
def get_health():
    """
    Health check endpoint.
    """
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict", tags=["Prediction"])
def predict_price(data: PredictIn):
    """
    Prediction endpoint.
    Accepts input features and returns the model's predicted output.
    """
    if model is None:
        return {"error": "Model not loaded. Check /health status."}

    try:
        # Convert the Pydantic input data into a DataFrame (required for scikit-learn)
        # We must maintain the order of features expected by the model!
        input_data = pd.DataFrame([data.dict()])
        
        # --- Preprocessing (Add any necessary preprocessing here!) ---
        # Example: if your model expects specific feature scaling or one-hot encoding,
        # you must apply it here before calling model.predict()

        # Make the prediction
        prediction = model.predict(input_data)
        
        # Return the result
        return {"prediction": prediction.tolist()[0]}

    except Exception as e:
        # Log the detailed error
        print(f"Prediction Error: {e}")
        return {"error": f"An error occurred during prediction: {str(e)}"}

# ----------------- 3. RUNNING (handled by uvicorn) -----------------
# The command below runs the application:
# uvicorn api.main:app --reload