#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    # Load data from various formats (CSV, Excel, SQL)
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

    return data

def handle_missing_values(data):
    # Handle missing values
    data = data.dropna()  # Drop rows with missing values for simplicity
    return data

def main():
    # Get user input for data file
    file_path = input("Enter the path to the data file: ")

    # Load data
    try:
        data = load_data(file_path)
        print("Data loaded successfully.")
    except Exception as e:
        print("Error loading data:", e)
        return

    # Preprocess data
    data = handle_missing_values(data)
    print("Data preprocessed.")

    
if __name__ == "__main__":
    main()


# In[ ]:




