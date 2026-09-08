import json
import os
import matplotlib.pyplot as plt
import pandas as pd


def load_predictions(experiment_number):
    """
    Load predictions and test observations for the specified experiment.
    """
    input_path = f"../results/experiment_{experiment_number}/predictions/test_predictions.csv"
    return pd.read_csv(input_path)


def calculate_errors(predictions_df, prediction_column):
    """
    Calculate prediction errors for the specified prediction column.
    """
    predictions_df["Error"] = (
        predictions_df[prediction_column]
        - predictions_df["ETo (mm)"]
    )

    predictions_df["Absolute Error"] = predictions_df["Error"].abs()

    return predictions_df


def compare_experiment_2_models():
    """
    Compare the performance of the two models from Experiment 2.
    """
    input_path = "../results/experiment_2/metrics/model_results.json"

    with open(input_path) as file:
        results = json.load(file)

    weather_only = results["Weather Only"]
    weather_seasonality = results["Weather + Day of Year"]

    print("\nExperiment 2 model comparison:")

    for metric in ["MAE", "RMSE", "R2"]:
        weather_value = weather_only[metric]
        seasonality_value = weather_seasonality[metric]

        difference = seasonality_value - weather_value

        print(f"\n{metric}")
        print(f"Weather Only: {weather_value:.3f}")
        print(f"Weather + Day of Year: {seasonality_value:.3f}")
        print(f"Difference: {difference:.3f}")


def analyze_overall_error(predictions_df):
    """
    Calculate overall error statistics.
    """
    print("\nError summary:")
    print(predictions_df["Error"].describe())

    print("\nAbsolute error summary:")
    print(predictions_df["Absolute Error"].describe())


def analyze_station_error(predictions_df):
    """
    Analyze prediction error by station.
    """
    station_errors = predictions_df.groupby("Station Name")["Absolute Error"].agg(
        ["mean", "median", "max"]
    )

    print("\nError by station:")
    print(station_errors)


def analyze_eto_range_error(predictions_df):
    """
    Analyze prediction error by actual ETo range.
    """
    eto_bins = [0, 2, 5, 8, float("inf")]
    eto_labels = ["0–2 mm", "2–5 mm", "5–8 mm", ">8 mm"]

    predictions_df["ETo Range"] = pd.cut(
        predictions_df["ETo (mm)"],
        bins=eto_bins,
        labels=eto_labels,
        include_lowest=True
    )

    eto_errors = predictions_df.groupby(
        "ETo Range",
        observed=False
    )["Absolute Error"].agg(
        ["mean", "median", "max", "count"]
    )

    print("\nError by ETo range:")
    print(eto_errors)


def plot_actual_vs_predicted(
    predictions_df,
    prediction_column,
    experiment_number
):
    """
    Plot actual ETo against predicted ETo.
    """
    output_directory = f"../results/experiment_{experiment_number}/plots"
    os.makedirs(output_directory, exist_ok=True)

    plt.figure(figsize=(8, 6))

    plt.scatter(
        predictions_df["ETo (mm)"],
        predictions_df[prediction_column],
        alpha=0.3
    )

    plt.plot(
        [0, 12],
        [0, 12],
        linestyle="--"
    )

    plt.xlabel("Actual ETo (mm)")
    plt.ylabel("Predicted ETo (mm)")
    plt.title(f"Actual vs Predicted ETo: {prediction_column}")

    plt.tight_layout()

    output_path = (
        f"{output_directory}/"
        f"actual_vs_predicted_{prediction_column.replace(' ', '_').replace('+', 'plus')}.png"
    )

    plt.savefig(output_path, dpi=300)
    plt.show()
    plt.close()


def plot_error_distribution(
    predictions_df,
    prediction_column,
    experiment_number
):
    """
    Plot the distribution of prediction errors.
    """
    output_directory = f"../results/experiment_{experiment_number}/plots"
    os.makedirs(output_directory, exist_ok=True)

    plt.figure(figsize=(8, 6))

    plt.hist(
        predictions_df["Error"],
        bins=40
    )

    plt.axvline(
        0,
        linestyle="--"
    )

    plt.xlabel("Prediction Error (mm)")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Prediction Errors: {prediction_column}")

    plt.tight_layout()

    output_path = (
        f"{output_directory}/"
        f"error_distribution_{prediction_column.replace(' ', '_').replace('+', 'plus')}.png"
    )

    plt.savefig(output_path, dpi=300)
    plt.show()
    plt.close()


