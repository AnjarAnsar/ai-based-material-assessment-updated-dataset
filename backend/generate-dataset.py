import pandas as pd
import numpy as np
import os

np.random.seed(42)
print("SCRIPT STARTED")
# =========================
# MATERIAL DATABASE
# =========================

materials = {

    "Steel": {
        "hardness": (60, 85),
        "density": (7.7, 7.9),
        "friction": (0.5, 0.9)
    },

    "Aluminum": {
        "hardness": (40, 60),
        "density": (2.6, 2.8),
        "friction": (0.3, 0.8)
    },

    "Brass": {
        "hardness": (45, 65),
        "density": (8.3, 8.7),
        "friction": (0.4, 0.9)
    },

    "Bronze": {
        "hardness": (55, 75),
        "density": (8.6, 8.9),
        "friction": (0.4, 0.9)
    },

    "CastIron": {
        "hardness": (70, 90),
        "density": (7.1, 7.4),
        "friction": (0.5, 0.9)
    },

    "PTFE": {
        "hardness": (5, 15),
        "density": (2.1, 2.3),
        "friction": (0.1, 0.3)
    },

    "Graphite": {
        "hardness": (10, 25),
        "density": (1.8, 2.2),
        "friction": (0.1, 0.35)
    },

    "Titanium": {
        "hardness": (75, 90),
        "density": (4.4, 4.6),
        "friction": (0.3, 0.7)
    },

    "Copper": {
        "hardness": (35, 50),
        "density": (8.8, 9.0),
        "friction": (0.4, 0.9)
    },

    "Nickel": {
        "hardness": (65, 80),
        "density": (8.7, 8.9),
        "friction": (0.4, 0.9)
    },

    "Magnesium": {
        "hardness": (30, 45),
        "density": (1.6, 1.8),
        "friction": (0.3, 0.7)
    },

    "Zinc": {
        "hardness": (25, 40),
        "density": (7.0, 7.2),
        "friction": (0.3, 0.7)
    },

    "Ceramic": {
        "hardness": (85, 100),
        "density": (3.5, 4.0),
        "friction": (0.2, 0.5)
    },

    "Inconel": {
        "hardness": (80, 100),
        "density": (8.1, 8.5),
        "friction": (0.3, 0.8)
    },

    "Tungsten": {
        "hardness": (90, 100),
        "density": (19.0, 19.4),
        "friction": (0.4, 0.8)
    }
}

# =========================
# GENERATE DATA
# =========================

rows = []

samples_per_material = 300

for material, props in materials.items():

    for _ in range(samples_per_material):

        hardness = round(
            np.random.uniform(*props["hardness"]),
            2
        )

        density = round(
            np.random.uniform(*props["density"]),
            2
        )

        temperature = np.random.randint(
            25,
            801
        )

        load = np.random.randint(
            5,
            201
        )

        speed = np.random.randint(
            50,
            1001
        )

        friction = round(
            np.random.uniform(*props["friction"]),
            4
        )

        wear_rate = (
            load * temperature
        ) / (
            hardness * speed
        )

        wear_rate *= np.random.uniform(
            0.8,
            1.2
        )

        wear_rate = round(
            max(0.01, wear_rate),
            4
        )

        rows.append([
            material,
            hardness,
            density,
            temperature,
            load,
            speed,
            wear_rate,
            friction
        ])

# =========================
# CREATE DATAFRAME
# =========================

df = pd.DataFrame(
    rows,
    columns=[
        "Material",
        "Hardness",
        "Density",
        "Temperature",
        "Load",
        "Speed",
        "WearRate",
        "FrictionCoefficient"
    ]
)

# =========================
# SAVE DATASET
# =========================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset"
)

os.makedirs(
    DATASET_DIR,
    exist_ok=True
)

DATASET_PATH = os.path.join(
    DATASET_DIR,
    "materials.csv"
)

df.to_csv(
    DATASET_PATH,
    index=False
)

print("\nDataset Created Successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nSaved To:")
print(DATASET_PATH)

print("\nFirst 5 Rows:")
print(df.head())