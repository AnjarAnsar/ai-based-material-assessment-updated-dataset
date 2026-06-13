print("STARTED")

import pandas as pd
import numpy as np
import os

from sklearn.metrics.pairwise import euclidean_distances

# =========================
# LOAD DATASET
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "materials.csv"
)

df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully")


# =========================
# RECOMMENDATION FUNCTION
# =========================

def recommend_materials(
    predicted_wear_rate,
    predicted_friction,
    top_n=5
):

    print("\nPredicted Values:")
    print("Wear Rate:", predicted_wear_rate)
    print("Friction Coefficient:", predicted_friction)

    # =========================
    # USER VECTOR
    # =========================

    user_vector = np.array([[
        predicted_wear_rate,
        predicted_friction
    ]])

    # =========================
    # DATASET VECTORS
    # =========================

    dataset_vectors = df[[
        "WearRate",
        "FrictionCoefficient"
    ]].values

    # =========================
    # EUCLIDEAN DISTANCE
    # =========================

    distances = euclidean_distances(
        user_vector,
        dataset_vectors
    )

    distances = distances[0]

    # =========================
    # CONVERT TO SIMILARITY
    # =========================

    similarities = 1 / (1 + distances)

    # =========================
    # CREATE COPY
    # =========================

    recommended = df.copy()

    recommended["Similarity"] = similarities * 100

    # =========================
    # SORT MATERIALS
    # =========================

    recommended = recommended.sort_values(
        by="Similarity",
        ascending=False
    )

    print("\nSorted Similarity Scores:\n")

    # for _, row in recommended.iterrows():

    #     print(
    #         f"{row['Material']} : "
    #         f"{row['Similarity']:.2f}%"
    #     ) 

    # =========================
    # REMOVE DUPLICATES
    # =========================

    recommended = recommended.drop_duplicates(
        subset=["Material"],
        keep="first"
    )

    # =========================
    # TOP MATERIALS
    # =========================

    top_materials = recommended.head(top_n)

    # =========================
    # FINAL RESULTS
    # =========================

    results = []

    for _, row in top_materials.iterrows():


        # =========================
        # SMART EXPLANATION
        # =========================

        reasons = []

        # MATERIAL-SPECIFIC WEAR ANALYSIS
        if row["WearRate"] < predicted_wear_rate:
            reasons.append(
                "better wear resistance"
            )

        # MATERIAL-SPECIFIC FRICTION ANALYSIS
        if row["FrictionCoefficient"] < predicted_friction:
            reasons.append(
                "lower friction behavior"
            )

        # HIGH SIMILARITY
        if row["Similarity"] > 90:
            reasons.append(
                "excellent operating condition match"
            )

        elif row["Similarity"] > 70:
            reasons.append(
                "good compatibility with operating conditions"
            )

        # FALLBACK
        if not reasons:
            reasons.append(
                "balanced engineering characteristics"
            )

        reason = (
            f"{row['Material']} is recommended because it provides "
            + ", ".join(reasons)
            + "."
        )

        results.append({

            "Material": row["Material"],

            "WearRate": round(
                row["WearRate"], 4
            ),

            "FrictionCoefficient": round(
                row["FrictionCoefficient"], 4
            ),

            "SimilarityScore": round(
                row["Similarity"], 2
            ),

            "Explanation": reason
        })

    return results