def plot_error_vs_actual(
    predictions_df,
    prediction_column,
    experiment_number
):
    """
    Plot prediction error against actual ETo.
    """
    output_directory = f"../results/experiment_{experiment_number}/plots"
    os.makedirs(output_directory, exist_ok=True)

    plt.figure(figsize=(8, 6))

    plt.scatter(
        predictions_df["ETo (mm)"],
        predictions_df["Error"],
        alpha=0.3
    )

    plt.axhline(
        0,
        linestyle="--"
    )

    plt.xlabel("Actual ETo (mm)")
    plt.ylabel("Prediction Error (mm)")
    plt.title(f"Prediction Error vs Actual ETo: {prediction_column}")

    plt.tight_layout()

    output_path = (
        f"{output_directory}/"
        f"error_vs_actual_{prediction_column.replace(' ', '_').replace('+', 'plus')}.png"
    )

    plt.savefig(output_path, dpi=300)
    plt.show()
    plt.close()


def run_error_analysis_experiment_1():
    """
    Run error analysis for Experiment 1.
    """
    predictions_df = load_predictions(1)

    models = [
        "Baseline",
        "Linear Regression",
        "Random Forest"
    ]

    for model in models:
        predictions_df = calculate_errors(
            predictions_df,
            model
        )

        print(f"\n{model}")

        analyze_overall_error(
            predictions_df
        )

        analyze_eto_range_error(
            predictions_df
        )

        if model != "Baseline":
            plot_actual_vs_predicted(
                predictions_df,
                model,
                1
            )

            plot_error_distribution(
                predictions_df,
                model,
                1
            )

            plot_error_vs_actual(
                predictions_df,
                model,
                1
            )


def run_error_analysis_experiment_2():
    """
    Run error analysis for Experiment 2.
    """
    predictions_df = load_predictions(2)

    compare_experiment_2_models()

    # Weather Only
    predictions_df = calculate_errors(
        predictions_df,
        "Weather Only"
    )

    print("\nWeather Only")

    analyze_overall_error(
        predictions_df
    )

    analyze_eto_range_error(
        predictions_df
    )

    plot_actual_vs_predicted(
        predictions_df,
        "Weather Only",
        2
    )

    plot_error_distribution(
        predictions_df,
        "Weather Only",
        2
    )

    plot_error_vs_actual(
        predictions_df,
        "Weather Only",
        2
    )

    # Weather + Day of Year
    predictions_df = calculate_errors(
        predictions_df,
        "Weather + Day of Year"
    )

    print("\nWeather + Day of Year")

    analyze_overall_error(
        predictions_df
    )

    analyze_eto_range_error(
        predictions_df
    )

    plot_actual_vs_predicted(
        predictions_df,
        "Weather + Day of Year",
        2
    )

    plot_error_distribution(
        predictions_df,
        "Weather + Day of Year",
        2
    )

    plot_error_vs_actual(
        predictions_df,
        "Weather + Day of Year",
        2
    )


def run_error_analysis_experiment_3():
    """
    Run error analysis for Experiment 3.
    """
    predictions_df = load_predictions(3)

    predictions_df = calculate_errors(
        predictions_df,
        "Random Forest"
    )

    analyze_overall_error(
        predictions_df
    )

    analyze_station_error(
        predictions_df
    )

    analyze_eto_range_error(
        predictions_df
    )

    plot_actual_vs_predicted(
        predictions_df,
        "Random Forest",
        3
    )

    plot_error_distribution(
        predictions_df,
        "Random Forest",
        3
    )

    plot_error_vs_actual(
        predictions_df,
        "Random Forest",
        3
    )


def main():
    """
    Run error analysis.
    """
    run_error_analysis_experiment_1()
    run_error_analysis_experiment_2()
    run_error_analysis_experiment_3()


if __name__ == "__main__":
    main()