import pandas as pd

def main():
    """
    Load and clean the CIMIS weather dataset.
    """
    input_path = "../data/raw/CIMIS_5station_5year_data_set.csv"

    df = pd.read_csv(input_path)

    selected_columns = [
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
    ]

    df = df[selected_columns]

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.dropna()

    print("\nDataset after removing missing values:")
    print(df.shape)

    print("\nRemaining missing values:")
    print(df.isna().sum())

    output_path = "../data/processed/CIMIS_daily_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"\nSaved processed dataset to {output_path}")


if __name__ == "__main__":
    main()