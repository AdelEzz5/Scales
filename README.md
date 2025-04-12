# 🏗️ Steel Scale Weight Prediction using Machine Learning  
*A machine learning-based prediction model for estimating the weight of steel scale formed during the reheating process in a rolling mill.*

---

## 📌 Project Overview

This project provides an interactive machine learning tool to predict the **steel scale weight (Kg/m²)** that forms on raw material during reheating in a **rolling mill furnace**. The scale is a key production factor that results in material loss and must be monitored.

The prediction is based on two primary parameters:
- **Furnace Temperature (°C)**
- **Processing Time (h)**

Other influencing parameters such as **excess air**, **furnace pressure**, and **gas composition** are considered **constant** in this model to simplify training.

---

## 🏭 Data Source

The dataset was collected from a **reheating furnace** at **Egarhy Steel Company**. It includes real production data representing furnace conditions and scale weight collected from surface measurements.

---

## 🤖 Machine Learning Models Used

We implemented and compared the performance of the following models:
- **Polynomial Regression** (Degree 4)
- **Random Forest Regressor**

Both models were trained and evaluated using RMSE and residual analysis. The Polynomial Regression model achieved an RMSE as low as **0.017 Kg/m²** on test data.

---

## 🖥️ GUI Application

A **Tkinter-based GUI** is included for practical use. Users can:
- Select a model
- Input furnace temperature and processing time
- Instantly receive a scale weight prediction

### 📦 Models are loaded using:
- `LinearRegression_model.pkl`
- `Random_Forest_Regressor_model.pkl`

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/AdelEzz5/scale-weight-ml.git
cd scale-weight-ml
```

### 2. Install dependencies
```bash
pip install numpy pandas scikit-learn matplotlib joblib
```

### 3. Run the GUI
```bash
python GUI.py
```

Or launch the notebook version:
```bash
jupyter notebook scale_weight_prediction.ipynb
```

---

## 📊 Results & Performance

| Model                   | RMSE (Test Set) | Cross-Validated RMSE     |
|------------------------|-----------------|---------------------------|
| Polynomial Regression  | **0.017**       | 0.0159 ± 0.0041           |
| Random Forest Regressor| ~0.000 (train)  | 0.4626 ± 0.1581 (overfit) |

---

## 📁 Files Included

- `scale_weight_prediction.ipynb` – Notebook for model training, evaluation, and GUI
- `scale_weight_gui.py` – GUI application script
- `LinearRegression_model.pkl` – Saved polynomial regression model
- `Random_Forest_Regressor_model.pkl` – Saved random forest model
- `README.md` – This documentation

---

## 🤝 Acknowledgments

- Special thanks to **Egarhy Steel Company** for providing the real-world dataset.
- Developed as part of a research and optimization initiative in industrial data science.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
