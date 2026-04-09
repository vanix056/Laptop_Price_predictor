# 💻 Laptop Price Predictor

## Overview

Laptop Price Predictor is an end-to-end machine learning application that estimates laptop prices based on hardware specifications and configuration. It addresses the practical problem of price opacity in the laptop market by giving buyers and sellers an instant, data-driven price estimate. The model was trained on a real-world dataset of 1,303 laptops, benchmarked against ten regression algorithms, and tuned with GridSearchCV to maximise accuracy. Results are delivered via an interactive Streamlit web app with multi-currency output (USD, PKR, INR).

## Key Features

- **Instant price prediction** from 12 hardware and software features
- **Multi-currency output** — estimates displayed simultaneously in USD, PKR, and INR
- **Advanced configuration panel** — CPU brand, GPU brand, OS, touchscreen, and IPS display toggles
- **PPI-aware display modelling** — pixel-per-inch density computed automatically from resolution and screen size
- **Comprehensive model benchmarking** — 10 algorithms evaluated; final model selected via cross-validated GridSearchCV
- **Animated, responsive UI** — glassmorphism design with floating particles, built entirely in Streamlit

## Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.12 |
| ML Framework | scikit-learn, XGBoost |
| Web UI | Streamlit |
| Data Processing | pandas, NumPy |
| EDA / Visualisation | Matplotlib, Seaborn |
| Model Serialisation | pickle |
| Font / Icons | Google Fonts (Space Grotesk), Font Awesome |

## Installation

### Prerequisites

- Python 3.9 or higher
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/vanix056/Laptop_Price_predictor.git
cd Laptop_Price_predictor

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

## Usage

Start the Streamlit application:

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

1. Select the **brand**, **laptop type**, and **RAM** in the Basic Specs panel.
2. Choose **HDD** and **SSD** storage sizes.
3. Expand **Advanced Settings** to configure processor, GPU, OS, and display options.
4. Enter the **weight** and **screen size**, then select a **resolution**.
5. Click **✨ PREDICT PRICE ✨** to see the estimated price in USD, PKR, and INR.

## Project Structure

```
Laptop_Price_predictor/
├── app.py                        # Streamlit web application
├── Laptop_price_predictor.ipynb  # EDA, feature engineering, and model training notebook
├── laptop_data.csv               # Raw dataset (1,303 laptops, 12 features)
├── pipe.pickle                   # Serialised trained pipeline (preprocessing + model)
├── read_csv.pickle               # Serialised processed DataFrame for UI dropdowns
└── requirements.txt              # Python dependencies
```

## Model Architecture

The prediction pipeline consists of two stages:

1. **Preprocessing** — `ColumnTransformer` with `OneHotEncoder` (drop-first) applied to categorical features: `Company`, `TypeName`, `Cpu brand`, `Gpu brand`, and `os`. Numerical features pass through unchanged.
2. **Regressor** — `RandomForestRegressor` trained on log-transformed prices to reduce skewness. Predictions are exponentiated to recover the final price.

**Final hyperparameters** (selected by 5-fold GridSearchCV):

| Parameter | Value |
|---|---|
| `n_estimators` | 300 |
| `max_depth` | 25 |
| `max_features` | 0.7 |
| `max_samples` | 0.9 |
| `min_samples_split` | 2 |
| `min_samples_leaf` | 1 |

## Dataset

- **Source:** Publicly available laptop specifications dataset
- **Size:** 1,303 records × 12 columns
- **Raw features:** `Company`, `TypeName`, `Inches`, `ScreenResolution`, `Cpu`, `Ram`, `Memory`, `Gpu`, `OpSys`, `Weight`, `Price`
- **Engineered features:** `Cpu brand`, `Gpu brand`, `os`, `Touchscreen`, `IPS`, `PPI` (pixels per inch), `HDD`, `SSD`
- **Target:** `log(Price)` in PKR (converted from EUR at a rate of 3.22)

## Training

Open the Jupyter notebook to reproduce all experiments:

```bash
jupyter notebook Laptop_price_predictor.ipynb
```

The notebook covers:
1. Data loading and exploratory data analysis
2. Feature extraction and engineering
3. Train / test split
4. Benchmarking of 10 regression models
5. VotingRegressor ensemble experimentation
6. GridSearchCV hyperparameter tuning for `RandomForestRegressor`
7. Model serialisation with `pickle`

## Evaluation Metrics

All models were evaluated on a held-out test set using:

- **R² Score** — proportion of price variance explained
- **Mean Absolute Error (MAE)** — average absolute deviation on the log-price scale

## Results

| Model | R² Score | MAE (log scale) |
|---|---|---|
| Linear Regression | 0.8073 | 0.2102 |
| Ridge Regression | 0.8127 | 0.2093 |
| Lasso Regression | 0.8072 | 0.2111 |
| K-Nearest Neighbours | 0.8031 | 0.1926 |
| Decision Tree | 0.8411 | 0.1831 |
| SVR (RBF kernel) | 0.8082 | 0.2024 |
| Gradient Boosting | 0.8809 | 0.1602 |
| AdaBoost | 0.7902 | 0.2319 |
| ExtraTrees | 0.8860 | 0.1582 |
| XGBoost | 0.8893 | 0.1548 |
| **Random Forest (tuned)** | **0.8904** | **0.1545** |

> Cross-validated R² of the final model: **0.8651**

## Configuration

No environment variables are required. The application loads two pre-built pickle files at startup:

| File | Description |
|---|---|
| `pipe.pickle` | Full scikit-learn pipeline (preprocessor + RandomForestRegressor) |
| `read_csv.pickle` | Processed DataFrame used to populate UI dropdown options |

If you retrain the model in the notebook, re-run the final `pickle.dump` cells to overwrite these files before restarting the app.

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository and create a feature branch (`git checkout -b feature/your-feature`).
2. Make your changes and ensure the notebook runs end-to-end without errors.
3. Open a pull request with a clear description of your changes.

Please keep commits focused and avoid unrelated refactors in the same PR.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Author

**Abdullah Waqar** ([@vanix056](https://github.com/vanix056))

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdullahwaqar/)
[![GitHub](https://img.shields.io/badge/GitHub-vanix056-black?style=flat&logo=github)](https://github.com/vanix056)
