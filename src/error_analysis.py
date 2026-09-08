import pandas as pd

import matplotlib.pyplot as plt

def load_predictions():
    """
    Load Experiment 3 predictions and test observations
    """
    input_path = "../results/experiment_3/predictions/test_predictions.csv"

    return pd.read_csv(input_path)


def calculate_errors(predictions_df):
    """
    Calculate prediction errors.
    """
    predictions_df["Error"] = (
        predictions_df["Random Forest"] - predictions_df["ETo (mm)"]
    )

    predictions_df["Absolute Error"] = predictions_df["Error"].abs()

    return predictions_df


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


def plot_actual_vs_predicted(predictions_df):
    """
    Plot actual ETo against predicted ETo.
    """
    plt.figure(figsize=(8, 6))

    plt.scatter(
        predictions_df["ETo (mm)"],
        predictions_df["Random Forest"],
        alpha=0.3
    )

    plt.plot(
        [0, 12],
        [0, 12],
        linestyle="--"
    )

    plt.xlabel("Actual ETo (mm)")
    plt.ylabel("Predicted ETo (mm)")
    plt.title("Actual vs Predicted ETo")

    plt.tight_layout()
    plt.show()


def plot_error_distribution(predictions_df):
    """
    Plot the distribution of prediction errors.
    """
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
    plt.title("Distribution of Prediction Errors")

    plt.tight_layout()
    plt.show()


def plot_error_vs_actual(predictions_df):
    """
    Plot prediction error against actual ETo.
    """
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
    plt.title("Prediction Error vs Actual ETo")

    plt.tight_layout()
    plt.show()


def main():
    """
    Run error analysis.
    """
    predictions_df = load_predictions()
    predictions_df = calculate_errors(predictions_df)

    analyze_overall_error(predictions_df)
    analyze_station_error(predictions_df)
    analyze_eto_range_error(predictions_df)

    plot_actual_vs_predicted(predictions_df)
    plot_error_distribution(predictions_df)
    plot_error_vs_actual(predictions_df)


if __name__ == "__main__":
    main()