print("AUTO ML TRAINING STARTED")

import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputRegressor

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR

from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)

# =========================
# CREATE MODELS FOLDER
# =========================

os.makedirs("models", exist_ok=True)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("dataset/materials.csv")

print("\nDataset Loaded Successfully")

# =========================
# INPUT FEATURES
# =========================

X = df[[
    "Hardness",
    "Density",
    "Temperature",
    "Load",
    "Speed"
]]

# =========================
# TARGET OUTPUTS
# =========================

Y = df[[
    "WearRate",
    "FrictionCoefficient"
]]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# =========================
# FEATURE SCALING
# =========================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# =========================
# CANDIDATE MODELS
# =========================

models = {

    "Linear Regression":
    MultiOutputRegressor(
        LinearRegression()
    ),

    "Random Forest":
    RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "Support Vector Machine":
    MultiOutputRegressor(
        SVR()
    ),

    "Gradient Boosting":
    MultiOutputRegressor(
        GradientBoostingRegressor()
    )
}

# =========================
# AUTOMATED MODEL SELECTION
# =========================

best_model = None

best_model_name = ""

best_score = -999

best_r2 = None

best_rmse = None

best_mae = None

print("\nTraining Multiple Models...\n")

# =========================
# TRAIN & EVALUATE MODELS
# =========================

for model_name, model in models.items():

    print(f"\nTraining {model_name}...")

    # =========================
    # TRAIN MODEL
    # =========================

    model.fit(
        X_train_scaled,
        y_train
    )

    # =========================
    # PREDICTIONS
    # =========================

    predictions = model.predict(
        X_test_scaled
    )

    # =========================
    # EVALUATION METRICS
    # =========================

    r2 = r2_score(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(mse)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    # =========================
    # COMPOSITE PERFORMANCE SCORE
    # =========================

    final_score = (
        (0.5 * r2)
        - (0.3 * rmse)
        - (0.2 * mae)
    )

    # =========================
    # PRINT METRICS
    # =========================

    print(f"R2 Score : {r2}")

    print(f"MSE : {mse}")

    print(f"RMSE : {rmse}")

    print(f"MAE : {mae}")

    print(f"Final Score : {final_score}")

    print("-" * 50)

    # =========================
    # SELECT BEST MODEL
    # =========================

    if final_score > best_score:

        best_score = final_score

        best_r2 = r2

        best_rmse = rmse

        best_mae = mae

        best_model = model

        best_model_name = model_name

# =========================
# FINAL BEST MODEL
# =========================

print("\nBEST MODEL SELECTED")

print(f"Model Name : {best_model_name}")

print(f"Best Composite Score : {best_score}")

print(f"Best R2 Score : {best_r2}")

print(f"Best RMSE : {best_rmse}")

print(f"Best MAE : {best_mae}")

# =========================
# SAVE BEST MODEL
# =========================

joblib.dump(
    best_model,
    "models/property_predictor.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)
print(df["FrictionCoefficient"].value_counts())
print("\nBest Model Saved Successfully")