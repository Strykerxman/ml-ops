import pandas as pd
import numpy as np
import os
import pickle
from sklearn.ensemble import RandomForestClassifier
import yaml

def load_params(params_path: str) -> int:
    try:
        with open(params_path,"r") as f:
            params = yaml.safe_load(f)
        return params["model_building"]["n_estimators"]
    except Exception as e:
        raise Exception(f"Error loading parameters from {params_path}: {e}")

def load_data(filepath: str) -> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise Exception(f"Error loading data from {filepath}: {e}")

def prepare_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    try:
        X = data.drop(columns=["Potability"], axis=1)
        y = data["Potability"]
        return X, y
    except Exception as e:
        raise Exception(f"Error preparing data: {e}")

def train_model(X: pd.DataFrame, y: pd.Series, n_estimators: int) -> RandomForestClassifier:
    try:
        clf = RandomForestClassifier(n_estimators=n_estimators)
        clf.fit(X, y)
        return clf
    except Exception as e:
        raise Exception(f"Error training model: {e}")

def save_model(model: RandomForestClassifier, filepath: str) -> None:
    try:
        with open(filepath, "wb") as f:
            pickle.dump(model, f)
    except Exception as e:
        raise Exception(f"Error saving model to {filepath}: {e}")

def main():
    params_path = "params.yaml"
    data_path = "./data/processed/train_processed.csv"
    model_path = "model.pkl"
    try:
        n_estimators = load_params(params_path)
        train_data = load_data(data_path)
        X_train, y_train = prepare_data(train_data)

        model = train_model(X_train, y_train, n_estimators)
        save_model(model, model_path)
    except Exception as e:
        raise Exception(f"An error occured: {e}")

if __name__ == "__main__":
    main()
