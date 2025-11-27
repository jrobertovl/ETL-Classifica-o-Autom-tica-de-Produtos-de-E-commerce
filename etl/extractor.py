import pandas as pd
import os

def extract(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")
    return pd.read_csv(path)
