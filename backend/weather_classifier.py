"""
Weather Classifier Pipeline
"""
import pandas as pd
import numpy as np

def load_weather_data(filepath="backend/weather_data.csv"):
    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    df = load_weather_data()
    print(f"Loaded weather dataset: {df.shape}")
