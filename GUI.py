import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import numpy as np
import pandas as pd

# Load models
try:
    poly_model = joblib.load("LinearRegression_model.pkl")
    rf_model = joblib.load("Random_Forest_Regressor_model.pkl")
except FileNotFoundError as e:
    print("❌ Make sure your model .pkl files are in the same directory!")
    raise e

# Predict function
def predict():
    try:
        temp = float(temp_entry.get())
        time = float(time_entry.get())
        model_choice = model_var.get()

        input_df = pd.DataFrame([[1100, 8]], columns=["Furnace Temeprature (c)", "Time (h)"])

        if model_choice == "Polynomial Regression":
            result = poly_model.predict(input_df)[0]
        elif model_choice == "Random Forest":
            result = rf_model.predict(input_df)[0]
        else:
            raise ValueError("Invalid model selected.")

        result_label.config(text=f"🔍 Predicted Scale Weight: {result:.3f} Kg/m²")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("Scale Weight Predictor")

root.geometry("400x300")
root.resizable(False, False)

# Model Selection
ttk.Label(root, text="Select Model:", font=("Arial", 12)).pack(pady=10)
model_var = tk.StringVar(value="Polynomial Regression")
model_dropdown = ttk.Combobox(root, textvariable=model_var, state="readonly",
                              values=["Polynomial Regression", "Random Forest"])
model_dropdown.pack()

# Input Fields
ttk.Label(root, text="Furnace Temperature (°C):", font=("Arial", 10)).pack(pady=(20, 5))
temp_entry = ttk.Entry(root)
temp_entry.pack()

ttk.Label(root, text="Time (h):", font=("Arial", 10)).pack(pady=5)
time_entry = ttk.Entry(root)
time_entry.pack()

# Predict Button
predict_button = ttk.Button(root, text="Predict", command=predict)
predict_button.pack(pady=20)

# Output
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()