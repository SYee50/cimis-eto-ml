import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def load_data():
    """
    Load the cleaned CIMIS weather dataset.
    """
    input_path = "../data/processed/CIMIS_daily_clean.csv"
    return pd.read_csv(input_path)


def get_features():
    """
    Return the weather features used by the experiment.
    """
    return [
        "Precip (mm)",
        "Avg Sol Rad (W/m²)",
        "Avg Vap Pres (kPa)",
        "Max Air Temp (°C)",
        "Min Air Temp (°C)",
        "Avg Air Temp (°C)",
        "Max Rel Hum (%)",
        "Min Rel Hum (%)",
        "Avg Rel Hum (%)",
        "Dew Point (°C)",
        "Avg Wind Speed (m/s)"
    ]


def train_random_forest(X_train, y_train):
    """
    Train a Random Forest regression model.
    """
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model

def run_experiment_1(df, features):
    """
    Run experiment 1 using weather variables only
    """
    # Separate features from target
    X = df[features]
    y = df["ETo (mm)"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    print(f"Experiment 1 training observations: {len(X_train)}")
    print(f"Experiment 1 testing observations: {len(X_test)}")

    # Baseline
    baseline_prediction = y_train.mean()
    baseline_predictions = [baseline_prediction] * len(y_test)

    print("\nBaseline predictions:")
    print(baseline_predictions[:5])

    # Linear Regression
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    linear_predictions = linear_model.predict(X_test)

    print("\nLinear Regression predictions:")
    print(linear_predictions[:5])

    # Random Forest
    random_forest_model = train_random_forest(
        X_train,
        y_train
    )

    random_forest_predictions = random_forest_model.predict(X_test)

    print("\nRandom Forest predictions:")
    print(random_forest_predictions[:5])

    # Save Predictions
    predictions_df = pd.DataFrame({
        "ETo (mm)": y_test.to_numpy(),
        "Baseline": baseline_predictions,
        "Linear Regression": linear_predictions,
        "Random Forest": random_forest_predictions
    })

    output_path = "../results/experiment_1/predictions/test_predictions.csv"

    predictions_df.to_csv(output_path, index=False)

    print(f"\nSaved Experiment 1 predictions to {output_path}")


def run_experiment_2(df, features):
    """
    Run Experiment 2 comparing weather variables with weather variables plus Day of Year.
    """
    X = df[features]
    y = df["ETo (mm)"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Weather only
    weather_model = train_random_forest(
        X_train,
        y_train
    )

    weather_predictions = weather_model.predict(X_test)

    print("\nExperiment 2: Weather Only predictions")
    print(weather_predictions[:5])

    # Weather + Day of Year
    seasonality_features = features + ["Jul"]

    X_seasonality = df[seasonality_features]

    X_train_seasonality, X_test_seasonality, y_train_seasonality, y_test_seasonality = train_test_split(
        X_seasonality,
        y,
        test_size=0.20,
        random_state=42
    )

    seasonality_model = train_random_forest(
        X_train_seasonality,
        y_train_seasonality
    )

    seasonality_predictions = seasonality_model.predict(X_test_seasonality)

    print("\nExperiment 2: Weather + Day of Year predictions:")
    print(seasonality_predictions[:5])

    # Save predictions
    predictions_df = pd.DataFrame({
        "ETo (mm)": y_test.to_numpy(),
        "Weather Only": weather_predictions,
        "Weather + Day of Year": seasonality_predictions
    })

    output_path = "../results/experiment_2/predictions/test_predictions.csv"

    predictions_df.to_csv(output_path, index=False)

    print(f"\nSaved Experiment 2 predictions to {output_path}")


def run_experiment_3(df, features):
    """
    Evaluate geographic generalization across held-out stations.
    """
    stations = df["Station Name"].unique()

    results = []

    for station in stations:
        train_df = df[df["Station Name"] != station]
        test_df = df[df["Station Name"] == station]

        X_train = train_df[features]
        y_train = train_df["ETo (mm)"]

        X_test = test_df[features]
        y_test = test_df["ETo (mm)"]

        random_forest_model = train_random_forest(
            X_train,
            y_train
        )

        predictions = random_forest_model.predict(X_test)

        print(f"\nExperiment 3: {station} station-hold-out predictions:")
        print(predictions[:5])

        predictions_df = test_df[[
            "Station Number",
            "Station Name",
            "CIMIS Region",
            "Date",
            "Jul",
            "ETo (mm)",
            "Precip (mm)",
            "Avg Sol Rad (W/m²)",
            "Avg Vap Pres (kPa)",
            "Max Air Temp (°C)",
            "Min Air Temp (°C)",
            "Avg Air Temp (°C)",
            "Max Rel Hum (%)",
            "Min Rel Hum (%)",
            "Avg Rel Hum (%)",
            "Dew Point (°C)",
            "Avg Wind Speed (m/s)"
        ]].copy()

        predictions_df["Random Forest"] = predictions

        results.append(predictions_df)

    predictions_df = pd.concat(results, ignore_index=True)

    output_path = "../results/experiment_3/predictions/test_predictions.csv"

    predictions_df.to_csv(output_path, index=False)

    print(f"\nSaved Experiment 3 predictions to {output_path}")


def main():
    """
    Run the machine learning experiments.
    """
    df = load_data()

    features = get_features()

    run_experiment_1(df, features)
    run_experiment_2(df, features)
    run_experiment_3(df, features)


if __name__ == "__main__":
    main()
