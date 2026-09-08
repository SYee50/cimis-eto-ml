import json

import numpy as np
import pandas as pd

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def calculate_metrics(actual, predictions):
    """
    Calculate MAE, RMSE, and R² for a set of predictions.
    """
    mae = mean_absolute_error(actual, predictions)
    rmse = np.sqrt(mean_squared_error(actual, predictions))
    r2 = r2_score(actual, predictions)

    return {
        "MAE": float(mae),
        "RMSE": float(rmse),
        "R2": float(r2)
    }


def evaluate_experiment_1():
    """
    Evaluate the models from Experiment 1
    """
    input_path = "../results/experiment_1/predictions/test_predictions.csv"

    predictions_df = pd.read_csv(input_path)

    models = [
        "Baseline",
        "Linear Regression",
        "Random Forest"
    ]

    results = {}

    for model in models:
        metrics = calculate_metrics(
            predictions_df["Actual ETo (mm)"],
            predictions_df[model]
        )

        results[model] = metrics

    print("\nExperiment 1 results:")

    for model, metrics in results.items():
        print(f"\n{model}")
        print(f"MAE: {metrics['MAE']:.3f}")
        print(f"RMSE: {metrics['RMSE']:.3f}")
        print(f"R²: {metrics['R2']:.3f}")

    output_path = "../results/experiment_1/metrics/model_results.json"

    with open(output_path, "w") as file:
        json.dump(results, file, indent=4)

    print(f"\nSaved Experiment 1 results to {output_path}")


def evaluate_experiment_2():
    """
    Evaluate the Random Forest models from Experiment 2
    """
    input_path = "../results/experiment_2/predictions/test_predictions.csv"

    predictions_df = pd.read_csv(input_path)

    models = [
        "Weather Only",
        "Weather + Day of Year"
    ]

    results = {}

    for model in models:
        metrics = calculate_metrics(
            predictions_df["Actual ETo (mm)"],
            predictions_df[model]
        )

        results[model] = metrics

    print("\nExperiment 2 results:")

    for model, metrics in results.items():
        print(f"\n{model}")
        print(f"MAE: {metrics['MAE']:.3f}")
        print(f"RMSE: {metrics['RMSE']:.3f}")
        print(f"R²: {metrics['R2']:.3f}")

    output_path = "../results/experiment_2/metrics/model_results.json"

    with open(output_path, "w") as file:
        json.dump(results, file, indent=4)

    print(f"\nSaved Experiment 2 results to {output_path}")


def evaluate_experiment_3():
    """
    Evaluate geographic generalization across held-out stations.
    """
    input_path = "../results/experiment_3/predictions/test_predictions.csv"

    predictions_df = pd.read_csv(input_path)

    results = {}

    for station in predictions_df["Station"].unique():
        station_df = predictions_df[
            predictions_df["Station"] == station
        ]

        metrics = calculate_metrics(
            station_df["Actual ETo (mm)"],
            station_df["Random Forest"]
        )

        results[station] = metrics

    print("\nExperiment 3 results:")

    for station, metrics in results.items():
        print(f"\n{station}")
        print(f"MAE: {metrics['MAE']:.3f}")
        print(f"RMSE: {metrics['RMSE']:.3f}")
        print(f"R²: {metrics['R2']:.3f}")

    output_path = "../results/experiment_3/metrics/model_results.json"

    with open(output_path, "w") as file:
        json.dump(results, file, indent=4)

    print(f"\nSaved Experiment 3 results to {output_path}")


def main():
    """
    Evaluate the machine learning experiments.
    """
    evaluate_experiment_1()
    evaluate_experiment_2()
    evaluate_experiment_3()


if __name__ == "__main__":
    main()
