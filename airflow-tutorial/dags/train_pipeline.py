from __future__ import annotations

import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

# --- Python Functions for Tasks ---
def load_data():
    """Simulates loading data from a source."""
    print("TASK: Data successfully loaded from source.")
    # ...

def preprocess_data():
    """Simulates data cleaning and feature engineering."""
    print("TASK: Data successfully cleaned and preprocessed.")
    # ...

def train_model():
    """Simulates training a Machine Learning model."""
    print("TASK: ML Model training complete. Model saved to storage.")
    # ...


# --- Airflow DAG Definition ---

with DAG(
    dag_id="ml_training_pipeline",
    start_date=pendulum.datetime(2023, 10, 26, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["mlops", "training"],
    doc_md=__doc__,
) as dag:
    
    task_load_data = PythonOperator(
        task_id="data_loading",
        python_callable=load_data,
    )

    task_preprocess_data = PythonOperator(
        task_id="data_preprocessing",
        python_callable=preprocess_data,
    )

    task_train_model = PythonOperator(
        task_id="model_training",
        python_callable=train_model,
    )

    # Define the task dependencies
    task_load_data >> task_preprocess_data >> task_train_model